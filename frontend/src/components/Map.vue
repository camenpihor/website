<template>
  <MglMap
    class="map"
    :access-token="this.getToken()"
    mapStyle="mapbox://styles/mapbox/dark-v10"
    :minZoom="2"
    :center="[longitude, latitude]"
    :zoom="zoom"
    logoPosition="bottom-right"
    :boxZoom="false"
    :scrollZoom="false"
    :dragRotate="false"
    :keyboard="false"
    :touchZoomRotate="false"
    @load="onLoad"
  >
    <MglNavigationControl position="top-right" :showCompass="false" />
  </MglMap>
</template>

<script>
import Mapbox from "mapbox-gl";
import { MglMap, MglNavigationControl } from "vue-mapbox";

export default {
  components: { MglMap, MglNavigationControl },
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
  },
  created() {
    // We need to set mapbox-gl library here in order to use it in template
    this.mapbox = Mapbox;
  }
};
</script>

<style>
.map a {
  color: inherit !important;
}
</style>
