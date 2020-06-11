<template>
  <div class="weather columns">
    <div class="column">
      <h1 class="has-text-weight-bold">Star Visibility</h1>
      <div class="is-size-7 is-capitalized">{{ starVisibility }}</div>
    </div>
    <div class="column">
      <h1 class="has-text-weight-bold">Precipitation</h1>
      <div class="is-size-7">
        {{ precipitationSummary }}
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
      <h1 class="has-text-weight-bold">Moon</h1>
      <div class="is-size-7">{{ moonIllumination }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    "starVisibility",
    "precipitationSummary",
    "temperatureLow",
    "temperatureHigh",
    "moonIllumination"
  ]
};
</script>
