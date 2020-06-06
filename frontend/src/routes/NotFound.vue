<template>
  <div class="section has-text-centered">
    <p class="title is-3">404</p>
    <p class="subtitle is-5">We could not find your request</p>
    <NoResults class="subsection" />
  </div>
</template>

<script>
import NoResults from "@/components/NoResults.vue";

export default {
  components: {
    NoResults
  },
  props: {
    requestedPath: {
      type: String,
      default: ""
    }
  }
};
</script>

<style>
.not-found {
  text-align: center;
}
</style>
