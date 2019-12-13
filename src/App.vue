<template>
  <div id="app">
    <Navigation />
    <router-view id="page-container" />
    <Footer />
  </div>
</template>

<script>
import Navigation from "./components/Navigation.vue";
import Footer from "./components/Footer.vue";

export default {
  name: "app",
  components: {
    Navigation,
    Footer
  }
};
</script>

<style>
#app {
  text-align: center;
}
#page-container {
  min-height: 100vh;
  margin-bottom: 50px;
}
</style>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

$gap: 200px;
$family-primary: "Open Sans";
$primary: #057715;
$primary-invert: findColorInvert($primary);

$colors: (
  "primary": (
    $primary,
    $primary-invert
  )
);

$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
