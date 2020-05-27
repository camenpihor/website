<template>
  <div>
    <div v-if="recommendations != null" class="recommendations">
      <ClientSideSearch
        class="recommendations__search"
        :keys="searchKeys"
        :json="recommendations"
        :jsonUUID="searchUUID"
        :imageFilePath="personHangingFilePath"
        v-on:output="searchResults = $event"
      />

      <div v-if="searchResults.length > 0" class="recommendations__groups">
        <ul
          class="recommendation__group"
          v-for="(groupData, groupLabel, index) in groupedRecommendations"
          :key="groupLabel"
        >
          <p class="recommendation__group__header">
            <img
              v-if="index === 1"
              class="person-computer"
              :src="personComputerFilePath"
            />
            {{ groupLabel }}
          </p>
          <li
            class="recommendation__group__item"
            v-for="item in groupData"
            :key="item.label"
          >
            <p class="recommendation__group__item__label">
              <a :href="item.url">{{ item.label }}</a>
              <span v-if="item.group_label !== null">
                by {{ item.group_label }}</span
              >
            </p>
          </li>
        </ul>
      </div>
      <NoResults
        v-else
        class="recommendations__no-results"
        message="No Results :("
      />
    </div>
  </div>
</template>

<script>
import NoResults from "@/components/NoResults.vue";
import ClientSideSearch from "@/components/search/ClientSideSearch.vue";

import recommendationsJson from "@/assets/json/recommendations.json";
import { groupBy } from "@/assets/js/utilities.js";

export default {
  components: {
    NoResults,
    ClientSideSearch
  },
  data() {
    return {
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      recommendations: recommendationsJson,
      searchResults: recommendationsJson,
      searchKeys: ["group_label", "label", "kind", "tags"],
      searchUUID: "url"
    };
  },
  computed: {
    groupedRecommendations() {
      return groupBy(this.searchResults, "kind");
    }
  }
};
</script>

<style>
.recommendations__search {
  margin-left: auto;
  margin-right: auto;
}

.recommendation__group {
  margin-top: 3rem;
}

.recommendation__group__header {
  text-transform: capitalize;
  font-size: 1.5rem;
  font-weight: bold;
}

.recommendation__group__item {
  margin-left: 1rem;
}

.recommendation__group__item__label {
  text-indent: -1rem;
  padding-left: 1rem;
}

.person-computer {
  width: 1rem;
  margin-left: -1rem; /* negative of width */
  float: left;
  position: relative;
  top: 0.6rem;
  left: 0.1rem;
}

.search__image {
  float: right;
  position: relative;
  top: -12px;
}
</style>
