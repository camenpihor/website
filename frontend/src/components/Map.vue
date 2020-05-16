<template>
  <Mapbox
    access-token="pk.eyJ1IjoiY2FtZW5waWhvciIsImEiOiJjazlpem43N2swMmUyM2RtcGo2Nmo1c25qIn0.xG-XxGg8DLWESXnlwhUBdw"
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
  }
};
</script>

<style>
</style>
