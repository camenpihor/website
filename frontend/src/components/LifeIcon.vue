<template>
  <img v-bind:src="filePath" class="life-icon" />
</template>

<script>
export default {
  props: ["filePath"]
};
</script>

<style>
.life-icon {
  height: 60px;
  width: 60px;
}
</style>
