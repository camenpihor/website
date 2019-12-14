<template>
  <section id="forecast-search">
    <div id="forecast-search-container" class="container">
      <b-input
        id="forecast-search-input"
        @click.native="clearInput"
        @blur="defaultInput"
        @keyup.native.enter="search"
        v-model="input"
        rounded
        placeholder="Seattle, WA"
      ></b-input>
    </div>
  </section>
</template>

<script>
import { getCoordinates } from "@/api.js";

export default {
  name: "search",
  props: ["value"],
  data() {
    return {
      input: this.value
    };
  },
  methods: {
    search() {
      this.$parent.star_forecast = null;
      getCoordinates(this.input).then(response => {
        let latitude = response.data.latitude.toFixed(3);
        let longitude = response.data.longitude.toFixed(3);
        this.$router.push(`/rogue-sky/${latitude}/${longitude}`);
      });
    },
    clearInput() {
      this.input = null;
    },
    defaultInput() {
      this.input = this.value;
    }
  },
  watch: {
    value() {
      this.input = this.value;
    }
  }
};
</script>

<style>
#forecast-search {
  padding-top: 10px;
  padding-bottom: 10px;
  background-color: #6b606013;
}

#forecast-search-container {
  max-width: 400px;
}

#forecast-search-input {
  text-align: center;
  font-weight: bold;
}
</style>
