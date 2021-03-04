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
    Navigation,
  },
};
</script>

<style lang="scss">
@import "~bulma/sass/utilities/_all";

// COLORS
$button-over-grey: #979797;
$grey-dark: #5b5b5f;
$off-white: #f0f0f0;
$blue: #3273dc;

$body-background-color: $white-ter;
$body-family: "Noto Sans JP", sans-serif;
$body-color: $grey-dark;

// elements
$footer-background-color: $grey-lighter;
$footer-padding: 4rem 1.5rem 5rem;
$section-padding: 4rem 1.5rem;
$hr-background-color: $button-over-grey;
$hr-height: 1px;
$hr-margin: 1.5rem 20%;
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
    findColorInvert($off-white),
  ),
  "transparent": (
    #00000000,
    #ffffff,
  ),
  "grey-dark": (
    $grey-dark,
    #ffffff,
  ),
  "blue": (
    $blue,
    findColorInvert($blue),
  ),
);

@import "~bulma";
@import "~buefy/src/scss/buefy";

html {
  font-size: 16px;
  @include from($desktop) {
    font-size: 18px;
  }
}

.subsection {
  padding-top: 2rem;
}

#app {
  position: relative;
  min-height: 100vh;
}

.route-view {
  max-width: 750px;
  margin-left: auto;
  margin-right: auto;
  min-height: 90vh;
  padding-top: 3.25rem; /* height of navbar */
  padding-bottom: 8rem;
}

a {
  color: $blue;
}

.non-blue-link {
  color: $grey-dark;
}

.non-blue-link:hover {
  color: $blue;
}

a:hover {
  color: $blue;
}

@media only screen and (max-width: 1024px) {
  // all touch screens
  a {
    color: $blue !important;
  }
}
</style>
