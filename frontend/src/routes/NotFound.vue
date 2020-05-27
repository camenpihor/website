<template>
  <div class="not-found">
    <p class="not-found__header">404</p>
    <p class="not-found__message">We could not find your request</p>
    <p v-if="requestedPath !== ''" class="not-found__requested-url">
      {{ createUrl() }}
    </p>
    <NoResults />
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
  },
  methods: {
    createUrl: function() {
      return window.location.origin + this.requestedPath;
    }
  }
};
</script>

<style>
.not-found {
  text-align: center;
}

.not-found__header {
  font-weight: bold;
  font-size: 2rem;
  color: black;
}

.not-found__message {
  margin-top: 1rem;
  font-weight: lighter;
}

.not-found__requested-url {
  font-weight: lighter;
}

.no-results {
  margin-top: 8rem;
}
</style>
