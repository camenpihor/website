<template>
  <div class="no-results">
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
  data() {
    return {
      fishPeopleingFilePath: require("@/assets/people/fish-peopleing.svg"),
      personFishingFilePath: require("@/assets/people/person-fishing.svg")
    };
  }
};
</script>

<style>
.no-results__image {
  margin-left: auto;
  margin-right: auto;
  width: 20rem;
}
</style>
