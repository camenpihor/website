<template>
  <section>
    <Loading v-if="star_forecast === null" />
    <div v-else>
      <div id="search-wrapper">
        <Search v-bind:value="city + ', ' + state" />
        <div class="scrolling-wrapper">
          <div
            class="scrolling-card"
            v-for="prediction in star_forecast"
            v-bind:key="prediction.weather_date_utc"
          >
            <p>
              <vue-fontawesome v-if="prediction.star_visibility < 0.5" icon="cloud" />
              <vue-fontawesome v-else-if="prediction.star_visibility < 0.85" icon="cloud-moon" />
              <vue-fontawesome v-else icon="moon" />
            </p>
            {{ prediction.weather_date_local | moment("MMM DD") }}
          </div>
        </div>
      </div>
      <div id="current-summary">
        <div id="icon-current-summary">
          <vue-fontawesome v-if="today.icon === 'rain'" icon="cloud-moon-rain" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'snow'" icon="snowflake" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'clear-day'" icon="moon" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'clear-night'" icon="moon" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'sleet'" icon="cloud-showers-heavy" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'wind'" icon="wind" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'fog'" icon="cloud" size="5x" />
          <vue-fontawesome v-else-if="today.icon === 'cloudy'" icon="cloud" size="5x" />
          <vue-fontawesome
            v-else-if="today.icon === 'partly-cloudy-day'"
            icon="cloud-moon"
            size="5x"
          />
          <vue-fontawesome
            v-else-if="today.icon === 'partly-cloudy-night'"
            icon="cloud-moon"
            size="5x"
          />
          <vue-fontawesome v-else icon="cloud-moon" size="3x" />
        </div>
        <div id="current-summary-text">{{ today.summary }}</div>
      </div>
      <b-table id="forecast-table" :data="star_forecast" class="container">
        <template slot-scope="props">
          <b-table-column label="Date" centered>{{ props.row.weather_date_local | moment("dddd") }}</b-table-column>
          <b-table-column
            label="Star Visibility"
            centered
            numeric
          >{{ (props.row.star_visibility * 100).toFixed(0) }}%</b-table-column>
          <b-table-column label="Summary" centered>{{ props.row.summary }}</b-table-column>
          <b-table-column
            label="Cloud Cover"
            centered
            numeric
          >{{ (props.row.cloud_cover_pct * 100).toFixed(0) }}%</b-table-column>
          <b-table-column
            label="Sunset"
            centered
          >{{ props.row.sunset_time_local | moment("h:MM a") }}</b-table-column>
          <b-table-column
            label="Moon Phase"
            centered
            numeric
          >{{ (props.row.moon_phase_pct * 100).toFixed(0) }}%</b-table-column>
          <b-table-column
            label="Precipitation"
            class="capitalize"
            centered
          >{{ props.row.precip_type }} ({{ (props.row.precip_probability * 100).toFixed(0) }}%)</b-table-column>
          <b-table-column
            label="Temperature"
            centered
          >{{ props.row.temperature_min_f.toFixed(0) }}°F - {{ props.row.temperature_max_f.toFixed(0) }}°F</b-table-column>
        </template>
      </b-table>
    </div>
  </section>
</template>

<script>
import { getStarForecast } from "@/api.js";
import Search from "@/components/rogue_sky/Search.vue";
import Loading from "@/components/Loading.vue";

export default {
  name: "forecast",
  components: {
    Search,
    Loading
  },
  data() {
    return {
      today: null,
      star_forecast: null,
      city: null,
      state: null
    };
  },
  methods: {
    getForecast(latitude, longitude) {
      getStarForecast(latitude, longitude)
        .then(response => {
          this.star_forecast = response.data.daily_forecast;
          this.today = this.star_forecast[0];
          this.city = response.data.city;
          this.state = response.data.state;
        })
        .catch(() => {
          this.$router.push({ name: "404" });
        });
    }
  },
  mounted() {
    this.getForecast(this.$route.params.latitude, this.$route.params.longitude);
  },
  watch: {
    $route() {
      this.getForecast(
        this.$route.params.latitude,
        this.$route.params.longitude
      );
    }
  }
};
</script>

<style>
#search-wrapper {
  padding-top: 15px;
  padding-bottom: 15px;
  background-color: #6b606013;
}

#current-summary {
  margin-top: 50px;
  margin-bottom: 50px;
}

#current-summary-text {
  font-size: 200%;
  font-weight: bold;
}

.scrolling-wrapper {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
  padding-top: 10px;
}

.scrolling-card {
  display: inline-block;
  margin: 0 18px;
  font-size: 14px;
}

.capitalize {
  text-transform: capitalize;
}
</style>
