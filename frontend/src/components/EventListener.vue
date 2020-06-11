<template>
  <div class="event-listener"></div>
</template>

<script>
export default {
  props: {
    method: {
      type: Function
    },
    eventType: {
      type: String,
      default: "keyup"
    }
  },
  created() {
    window.addEventListener(this.eventType, this.method);
  },
  beforeDestroy() {
    window.removeEventListener(this.eventType, this.method);
  }
};
</script>

<style>
.event-listener {
  display: none;
}
</style>
