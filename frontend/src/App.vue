<template>
  <div id="app">
    <NavBar />
    <router-view id="router-view" />
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import NavBar from "@/components/NavBar.vue";

export default {
  name: "app",
  components: {
    Footer,
    NavBar
  }
};
</script>

<style>
body {
  font-family: "Helvetica" !important;
}

#app {
  text-align: center;
}

#router-view {
  min-height: 100vh;
}
</style>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

$off-white: #f0f0f0;

$colors: (
  "off-white": (
    $off-white,
    findColorInvert($off-white)
  )
);

@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
