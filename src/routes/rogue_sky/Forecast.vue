<template>
  <section>
    <Loading v-if="star_forecast === null" />
    <div v-else>
      <div id="search-wrapper">
        <Search v-bind:value="city + ', ' + state" />
        <div id="scrolling-wrapper">
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
          <vue-fontawesome :icon="getIcon(today.icon)" size="5x" />
        </div>
        <div id="current-summary-text">{{ today.summary }}</div>
        <div>Sunset today is at {{ today.sunset_time_local | moment("h:MM a") }}</div>
      </div>
      <b-table id="forecast-table" :data="star_forecast" class="container" hoverable narrowed>
        <template slot-scope="props">
          <b-table-column>
            <span>
              {{ props.row.weather_date_local | moment("calendar", null, {
              sameDay: '[Today]',
              nextDay: '[Tomorrow]',
              nextWeek: 'dddd',
              sameElse: '[Next] dddd'
              }) }}
            </span>
          </b-table-column>
          <b-table-column
            label="Star Visibility"
            centered
            numeric
          >{{ (props.row.star_visibility * 100).toFixed(0) }}%</b-table-column>
          <b-table-column class="day-summary" label="Summary" centered width="300">
            <span>
            {{ props.row.summary }}
            <span
              v-if="props.row.precip_probability > 0.2"
            >There is a {{ (props.row.precip_probability * 100).toFixed(0) }}% of {{ getPrecipitationIdentifier(props.row.precip_intensity_max_in_hr) }} {{ props.row.precip_type }}.</span>
            </span>
          </b-table-column>
          <b-table-column
            label="Cloud Cover"
            centered
            numeric
          >{{ (props.row.cloud_cover_pct * 100).toFixed(0) }}%</b-table-column>
          <b-table-column
            label="Moon Phase"
            centered
            numeric
          >{{ (props.row.moon_phase_pct * 100).toFixed(0) }}%</b-table-column>
          <b-table-column label="Temperature" centered>
            <div>Low: {{ props.row.temperature_min_f.toFixed(0) }}°F</div>
            <div>High: {{ props.row.temperature_max_f.toFixed(0) }}°F</div>
          </b-table-column>
        </template>
        <template slot="footer">
          <div id="table-footer" class="has-text-right">from darksky</div>
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
    },
    getIcon(icon) {
      let iconLookup = {
        snow: "snowflake",
        "clear-day": "moon",
        "clear-night": "moon",
        sleet: "cloud-showers-heavy",
        wind: "wind",
        fog: "cloud",
        cloudy: "cloud",
        "partly-cloudy-day": "cloud-moon",
        "partly-cloudy-night": "cloud-moon",
        rain: "cloud-moon-rain"
      };
      return iconLookup[icon];
    },
    getPrecipitationIdentifier(precip_in_per_hour) {
      if (precip_in_per_hour < 0.1) {
        return "light";
      } else if (precip_in_per_hour < 0.3) {
        return "moderate";
      } else {
        return "heavy";
      }
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

#table-footer {
  font-weight: normal;
  color: rgba(119, 136, 153, 0.349);
  font-size: 80%;
}

#scrolling-wrapper {
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

#forecast-table td {
  vertical-align: middle;
}

#forecast-table span {
  text-align: right;
}
</style>
