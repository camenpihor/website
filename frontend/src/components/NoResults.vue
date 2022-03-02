<template>
  <div class="no-results has-text-centered">
    <div v-if="message != null" class="no-results__message has-text-centered">
      {{ message }}
    </div>
    <img
      class="no-results__image"
      v-if="Math.random() < 0.31"
      :src="fishPeopleingFilePath"
    />
    <img class="no-results__image" v-else :src="personFishingFilePath" />
  </div>
</template>

<script>
export default {
  props: ["message"],
  data() {
    return {
      fishPeopleingFilePath: require("@/assets/people/fish-peopleing.svg"),
      personFishingFilePath: require("@/assets/people/person-fishing.svg"),
    };
  },
};
</script>

<style>
.no-results {
  margin-top: 2rem;
  margin-left: auto;
  margin-right: auto;
}

.no-results__message {
  font-weight: lighter;
  padding-bottom: 1rem;
}

.no-results__image {
  width: 20rem;
}
</style>
