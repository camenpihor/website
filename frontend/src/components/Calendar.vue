<template>
  <div class="calendar">
    <ul v-if="colorKey != null" class="has-text-centered">
      <li
        v-for="(color, key) in colorKey"
        :key="key"
        class="calendar__key__value"
      >
        <span>{{ camelCaseToWords(key) }}: </span
        ><span
          class="calendar__key__color"
          v-bind:style="{ color: color }"
        ></span>
      </li>
    </ul>
    <vc-calendar
      is-expanded
      :min-date="minDate"
      :max-date="maxDate"
      :attributes="attributes"
      timezone="UTC"
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

export default {
  components: {
    PopoverRow,
  },
  props: {
    attributes: {
      type: Array,
    },
    minDate: {
      type: String,
      default: "2020-01-01",
    },
    maxDate: {
      type: String,
      default: "2022-01-01",
    },
    colorKey: {
      type: Object,
      default: null,
    },
    timezone: {
      type: String,
      default: "UTC",
    },
  },
  methods: {
    camelCaseToWords: function(camelCase) {
      return camelCase.replace(/([A-Z])/g, " $1").toLowerCase();
    },
  },
};
</script>

<style>
.calendar__key__value {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
  display: inline-block;
  font-weight: lighter;
  font-size: 0.8rem;
}

.calendar__key__color:before {
  content: "\25AC";
}

.calendar__popover {
  max-width: 10rem;
}

.calendar__popover__extra-info::after {
  font-size: 0.6rem;
}
</style>
