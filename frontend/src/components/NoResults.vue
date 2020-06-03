<template>
  <div class="no-results">
    <p v-if="message != null" class="no-results__message">
      {{ message }}
    </p>
    <img
      class="no-results__image"
      v-if="Math.random() > 0.5"
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
      personFishingFilePath: require("@/assets/people/person-fishing.svg")
    };
  }
};
</script>

<style>
.no-results {
  margin-top: 2rem;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

.no-results__message {
  font-weight: lighter;
  padding-bottom: 1rem;
}

.no-results__image {
  width: 20rem;
}
</style>
