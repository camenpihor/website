<template>
  <div id="app">
    <router-view id="router-view" />
  </div>
</template>

<script>
export default {
  name: "app"
};
</script>

<style>
#app {
  text-align: center;
}

#router-view {
  min-height: 105vh;
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
