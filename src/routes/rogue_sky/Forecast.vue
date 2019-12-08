<template>
  <section>

    <div v-if="star_forecast !== null">
      <Search v-bind:value="city + ', ' + state"/>
      <div id="current-summary">
        <div id="icon-current-summary">
          <vue-fontawesome v-if="today.icon === 'rain'" icon="cloud-moon-rain" size="3x"/>
          <vue-fontawesome v-else-if="today.icon === 'snow'" icon="snowflake" size="3x"/>
          <vue-fontawesome v-else-if="today.icon === 'clear-day'" icon="sun" size="3x"/>
          <vue-fontawesome
            v-else-if="today.icon === 'clear-night'"
            icon="moon"
            size="3x"
          />
          <vue-fontawesome
            v-else-if="today.icon === 'sleet'"
            icon="cloud-showers-heavy"
            size="3x"
          />
          <vue-fontawesome v-else-if="today.icon === 'wind'" icon="wind" size="3x"/>
          <vue-fontawesome v-else-if="today.icon === 'fog'" icon="cloud" size="3x"/>
          <vue-fontawesome v-else-if="today.icon === 'cloudy'" icon="cloud" size="3x"/>
          <vue-fontawesome
            v-else-if="today.icon === 'partly-cloudy-day'"
            icon="cloud-sun"
            size="3x"
          />
          <vue-fontawesome
            v-else-if="today.icon === 'partly-cloudy-night'"
            icon="cloud-moon"
            size="3x"
          />
          <vue-fontawesome v-else icon="cloud-moon" size="3x"/>
        </div>
        <div id="current-summary">
          {{ today.summary }}
        </div>
      </div>
      <b-table :data="star_forecast" :columns="columns"></b-table>
    </div>
  </section>
</template>

<script>
import { getStarForecast } from "@/api.js";
import Search from "@/components/rogue_sky/Search.vue";

export default {
  name: "forecast",
  components: {
    Search
  },
  data() {
    return {
      today: null,
      star_forecast: null,
      city: null,
      state: null,
      columns: [
        {
          field: "weather_date_utc",
          label: "Date",
          centered: true
        },
        {
          field: "star_visibility",
          label: "Visibility",
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
          field: "sunset_time_utc",
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
          label: "Precipitation %",
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
    getForecast(latitude, longitude) {
      getStarForecast(latitude, longitude).then(response => {
        this.star_forecast = response.data.daily_forecast;
        this.today = this.star_forecast[0];
        this.city = response.data.city;
        this.state = response.data.state;
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
#icon-current-summary {
  margin-top: 10px;
}

#current-summary {
  font-size: 150%;
  font-weight: bold;
}
</style>
