<template>
  <section class="recommendations">
    <div v-if="recommendations != null">
      <ClientSideSearch
        class="recommendations__search"
        :keys="searchKeys"
        :json="recommendations"
        :jsonUUID="searchUUID"
        :imageFilePath="personHangingFilePath"
        v-on:output="searchResults = $event"
        ref="search"
      />

      <div v-if="searchResults.length > 0" class="section">
        <ul
          class="recommendations__group subsection"
          v-for="(groupData, groupLabel, index) in groupedRecommendations"
          :key="groupLabel"
        >
          <p class="heading is-size-5">
            <img
              v-if="index === 1"
              class="person-computer"
              :src="personComputerFilePath"
            />
            {{ groupLabel }}
          </p>
          <li v-for="item in groupData" :key="item.label">
            <p class="recommendation__group__item">
              <a :href="item.url" target="_blank">{{ item.label }}</a>
              <span v-if="item.group_label !== null">
                by {{ item.group_label }}
              </span>
              <span class="tags">
                <span
                  v-for="tag in item.tags"
                  :key="tag"
                  class="tag"
                  @click="search(tag)"
                >
                  {{ tag }}
                </span>
              </span>
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
  </section>
</template>

<script>
import ClientSideSearch from "@/components/search/ClientSideSearch.vue";
import NoResults from "@/components/NoResults.vue";

import recommendationsJson from "@/assets/json/recommendations.json";
import { compare, groupBy } from "@/assets/js/utilities.js";

export default {
  components: {
    ClientSideSearch,
    NoResults
  },
  data() {
    return {
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      recommendations: null,
      searchResults: null,
      searchKeys: ["group_label", "label", "kind", "tags"],
      searchUUID: "label"
    };
  },
  computed: {
    groupedRecommendations() {
      return groupBy(this.searchResults, "kind");
    }
  },
  methods: {
    initialize: function() {
      let arr = recommendationsJson.sort(compare("label"));
      this.recommendations = arr;
      this.searchResults = arr;
    },
    search: function(word) {
      this.$refs.search.input = word;
      this.$refs.search.search();
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>

<style>
.recommendations__search {
  margin-top: 3.25rem;
  margin-left: auto;
  margin-right: auto;
}

.recommendations__group:first-of-type {
  padding-top: 0;
}

.recommendation__group__item {
  text-indent: -1rem;
  padding-left: 1rem;
  padding-bottom: 1rem;
}

.recommendation__group__item .tags .tag {
  cursor: pointer;
  font-size: 0.6rem;
}

.recommendation__group__item .tags .tag:hover {
  text-decoration: underline;
}

.person-computer {
  width: 1rem;
  margin-left: -1rem; /* negative of character width */
  float: left;
  position: relative;
  top: 0.6rem;
  left: 0.1rem;
}

.recommendations__search .search__image {
  width: 3rem;
  float: right;
  position: relative;
  top: -1rem;
}
</style>
