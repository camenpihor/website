<template>
  <section>
    <EventListener :method="searchListener" />

    <div v-if="error" class="section">
      <BackendSearch
        class="rogue-sky__search"
        placeholder="search address..."
        :method="search"
        ref="search"
        :imageFilePath="personHangingFilePath"
      />
      <NotFound :requestedPath="this.$route.fullPath" />
    </div>
    <Loading v-if="!error & (starForecast == null)" :isFullPage="false" />
    <div v-if="starForecast != null">
      <div class="section">
        <BackendSearch
          class="rogue-sky__search"
          placeholder="search address..."
          :method="search"
          ref="search"
          :imageFilePath="personHangingFilePath"
        />
        <h1 class="title is-3 has-text-centered">
          {{ this.city }}, {{ this.state }}
        </h1>
        <div class="level is-mobile rogue-sky__icon-summary">
          <StarVizIcon
            class="level-item has-text-centered is-size-7"
            v-for="star in starForecast"
            :key="star.weather_date_local"
            :word="star.icon"
            :date="humanizeDate(star.weather_date_local)"
          />
        </div>
        <hr />

        <div class="rogue-sky__map__wrapper">
          <Map
            class="rogue-sky__map__image"
            :latitude="parseFloat(latitude)"
            :longitude="parseFloat(longitude)"
            :zoom="6"
            :onLoad="cloudCoverLayer"
          />
        </div>
      </div>

      <div class="section">
        <p class="title is-3 has-text-centered">Weather</p>
        <p class="subtitle is-7 has-text-centered">
          daily weather summaries
        </p>
        <b-tabs position="is-centered" expanded>
          <b-tab-item
            v-for="dailyWeather in starForecast"
            :key="dailyWeather.weather_date_local"
          >
            <template slot="header">
              <StarVizIcon
                class="level-item has-text-centered is-size-7"
                :word="dailyWeather.icon"
                :date="humanizeDate(dailyWeather.weather_date_local)"
              />
            </template>
            <p class="title is-5 has-text-centered">
              {{
                dailyWeather.weather_date_local | moment("dddd, MMMM Do YYYY")
              }}
            </p>
            <p class="subtitle is-7 has-text-centered">
              <span>{{ dailyWeather.summary }}</span>
            </p>
            <div class="subsection">
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Star Visibility</span
                >
                <span class="column is-capitalized">{{
                  humanizeStarVisibility(dailyWeather.star_visibility)
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Cloud Cover</span
                >
                <span class="column">{{
                  floatToPercent(dailyWeather.cloud_cover_pct)
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Sunset</span
                >
                <span class="column">{{
                  dailyWeather.sunset_time_local
                    | moment("timezone", timezone, "h:mm a z")
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Moon Rise</span
                >
                <span class="column">{{
                  dailyWeather.moonrise_time_local
                    | moment("timezone", timezone, "h:mm a z")
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Moon Illumination</span
                >
                <span class="column"
                  >{{ floatToPercent(dailyWeather.moon_illumination) }}
                  <i
                    v-if="dailyWeather.moon_phase_pct < 0.5"
                    class="fal fa-long-arrow-up"
                  />
                  <i v-else class="fal fa-long-arrow-down" />
                </span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Precipitation</span
                >
                <span class="column">{{
                  humanizePrecipitation(
                    dailyWeather.precip_type,
                    dailyWeather.precip_intensity_max_in_hr,
                    dailyWeather.precip_probability
                  )
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Temperature</span
                >
                <span class="column">
                  <p>Low: {{ Math.round(dailyWeather.temperature_min_f) }}°F</p>
                  <p>
                    High: {{ Math.round(dailyWeather.temperature_max_f) }}°F
                  </p>
                </span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Wind</span
                >
                <span class="column"
                  >{{ Math.round(dailyWeather.wind_speed_mph) }} mph</span
                >
              </div>
            </div>
          </b-tab-item>
        </b-tabs>
      </div>

      <div class="section">
        <p class="title is-3 has-text-centered">Calendar</p>
        <p class="subtitle is-7 has-text-centered">
          Star visibility temporal projections | Astronomical events
        </p>
        <Calendar
          class="rogue-sky__calendar"
          :attributes="attributes"
          minDate="2020-01-02"
          maxDate="2021-01-01"
          :colorKey="calendarColors"
        />
      </div>

      <div class="section rogue-sky__additional-info">
        <p class="title is-3 has-text-centered">Additional Information</p>
        <ul class="has-text-centered">
          <li class="is-size-6">
            <a
              target="_blank"
              :href="
                `https://www.darksky.net/forecast/${latitude},${longitude}`
              "
              >darksky.net/forecast/{{ latitude }},{{ longitude }}</a
            >
          </li>
          <li class="is-size-6">
            <a
              target="_blank"
              href="https://www.darksitefinder.com/maps/world.html"
              >darksitefinder.com/maps/world.html</a
            >
          </li>
          <li class="is-size-6">
            <a target="_blank" href="https://www.darksky.org">darksky.org</a>
          </li>
          <li class="is-size-6">
            <a target="_blank" href="https://www.starwalk.space"
              >starwalk.space</a
            >
          </li>
        </ul>
      </div>
      <img class="person-mountain-moon" :src="personMountainMoonFilePath" />
    </div>
  </section>
</template>

<script>
import BackendSearch from "@/components/search/BackendSearch.vue";
import Calendar from "@/components/Calendar.vue";
import EventListener from "@/components/EventListener.vue";
import Loading from "@/components/Loading.vue";
import Map from "@/components/Map.vue";
import NotFound from "@/routes/NotFound.vue";
import StarVizIcon from "@/components/StarVizIcon.vue";

import { getCoordinates, getStarForecast } from "@/assets/js/api.js";
import astronomicalJson from "@/assets/json/astronomical_events.json";

export default {
  components: {
    BackendSearch,
    Calendar,
    EventListener,
    Loading,
    Map,
    NotFound,
    StarVizIcon
  },
  data() {
    return {
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      personMountainMoonFilePath: require("@/assets/people/person-mountain-moon.svg"),
      personWaveMoveFilePath: require("@/assets/people/person-wave-move.svg"),
      calendarColors: {
        best: "#d69e2e", // yellow
        moon: "green",
        eclipse: "gray",
        planetary: "red",
        meteorShower: "purple",
        other: "blue"
      },
      starForecast: null,
      timezone: null,
      city: null,
      state: null,
      latitude: null,
      longitude: null,
      error: false
    };
  },
  methods: {
    reset: function() {
      this.error = false;
      this.latitude = null;
      this.longitude = null;
      this.timezone = null;
      this.city = null;
      this.state = null;
      this.starForecast = null;
    },
    initialize: function() {
      this.reset();
      if (this.$route.query.address != null) {
        this.fetchCoordinates();
      } else if (
        this.$route.params.latitude !== undefined ||
        this.$route.params.longitude !== undefined
      ) {
        this.latitude = this.$route.params.latitude;
        this.longitude = this.$route.params.longitude;
        this.fetchForecast();
      } else {
        let seattle_lat = 47.687;
        let seattle_lon = -122.377;
        this.$router.replace({
          name: "rogue-sky-location",
          params: { latitude: seattle_lat, longitude: seattle_lon }
        });
      }
    },
    fetchCoordinates: function() {
      getCoordinates(this.$route.query.address)
        .then(response => {
          let latitude = response.data.latitude.toFixed(3);
          let longitude = response.data.longitude.toFixed(3);
          this.$router.replace({
            name: "rogue-sky-location",
            params: { latitude: latitude, longitude: longitude }
          });
        })
        .catch(() => {
          this.error = true;
        });
    },
    fetchForecast: function() {
      getStarForecast(this.latitude, this.longitude)
        .then(response => {
          this.timezone = response.data.timezone;
          this.starForecast = response.data.daily_forecast.slice(0, 7);
          this.city = response.data.city;
          this.state = response.data.state;
        })
        .catch(() => {
          this.error = true;
        });
    },
    humanizeStarVisibility: function(percent) {
      if (percent != null) {
        if (percent < 0.8) {
          return "poor";
        } else if (percent < 0.85) {
          return "fair";
        } else if (percent < 0.95) {
          return "good";
        } else {
          return "great";
        }
      }
    },
    floatToPercent: function(float) {
      return `${Math.round(float * 100)}%`;
    },
    humanizePrecipitation: function(type, intensity, probability) {
      if (probability < 0.01 || type == null) {
        return "None";
      }

      let percent = this.floatToPercent(probability);

      let intensityHuman;
      if (intensity < 0.1) {
        intensityHuman = "light";
      } else if (intensity < 0.3) {
        intensityHuman = "moderate";
      } else {
        intensityHuman = "heavy";
      }

      return `There is a ${percent} chance of ${intensityHuman} ${type}`;
    },
    search: function(input) {
      this.reset();
      this.$router.push({
        name: "rogue-sky",
        query: { address: input }
      });
    },
    searchListener: function(event) {
      let badTags = ["INPUT", "TEXTAREA"];
      if ((event.code === "Slash") & !badTags.includes(event.target.tagName)) {
        this.$refs.search.$el.getElementsByTagName("input")[0].focus();
      }
    },
    humanizeDate: function(date) {
      date = this.$moment(date);
      if (date.isSame(this.$moment(), "day")) {
        return "Today";
      } else {
        return date.format("ddd");
      }
    },
    cloudCoverLayer: function(map) {
      map.addLayer({
        id: "simple-tiles",
        type: "raster",
        source: {
          type: "raster",
          tiles: [
            `https://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid=${process.env.VUE_APP_WEATHERMAP_SECRET_TOKEN}`
          ],
          tileSize: 256
        },
        minzoom: 0,
        maxzoom: 22
      });
    }
  },
  computed: {
    today() {
      if (this.starForecast != null) {
        return this.starForecast[0];
      }
      return null;
    },
    bestDay() {
      if (this.starForecast != null) {
        let arr = this.starForecast;
        let maxObject = arr[0];

        for (let i = 0, len = arr.length; i < len; i++) {
          let current = arr[i];
          if (current.star_visibility > maxObject.star_visibility) {
            maxObject = current;
          }
        }
        return maxObject;
      }
      return null;
    },
    attributes() {
      if (this.starForecast != null) {
        let today = {
          key: "today",
          highlight: {
            color: "blue",
            fillMode: "light"
          },
          dates: new Date(),
          popover: {
            label: "Today",
            placement: "auto"
          },
          customData: { event: "Today" }
        };

        let bestDayEvent = `Best day of star visibility over the next week (${this.humanizeStarVisibility(
          this.bestDay.star_visibility
        )})`;
        let bestDay = {
          key: "bestDay",
          bar: "yellow",
          dates: this.bestDay.weather_date_local,
          popover: {
            label: bestDayEvent,
            placement: "auto"
          },
          customData: { event: bestDayEvent }
        };

        var allEvents = [today, bestDay];

        for (let dayForecast of this.starForecast) {
          if (
            dayForecast.weather_date_local !== this.bestDay.weather_date_local
          ) {
            allEvents.push({
              dates: dayForecast.weather_date_local,
              highlight: {
                color: "gray",
                fillMode: "light"
              },
              popover: {
                label: this.humanizeStarVisibility(dayForecast.star_visibility),
                placement: "auto",
                isInteractive: true
              },
              customData: {
                event: `Expected star visibility is ${this.humanizeStarVisibility(
                  dayForecast.star_visibility
                )}`
              }
            });
          }
        }
        for (const [label, data] of Object.entries(astronomicalJson)) {
          allEvents = allEvents.concat([
            ...data.map(datum => ({
              dates: datum.date,
              bar: this.calendarColors[label],
              popover: {
                label: datum.event,
                placement: "auto",
                isInteractive: true
              },
              customData: datum
            }))
          ]);
        }
        return allEvents;
      }
      return null;
    }
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        this.initialize();
      }
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>

<style>
.rogue-sky__search {
  margin-left: auto;
  margin-right: auto;
}

.rogue-sky__search .search__image {
  position: relative;
  top: -12px;
  left: 1rem;
}

.person-wave-move-image {
  float: right;
  position: relative;
  width: 1rem;
  right: 20%;
}

.rogue-sky__icon-summary {
  max-width: 25rem;
  margin-left: auto;
  margin-right: auto;
}

.rogue-sky__weather__item {
  margin: 0 0 0.5rem 0 !important;
}

.rogue-sky__weather__item .column {
  padding: 0;
}

.rogue-sky__map__wrapper {
  height: 50vh; /* same height as map */
}

.rogue-sky__map__image {
  height: 50vh;
  position: absolute;
  left: 0;
  right: 0;
  max-width: 700px; /* same as max-width on router-view */
  margin: auto;
}

.rogue-sky__additional-info {
  margin-bottom: 5rem;
}

.person-mountain-moon {
  z-index: -1;
  position: absolute;
  width: 15rem;
  bottom: calc(1rem + 4rem + 5rem);
  /* footer fontsize + footer top padding + footer bottom padding */
}
</style>
