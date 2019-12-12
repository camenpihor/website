<template>
  <div>
    <Search/>
  </div>
</template>

<script>
import Search from "@/components/rogue_sky/Search.vue"

export default {
  name: "rogue_sky",
  components: {
    Search
  },
  methods: {
    toDefaultForecast() {
      // seattle
      var startLat = 47.687;
      var startLon = -122.377;
      this.$router.push(`/rogue-sky/${startLat}/${startLon}`);
    }
  },
  mounted() {
    this.toDefaultForecast();
  }
};
</script>
