<template>
  <div class="weather columns is-mobile">
    <div class="column">
      <h1 class="weather__title">Star Visibility</h1>
      <div class="weather__value">{{ starVisibility }}%</div>
    </div>
    <div class="column">
      <h1 class="weather__title">Precipitation</h1>
      <div class="weather__value">
        {{ precipitationProbability }}%
        <span v-if="precipitationProbability != 0">{{
          precipitationType
        }}</span>
      </div>
    </div>
    <div class="column">
      <h1 class="weather__title">Temperature</h1>
      <div class="weather__value">
        <ul>
          <li>Low: {{ temperatureLow }}°F</li>
          <li>High: {{ temperatureHigh }}°F</li>
        </ul>
      </div>
    </div>
    <div class="column">
      <h1 class="weather__title">Moon Phase</h1>
      <div class="weather__value">{{ moonPhase }}%</div>
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

<style>
.weather__title {
  font-weight: bold;
}

.weather__value {
  font-weight: lighter;
}
</style>
