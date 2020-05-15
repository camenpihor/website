<template>
  <div id="app">
    <Navigation />
    <router-view class="route-view" />
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/Footer.vue";
import Navigation from "@/components/Navigation.vue";

export default {
  name: "app",
  components: {
    Footer,
    Navigation
  }
};
</script>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

$off-white: #f0f0f0;
$blue: #3273dc;
$green: rgb(0, 117, 0);
$button-over-grey: #979797;

// buefy and bulma variables
$family-primary: "Helvetica";
$menu-item-hover-color: $blue;
$menu-item-hover-background-color: transparent;
$input-background-color: #ebebeb;
$input-border-color: $button-over-grey;
$input-focus-border-color: $button-over-grey;
$input-hover-border-color: $button-over-grey;
$input-focus-box-shadow-size: 0 0 0;
$input-focus-box-shadow-color: $button-over-grey;

$colors: (
  "off-white": (
    $off-white,
    findColorInvert($off-white)
  ),
  "transparent": (
    #f0f0f000,
    #000000
  )
);

@import "~bulma";
@import "~buefy/src/scss/buefy";

html {
  font-size: 16px;
  @include from($desktop) {
    font-size: 20px;
  }
}

a {
  color: inherit;
}

a:hover {
  -webkit-tap-highlight-color: transparent;
  color: $blue;
}

#app {
  position: relative;
  min-height: 100vh;
}

.route-view {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 2rem;
  padding-right: 2rem;
  padding-top: 2.5rem;
  padding-bottom: 10rem;
}

@media only screen and (max-width: 1023px) {
  // all touch screens
  a {
    // color: $green !important;
    // color: $blue !important;
    color: #7957d5 !important;
  }
}
</style>
