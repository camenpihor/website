<template>
  <div class="rogue-sky">
    <SearchBar class="rogue-sky__search" placeholder="Boston, MA" />
    <div class="rogue-sky__results">
      <div class="rogue-sky__location rogue-sky__section">
        <div class="rogue-sky__week columns is-mobile">
          <StarVizIcon class="column" word="clear" date="May 8" />
          <StarVizIcon class="column" word="cloudy" date="May 9" />
          <StarVizIcon class="column" word="very-cloudy" date="May 10" />
          <StarVizIcon class="column" word="rain" date="May 11" />
          <StarVizIcon class="column" word="best" date="May 12" />
          <StarVizIcon class="column" word="cloudy" date="May 13" />
          <StarVizIcon class="column" word="rain" date="May 14" />
          <StarVizIcon class="column" word="clear" date="May 15" />
        </div>
      </div>

      <div class="rogue-sky__day__today rogue-sky__section">
        <h1 class="rogue-sky__header">Today</h1>
        <WeatherSummary
          class="rogue-sky__weather"
          starVisibility="62"
          precipitationAmount="3"
          precipitationType="heavy rain"
          temperatureLow="52"
          temperatureHigh="78"
          moonPhase="83"
        />
      </div>
      <div class="rogue-sky__day__best rogue-sky__section">
        <div class="rogue-sky__header">
          <p>Best of Week</p>
          <p class="rogue-sky__header__subtext">(Wednesday May 12)</p>
        </div>
        <WeatherSummary
          class="rogue-sky__weather"
          starVisibility="94"
          precipitationAmount="0"
          precipitationType="rain"
          temperatureLow="60"
          temperatureHigh="75"
          moonPhase="100"
        />
      </div>

      <div class="rogue-sky__map rogue-sky__section">
        <h1 class="rogue-sky__header">Map</h1>
        <div class="rogue-sky__map__wrapper">
          <Map class="rogue-sky__map__image" />
        </div>
      </div>

      <div class="rogue-sky__month rogue-sky__section">
        <h1 class="rogue-sky__header">Month</h1>
        <div class="rogue-sky__calendar__wrapper">
          <Calendar
            class="rogue-sky__calendar"
            :attributes="attributes"
            minDate="2020-01-02"
            maxDate="2021-01-01"
            :colorKey="colors"
          />
        </div>
      </div>

      <div class="rogue-sky__addition-info rogue-sky__section">
        <h1 class="rogue-sky__header">Additional Information</h1>
        <ul>
          <li>
            <a href="https://www.camenpiho.com/rogue-sky/documentation"
              >www.camenpiho.com/rogue-sky/documentation</a
            >
          </li>
          <li>
            <a href="https://www.darksky.net/forecast/40.7127,-74.0059"
              >www.darksky.net/forecast/40.7127,-74.0059</a
            >
          </li>
          <li>
            <a href="https://www.darksitefinder.com/maps/world.html"
              >www.darksitefinder.com/maps/world.html</a
            >
          </li>
          <li>
            <a href="https://www.darksky.org">www.darksky.org</a>
          </li>
          <li>
            <a href="https://www.starwalk.space">www.starwalk.space</a>
          </li>
        </ul>
      </div>
      <img class="person-mountain-moon" :src="personMountainMoonFilePath" />
    </div>
  </div>
</template>

<script>
import Calendar from "@/components/Calendar.vue";
import Map from "@/components/Map.vue";
import SearchBar from "@/components/SearchBar.vue";
import StarVizIcon from "@/components/StarVizIcon.vue";
import WeatherSummary from "@/components/WeatherSummary.vue";

import astronomicalJson from "@/assets/astronomical_events.json";

export default {
  components: {
    Calendar,
    Map,
    SearchBar,
    StarVizIcon,
    WeatherSummary
  },
  data() {
    return {
      personMountainMoonFilePath: require("@/assets/people/person-mountain-moon.svg"),
      colors: {
        moon: "green",
        eclipse: "gray",
        planetary: "red",
        meteorShower: "purple",
        other: "blue"
      },
      bestDay: {
        date: "2020-05-18",
        starVisibility: 78,
        event: "Best day of star visibility this week (78%)"
      }
    };
  },
  computed: {
    attributes() {
      let today = {
        key: "today",
        highlight: "blue",
        dates: new Date(),
        popover: {
          label: "Today",
          placement: "auto"
        },
        customData: { event: "Today" }
      };

      let bestDay = {
        key: "bestDay",
        highlight: { color: "yellow" },
        dates: this.bestDay.date,
        popover: {
          label: this.bestDay.event,
          placement: "auto"
        },
        customData: this.bestDay
      };

      var allEvents = [today, bestDay];
      for (const [label, data] of Object.entries(astronomicalJson)) {
        allEvents = allEvents.concat([
          ...data.map(datum => ({
            dates: datum.date,
            bar: this.colors[label],
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
  }
};
</script>

<style>
.rogue-sky {
  padding-bottom: 20rem;
}

.rogue-sky__search {
  margin-left: auto;
  margin-right: auto;
}

.rogue-sky__section {
  margin-top: 4rem;
  margin-bottom: 4rem;
}

.rogue-sky__section:first-of-type {
  margin-top: 2.5rem;
}

.rogue-sky__section:last-of-type {
  margin-bottom: 0;
}

.rogue-sky__header {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-align: left;
}

.rogue-sky__header__subtext {
  font-size: 0.7rem;
  font-weight: lighter;
  margin-top: -0.5rem;
}

.rogue-sky__week {
  margin-left: -2rem; /* same as padding-left on router-view */
  margin-right: -2rem; /* same as padding-right on router-view */
}

.rogue-sky__weather {
  margin-left: -2rem; /* same as padding-left on router-view */
  margin-right: -2rem; /* same as padding-right on router-view */
}

.rogue-sky__weather {
  font-size: 0.9rem;
}

.rogue-sky__week {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
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

.rogue-sky__calendar__wrapper {
  margin-left: -2rem; /* same as padding-left on router-view */
  margin-right: -2rem; /* same as padding-right on router-view */
}

.person-mountain-moon {
  position: absolute;
  width: 15rem;
  bottom: 2.3rem; /* height of footer - a smidgeon */
  left: 15vw;
  z-index: -1;
}
</style>
