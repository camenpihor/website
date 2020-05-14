<template>
  <div class="recommendations">
    <SearchBar
      class="recommendations__search"
      placeholder="'type: book' or 'topic: nature'"
    />
    <img class="person-hanging" :src="personHangingFilePath" />
    <div class="recommendations__groups">
      <ul
        class="recommendation__group"
        v-for="(groupData, groupLabel, index) in recommendations"
        :key="groupLabel"
      >
        <p class="recommendation__group__header">
          <img
            v-if="index === 2"
            class="person-computer"
            :src="personComputerFilePath"
          />{{ groupLabel }}
        </p>
        <li
          class="recommendation__group__item"
          v-for="item in groupData"
          :key="item.label"
        >
          <p class="recommendation__group__item__label">
            <a :href="item.url">
              <span>{{ item.label }}</span
              ><span v-if="item.group_label !== null">
                by {{ item.group_label }}</span
              >
            </a>
          </p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";
import recommendationJson from "@/assets/recommendations.json";

export default {
  components: {
    SearchBar
  },
  data() {
    return {
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      recommendations: recommendationJson
    };
  }
};
</script>

<style>
.recommendations {
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  margin-top: 20px;
  margin-bottom: 60px;
}

.recommendations__search {
  margin-left: auto;
  margin-right: auto;
}

.person-hanging {
  position: relative;
  top: -12px;
  left: 150px;
}

.recommendation__group:first-of-type {
  margin-top: 20px;
}

.recommendations__groups {
  margin-left: 20px;
  margin-right: 20px;
  text-align: left;
}

.recommendation__group {
  margin-top: 30px;
}

.recommendation__group__header {
  font-size: 1.5rem;
  font-weight: bold;
}

.recommendation__group__item {
  margin-left: 20px;
}

.recommendation__group__item a:hover {
  color: #3273dc;
}

.recommendation__group__item__label {
  text-indent: -20px;
  padding-left: 20px;
}

.person-computer {
  margin-left: -1rem;
}
</style>
