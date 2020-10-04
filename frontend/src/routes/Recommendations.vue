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
        :initial="query"
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
          <li
            v-for="item in groupData"
            :key="item.label"
            class="recommendations__item"
          >
            <RecommendationItem
              :href="item.url"
              :label="item.label"
              :group="item.group_label"
              :tags="item.tags"
              :info="item.endorsement"
            />
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
import RecommendationItem from "@/components/RecommendationItem.vue";

import recommendationsJson from "@/assets/json/recommendations.json";
import { compare, groupBy } from "@/assets/js/utilities.js";

export default {
  components: {
    ClientSideSearch,
    NoResults,
    RecommendationItem,
  },
  data() {
    return {
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      recommendations: null,
      searchResults: null,
      query: null,
      searchKeys: ["group_label", "label", "kind", "tags"],
      searchUUID: "label",
    };
  },
  computed: {
    groupedRecommendations() {
      return groupBy(this.searchResults, "kind");
    },
  },
  methods: {
    initialize: function() {
      let arr = recommendationsJson.sort(compare("label"));
      this.recommendations = arr;
      this.searchResults = arr;

      this.query = "";
      if (this.$route.query.search != null) {
        this.query = this.$route.query.search;
        this.$router.replace("");
      }
    },
    toggleInfo: function(event) {
      let recommendationItem = event.target.parentElement.parentElement;
      let endorsement = recommendationItem.querySelector(
        ".recommendation__group__item__info"
      );
      endorsement.classList.toggle("is-hidden");
    },
  },
  mounted() {
    this.initialize();
  },
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

.recommendations__item {
  padding-bottom: 1rem;
}

.recommendations__group .person-computer {
  width: 1rem;
  margin-left: -1rem; /* negative of character width */
  float: left;
  position: relative;
  top: 0.6rem;
  left: 0.1rem;
}

.recommendations__search .search__image {
  width: 3rem;
  position: absolute;
  top: 1.3rem;
  right: 1rem;
}
</style>
