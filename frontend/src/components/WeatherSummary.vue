<template>
  <div class="weather columns">
    <div class="column">
      <h1 class="has-text-weight-bold">Star Visibility</h1>
      <div class="is-size-7 is-capitalized">{{ starVisibility }}</div>
    </div>
    <div class="column">
      <h1 class="has-text-weight-bold">Precipitation</h1>
      <div class="is-size-7">
        {{ precipitationProbability }}%
        <span v-if="precipitationProbability != 0">{{
          precipitationType
        }}</span>
      </div>
    </div>
    <div class="column">
      <h1 class="has-text-weight-bold">Temperature</h1>
      <div class="is-size-7">
        <ul>
          <li>Low: {{ temperatureLow }}°F</li>
          <li>High: {{ temperatureHigh }}°F</li>
        </ul>
      </div>
    </div>
    <div class="column">
      <h1 class="has-text-weight-bold">Moon Phase</h1>
      <div class="is-size-7">{{ moonPhase }}%</div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    "starVisibility",
    "precipitationProbability",
    "precipitationType",
    "temperatureLow",
    "temperatureHigh",
    "moonPhase"
  ]
};
</script>
