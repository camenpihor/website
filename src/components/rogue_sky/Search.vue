<template>
  <section id="forecast-search">
    <b-input
      class="container"
      @keyup.native.enter="search"
      v-model="input"
      rounded
      icon="search"
      icon-clickable
      @icon-click="search"
      placeholder="Seattle, WA"
    ></b-input>
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
  }
};
</script>

<style>
#forecast-search {
  padding-top: 10px;
  padding-bottom: 10px;
  background-color: #3c3f7d;
}

#forecast-search .input {
  text-align: center;
  font-weight: bold;
}
</style>
