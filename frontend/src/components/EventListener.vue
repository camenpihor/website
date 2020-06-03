<template>
  <div class="event-listener"></div>
</template>

<script>
export default {
  props: {
    method: {
      type: Function
    }
  },
  created() {
    window.addEventListener("keyup", this.method);
  },
  beforeDestroy() {
    window.removeEventListener("keyup", this.method);
  }
};
</script>

<style>
.event-listener {
  display: none;
}
</style>
