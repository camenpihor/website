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
    getUserLocation() {
      var startLat = 47.687;
      var startLon = -122.377;
      let geoOptions = {
          timeout: 5 * 1000, maximumAge: 5 * 60 * 1000
      };

      var geoSuccess = function(position) {
        let latitude = position.coords.latitude;
        let longitude = position.coords.longitude;
        this.$router.push(`/rogue-sky/${latitude}/${longitude}`);
      };
  
      var geoError = function(error) {
        if (error.code !== 0) {
          this.$router.push(`/rogue-sky/${startLat}/${startLon}`);
        }
        else {
          this.$router.push({ name: "404"});
        }
      };

      navigator.geolocation.getCurrentPosition(geoSuccess, geoError, geoOptions);
    }
  },
  mounted() {
    this.getUserLocation();
  }
};
</script>
