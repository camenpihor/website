<template>
  <div id="app">
    <Navigation/>
    <router-view id="page-container"/>
    <Footer/>
  </div>
</template>

<script>
import Navigation from "./components/Navigation.vue";
import Footer from "./components/Footer.vue"

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
}
</style>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

$gap: 200px;
$family-primary: "Roboto";
$primary: #00660e;
$primary-invert: findColorInvert($primary);

$colors: (
    "white": ($white, $black),
    "black": ($black, $white),
    "light": ($light, $light-invert),
    "dark": ($dark, $dark-invert),
    "primary": ($primary, $primary-invert),
    "info": ($info, $info-invert),
    "success": ($success, $success-invert),
    "warning": ($warning, $warning-invert),
    "danger": ($danger, $danger-invert),
);

$link: $primary;
$link-invert: $primary-invert;
$link-focus-border: $primary;

@import "~bulma";
@import "~buefy/src/scss/buefy";
</style>
