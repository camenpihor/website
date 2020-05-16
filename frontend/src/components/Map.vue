<template>
  <Mapbox
    :access-token="this.getToken()"
    :map-options="{
      style: 'mapbox://styles/mapbox/dark-v10',
      center: [lat, lon],
      zoom: 2,
      dragRotate: false
    }"
    :geolocate-control="{
      show: true,
      position: 'top-right'
    }"
    :fullscreen-control="{
      show: true,
      position: 'top-right'
    }"
    :nav-control="{
      show: false
    }"
  />
</template>

<script>
import Mapbox from "mapbox-gl-vue";

export default {
  components: { Mapbox },
  props: {
    lat: {
      type: Number,
      default: -96
    },
    lon: {
      type: Number,
      default: 37.8
    }
  },
  methods: {
    getToken: function() {
      return process.env.VUE_APP_MAPBOX_SECRET_TOKEN;
    }
  }
};
</script>

<style>
</style>
