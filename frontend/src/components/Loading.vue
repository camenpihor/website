<template>
  <div class="loading">
    <b-loading :is-full-page="isFullPage" active />
  </div>
</template>

<script>
export default {
  props: {
    isFullPage: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style></style>
