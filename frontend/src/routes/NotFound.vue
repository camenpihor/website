<template>
  <div class="not-found">
    <p class="not-found__header">404</p>
    <p class="not-found__message">We could not find your request</p>
    <p v-if="requestedPath !== ''" class="not-found__requested-url">
      {{ createUrl() }}
    </p>
    <img class="not-found__image" :src="chooseImage()" />
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
    chooseImage: function() {
      let filepaths = [this.fishPeopleingFilePath, this.personFishingFilePath];
      let randomIdx = Math.floor(Math.random() * filepaths.length);
      return filepaths[randomIdx];
    },
    createUrl: function() {
      return window.location.origin + this.requestedPath;
    }
  }
};
</script>

<style>
.not-found {
  margin-top: 60px;
}

.not-found__header {
  font-weight: bold;
  font-size: 1.875rem;
  color: black;
}

.not-found__message {
  margin-top: 20px;
  font-weight: lighter;
}

.not-found__requested-url {
  font-weight: lighter;
}

.not-found__image {
  margin-top: 55px;
  width: 18rem;
  height: 9rem;
}
</style>
