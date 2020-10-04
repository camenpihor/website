<template>
  <section class="hero">
    <div
      class="hero-body background__image"
      v-bind:style="{ 'background-image': 'url(' + filePath + ')' }"
    ></div>
  </section>
</template>

<script>
export default {
  props: ["filePath"],
};
</script>

<style>
.background__image {
  background-attachment: fixed;
  background-size: 100vw;
}
</style>
