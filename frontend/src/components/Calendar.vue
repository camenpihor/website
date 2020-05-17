<template>
  <div class="calendar">
    <ul class="calendar__key">
      <li
        v-for="(color, key) in colors"
        :key="key"
        class="calendar__key__value"
      >
        <span>{{ camelCaseToWords(key) }}: </span
        ><span
          class="calendar__key__circle"
          v-bind:style="{ color: color }"
        ></span>
      </li>
    </ul>
    <vc-calendar
      is-expanded
      min-date="2020-01-02"
      max-date="2021-01-01"
      :attributes="attributes"
    >
      <div
        class="calendar__popover"
        slot="day-popover"
        slot-scope="{ day, dayTitle, attributes }"
      >
        <div class="calendar__popover__date">
          {{ dayTitle }}
        </div>
        <PopoverRow
          v-for="attr in attributes"
          :key="attr.key"
          :attribute="attr"
        >
          <div>
            <b-tooltip
              v-if="attr.customData.info != null"
              class="calendar__popover__extra-info"
              :label="attr.customData.info"
              type="is-blue"
              position="is-bottom"
              size="is-small"
              multilined
            >
              <i class="fal fa-info-circle" style="cursor:pointer;" />
            </b-tooltip>
            {{ attr.customData.event }}
          </div>
        </PopoverRow>
      </div>
    </vc-calendar>
  </div>
</template>

<script>
import PopoverRow from "v-calendar/lib/components/popover-row.umd.min";

import astronomicalJson from "@/assets/astronomical_events.json";

export default {
  components: {
    PopoverRow
  },
  data() {
    return {
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

      var blah = [today, bestDay];
      for (const [label, data] of Object.entries(astronomicalJson)) {
        blah = blah.concat([
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
      return blah;
    }
  },
  methods: {
    camelCaseToWords: function(camelCase) {
      return camelCase.replace(/([A-Z])/g, " $1").toLowerCase();
    }
  }
};
</script>

<style>
.calendar__key__value {
  padding: 0.5rem;
  display: inline-block;
}

.calendar__key__circle:before {
  content: " \25CF";
  font-size: 1rem;
}

.calendar__popover {
  max-width: 10rem;
}

.calendar__popover__extra-info::after {
  font-size: 0.6rem;
}
</style>
