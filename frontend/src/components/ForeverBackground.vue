<template>
  <div
    class="image"
    v-bind:style="{ 'background-image': 'url(' + filePath + ')' }"
  />
</template>

<script>
export default {
  props: ["filePath"]
};
</script>

<style>
.image {
  background-position: center center;
  background-repeat: repeat;
  background-attachment: fixed;
  background-size: cover;
  height: 100vh;
}
</style>
