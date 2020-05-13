<template>
  <div class="recommendations">
    <SearchBar placeholder="'type: book' or 'topic: nature'" />
    <img class="person-hanging" :src="personHangingFilePath" />
    <div class="recommendations__groups"></div>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";

export default {
  components: {
    SearchBar
  },
  data() {
    return {
      personHangingFilePath: require("@/assets/person-hanging.svg")
    };
  }
};
</script>

<style>
.recommendations {
  margin-top: 20px;
}

.person-hanging {
  position: relative;
  top: -12px;
  left: 150px;
}
</style>
