<template>
  <section>
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
            class="level-item has-text-centered is-size-7 star-viz-icon"
            v-for="(star, idx) in starForecast"
            :key="star.weather_date_local"
            :word="star.icon"
            :date="humanizeDate(star.weather_date_local)"
            v-on:click.native="focusWeather(idx)"
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
        <h1 class="title is-3 has-text-centered">
          Best
          <img class="person-wave-move-image" :src="personWaveMoveFilePath" />
        </h1>
        <div class="is-hidden-touch">
          <div>
            <h1 class="heading is-size-7">Today</h1>
            <p class="heading is-size-9">
              {{ today.weather_date_local }}
            </p>
            <WeatherSummary
              :starVisibility="humanizeStarVisibility(today.star_visibility)"
              :precipitationSummary="
                humanizePrecipitation(
                  today.precip_type,
                  today.precip_intensity_max_in_hr,
                  today.precip_probability
                )
              "
              :temperatureLow="Math.round(today.temperature_min_f)"
              :temperatureHigh="Math.round(today.temperature_max_f)"
              :moonIllumination="floatToPercent(today.moon_illumination)"
            />
          </div>
          <div class="subsection">
            <div>
              <p class="heading is-size-7">Best</p>
              <p
                v-if="bestDay.weather_date_local != today.weather_date_local"
                class="heading is-size-9"
              >
                {{ printDate(bestDay.weather_date_local) }}
              </p>
              <p v-else class="heading is-size-9">
                Today
              </p>
            </div>
            <WeatherSummary
              v-if="bestDay.weather_date_local != today.weather_date_local"
              :starVisibility="humanizeStarVisibility(bestDay.star_visibility)"
              :precipitationSummary="
                humanizePrecipitation(
                  bestDay.precip_type,
                  bestDay.precip_intensity_max_in_hr,
                  bestDay.precip_probability
                )
              "
              :temperatureLow="Math.round(bestDay.temperature_min_f)"
              :temperatureHigh="Math.round(bestDay.temperature_max_f)"
              :moonIllumination="floatToPercent(bestDay.moon_illumination)"
            />
          </div>
        </div>
        <div
          class="columns is-mobile is-hidden-desktop subsection"
          style="margin-left:auto"
        >
          <div class="column">
            <div>
              <h1 class="heading is-size-7">Today</h1>
              <p class="heading is-size-9">
                {{ printDate(today.weather_date_local) }}
              </p>
            </div>
            <WeatherSummary
              :starVisibility="humanizeStarVisibility(today.star_visibility)"
              :precipitationSummary="
                humanizePrecipitation(
                  today.precip_type,
                  today.precip_intensity_max_in_hr,
                  today.precip_probability,
                  true
                )
              "
              :temperatureLow="Math.round(today.temperature_min_f)"
              :temperatureHigh="Math.round(today.temperature_max_f)"
              :moonIllumination="floatToPercent(today.moon_illumination)"
            />
          </div>
          <div class="column">
            <div>
              <p class="heading is-size-7">Suggested</p>
              <p
                v-if="bestDay.weather_date_local != today.weather_date_local"
                class="heading is-size-9"
              >
                {{ printDate(bestDay.weather_date_local) }}
              </p>
              <p v-else class="heading is-size-9">
                Today
              </p>
            </div>
            <WeatherSummary
              v-if="bestDay.weather_date_local != today.weather_date_local"
              :starVisibility="humanizeStarVisibility(bestDay.star_visibility)"
              :precipitationSummary="
                humanizePrecipitation(
                  bestDay.precip_type,
                  bestDay.precip_intensity_max_in_hr,
                  bestDay.precip_probabilitym,
                  true
                )
              "
              :temperatureLow="Math.round(bestDay.temperature_min_f)"
              :temperatureHigh="Math.round(bestDay.temperature_max_f)"
              :moonIllumination="floatToPercent(bestDay.moon_illumination)"
            />
          </div>
        </div>
      </div>

      <div class="section" ref="weather">
        <p class="title is-3 has-text-centered">Weather</p>
        <p class="subtitle is-7 has-text-centered">
          daily weather summaries
        </p>
        <b-tabs position="is-centered" v-model="weatherIdx" expanded>
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
              {{ printDate(dailyWeather.weather_date_local) }}
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
                <span class="column">{{ dailyWeather.sunset_time_local }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold	"
                  >Moon Rise</span
                >
                <span class="column">{{
                  dailyWeather.moonrise_time_local
                }}</span>
              </div>
              <div class="columns is-mobile rogue-sky__weather__item">
                <span class="column is-4-desktop has-text-weight-semibold">
                  <span class="is-hidden-touch">Moon Illumination</span>
                  <span class="is-hidden-desktop">Moon Fullness</span>
                </span>
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
import Map from "@/components/Map.vue";
import NotFound from "@/routes/NotFound.vue";
import StarVizIcon from "@/components/StarVizIcon.vue";
import WeatherSummary from "@/components/WeatherSummary.vue";

import { format, parseISO } from "date-fns";

import {
  getAstronomicalEvents,
  getCoordinates,
  getStarForecast
} from "@/assets/js/api.js";

export default {
  components: {
    BackendSearch,
    Calendar,
    Map,
    NotFound,
    StarVizIcon,
    WeatherSummary
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
      astronomicalEvents: null,
      timezone: null,
      city: null,
      state: null,
      latitude: null,
      longitude: null,
      weatherIdx: 0,
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
        this.fetchAstronomicalEvents();
      } else {
        let seattle_lat = 47.687;
        let seattle_lon = -122.377;
        this.$router.replace({
          name: "rogue-sky-location",
          params: { latitude: seattle_lat, longitude: seattle_lon }
        });
      }
    },
    fetchAstronomicalEvents: function() {
      getAstronomicalEvents()
        .then(response => {
          this.astronomicalEvents = response.data;
        })
        .catch(() => {
          this.error = true;
        });
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
    humanizePrecipitation: function(type, intensity, probability, summarize) {
      if (probability <= 0.01 || type == null || probability == null) {
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

      if (summarize) {
        return `${percent} chance of ${type}`;
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
    printDate: function(date) {
      return format(parseISO(date), "eeee, MMMM do yyyy");
    },
    humanizeDate: function(date) {
      return format(parseISO(date), "eee");
    },
    focusWeather: function(idx) {
      this.weatherIdx = idx;
      let weatherSection = this.$refs.weather;
      window.scrollTo({
        top: weatherSection.offsetTop,
        behavior: "smooth"
      });
    },
    cloudCoverLayer: function(event) {
      let map = event.map;

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
      if ((this.starForecast != null) & (this.astronomicalEvents != null)) {
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
        allEvents = allEvents.concat([
          ...this.astronomicalEvents.map(event => ({
            dates: event.date,
            bar: this.calendarColors[event.type],
            popover: {
              label: event.event,
              placement: "auto",
              isInteractive: true
            },
            customData: event
          }))
        ]);
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

.star-viz-icon {
  cursor: pointer;
}

.star-viz-icon:hover {
  color: #3273dc;
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
  max-width: 1000px;
  margin: auto;
}

.vc-container {
  --day-content-height: 2rem;
}

.rogue-sky__additional-info {
  margin-bottom: 5rem;
}

.tabs a {
  color: inherit !important;
}

.person-mountain-moon {
  z-index: -1;
  position: absolute;
  width: 15rem;
  bottom: calc(1rem + 4rem + 5rem);
  /* footer fontsize + footer top padding + footer bottom padding */
}
</style>
