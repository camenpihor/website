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
        this.$router.push(
          `/rogue-sky/${pos.coords.latitude}/${pos.coords.longitude}`
        )
      })
    }
  },
  mounted() {
    this.getUserLocation();
  }
};
</script>
