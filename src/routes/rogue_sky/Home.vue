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
      navigator.geolocation.getCurrentPosition(pos => {
        let latitude = pos.coords.latitude
        let longitude = pos.coords.longitude
        this.$router.push(`/rogue-sky/${latitude}/${longitude}`)
      })
    }
  },
  mounted() {
    this.getUserLocation();
  }
};
</script>
