<template>
  <div
    class="has-background-image"
    v-bind:style="{ 'background-image': 'url(' + filePath + ')' }"
  />
</template>

<script>
export default {
  props: ["filePath"]
};
</script>

<style>
.has-background-image {
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
</style>
