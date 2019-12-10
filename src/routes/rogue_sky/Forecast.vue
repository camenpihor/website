<template>
  <section>
    <Loading v-if="star_forecast === null"/>
    <div v-else>
      <Search v-bind:value="city + ', ' + state" />
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
      <div id="forecast-summary" class="columns is-centered is-multiline">
        <div v-for="prediction in star_forecast" v-bind:key="prediction.weather_date_utc" >
          <div class="column">
            <p>
              <vue-fontawesome v-if="prediction.star_visibility < 0.5" icon="cloud"/>
              <vue-fontawesome
                v-else-if="prediction.star_visibility < 0.85"
                icon="cloud-moon"
              />
              <vue-fontawesome v-else icon="moon"/>
            </p>
            {{ prediction.weather_date_local }}
          </div>
        </div>
      </div>
      <b-table id="forecast-table" :data="star_forecast" :columns="columns"></b-table>
    </div>
  </section>
</template>

<script>
import { getStarForecast } from "@/api.js";
import Search from "@/components/rogue_sky/Search.vue";
import Loading from "@/components/Loading.vue"

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
      state: null,
      isFullPage: true,
      columns: [
        {
          field: "weather_date_local",
          label: "Date",
          centered: true
        },
        {
          field: "star_visibility",
          label: "Star Visibility",
          centered: true,
          numeric: true
        },
        {
          field: "summary",
          label: "Summary",
          centered: true
        },
        {
          field: "cloud_cover_pct",
          label: "Clould Cover",
          centered: true
        },
        {
          field: "sunset_time_local",
          label: "Sunset",
          centered: true
        },
        {
          field: "moon_phase_pct",
          label: "Moon Phase",
          centered: true
        },
        {
          field: "precip_probability",
          label: "Precipitation Probability",
          centered: true
        },
        {
          field: "precip_type",
          label: "Pricipitation Type",
          centered: true
        },
        {
          field: "temperature_min_f",
          label: "Min Temperature",
          centered: true
        },
        {
          field: "temperature_max_f",
          label: "Max Temperature",
          centered: true
        }
      ]
    };
  },
  methods: {
    getForecast(latitude, longitude,) {
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
    this.getForecast(
      this.$route.params.latitude, this.$route.params.longitude
    );
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
#icon-current-summary {
  margin-top: 30px;
}

#current-summary-text {
  font-size: 200%;
  font-weight: bold;
}

#forecast-summary {
  margin-top: 10px;
}

#forecast-table {
  margin-top: 30px;
}
</style>
