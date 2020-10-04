<template>
  <div>
    <div>
      <i v-bind:class="wordToIconClass()" />
      <p>{{ date }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["word", "date"],
  methods: {
    wordToIconClass: function() {
      let cantFind = "fas fa-monkey";
      let lookup = {
        best: "fas fa-moon-stars",
        "clear-day": "fas fa-moon",
        "clear-night": "fas fa-moon",
        cloudy: "fas fa-cloud",
        "very-cloudy": "fas fa-clouds",
        rain: "fas fa-cloud-rain",
        snow: "fas fa-cloud-snow",
        sleet: "fas fa-cloud-sleet",
        fog: "fas fa-clouds",
        "partly-cloudy-day": "fas fa-moon-cloud",
        "partly-cloudy-night": "fas fa-moon-cloud",
      };
      if (this.word in lookup) {
        return lookup[this.word];
      } else {
        return cantFind;
      }
    },
  },
};
</script>

<style></style>
