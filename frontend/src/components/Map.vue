<template>
  <Mapbox
    class="map"
    :access-token="this.getToken()"
    :map-options="{
      style: 'mapbox://styles/mapbox/dark-v10',
      center: [longitude, latitude],
      zoom: zoom,
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
    @map-load="onLoad"
  />
</template>

<script>
import Mapbox from "mapbox-gl-vue";

export default {
  components: { Mapbox },
  props: {
    latitude: {
      type: Number,
      default: 37.8
    },
    longitude: {
      type: Number,
      default: -96
    },
    zoom: {
      type: Number,
      default: 2
    },
    onLoad: {
      type: Function,
      default: () => null
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
.map a {
  color: inherit !important;
}
</style>
