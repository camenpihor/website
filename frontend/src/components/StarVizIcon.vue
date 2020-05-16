<template>
  <div class="star-viz">
    <i class="star-viz__icon" v-bind:class="wordToIconClass()" />
    <div class="star-viz__date">{{ date }}</div>
  </div>
</template>

<script>
export default {
  props: ["word", "date"],
  methods: {
    wordToIconClass: function() {
      let cantFind = "fal fa-space-station-moon-alt";
      let lookup = {
        best: "fas fa-moon-stars",
        clear: "fas fa-moon",
        cloudy: "fas fa-moon-cloud",
        "very-cloudy": "fas fa-clouds-moon",
        rain: "fas fa-cloud-moon-rain"
      };
      if (this.word in lookup) {
        return lookup[this.word];
      } else {
        return cantFind;
      }
    }
  }
};
</script>

<style>
.star-viz {
  text-align: center;
}
</style>
