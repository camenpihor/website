<template>
  <section id="forecast-search">
    <div id="forecast-search-container" class="container">
      <b-input
        id="forecast-search-input"
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
      getCoordinates(this.input).then(response => {
        this.$router.push(
          `/rogue-sky/${response.data.latitude}/${response.data.longitude}`
        );
      });
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
