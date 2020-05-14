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
  padding-bottom: 6.25rem;
}

.recommendations__search {
  margin-left: auto;
  margin-right: auto;
}

.recommendations__groups {
  margin-top: 4rem;
}

.recommendation__group {
  margin-top: 2rem;
}

.recommendation__group__header {
  font-size: 1.5rem;
  font-weight: bold;
}

.recommendation__group__item {
  margin-left: 1rem;
}

.recommendation__group__item a:hover {
  color: #3273dc;
}

.recommendation__group__item__label {
  text-indent: -1rem;
  padding-left: 1rem;
}

.person-hanging {
  position: relative;
  top: -10px;
  float: right;
  left: -9rem;
}

.person-computer {
  margin-left: -1rem;
}
</style>
