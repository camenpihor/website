<template>
  <div class="not-found">
    <p class="not-found__header">404</p>
    <p class="not-found__message">We could not find your request</p>
    <p v-if="requestedPath !== ''" class="not-found__requested-url">
      {{ createUrl() }}
    </p>
    <img
      class="not-found__image"
      v-if="Math.random() > 0.5"
      :src="fishPeopleingFilePath"
    />
    <img class="not-found__image" v-else :src="personFishingFilePath" />
  </div>
</template>

<script>
export default {
  props: {
    requestedPath: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      fishPeopleingFilePath: require("@/assets/people/fish-peopleing.svg"),
      personFishingFilePath: require("@/assets/people/person-fishing.svg")
    };
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

.not-found__image {
  margin-top: 8rem;
  width: 20rem;
}
</style>
