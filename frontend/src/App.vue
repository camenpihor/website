<template>
  <div id="app">
    <Navigation />
    <router-view id="router-view" />
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

$family-primary: "Helvetica";
$off-white: #f0f0f0;
$menu-item-hover-color: #3273dc;
$menu-item-hover-background-color: transparent;
$input-background-color: #EBEBEB;
$input-border-color: #979797;
$input-focus-border-color: #979797;
$input-hover-border-color: #979797;
$input-focus-box-shadow-size: 0 0 0;
$input-focus-box-shadow-color: #979797;

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
}

#app {
  text-align: center;
}

#router-view {
  min-height: 100vh;
}
</style>
