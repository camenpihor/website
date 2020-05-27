<template>
  <div>
    <div v-if="recommendations != null" class="recommendations">
      <SearchBar
        class="recommendations__search"
        :keys="searchKeys"
        :json="recommendations"
        :jsonUUID="searchUUID"
        :imageFilePath="personHangingFilePath"
        v-on:output="searchResults = $event"
      />

      <div class="recommendations__groups">
        <div v-if="searchResults.length > 0">
          <ul
            class="recommendation__group"
            v-for="(groupData, groupLabel, index) in groupBy(
              searchResults,
              'kind'
            )"
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
        <div v-else class="recommendations__no-results">
          <NoResults message="No Results :(" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NoResults from "@/components/NoResults.vue";
import SearchBar from "@/components/SearchBar.vue";
import { getRecommendations } from "@/api.js";

export default {
  components: {
    NoResults,
    SearchBar
  },
  data() {
    return {
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      personHangingFilePath: require("@/assets/people/person-hanging.svg"),
      recommendations: null,
      searchResults: null,
      searchKeys: ["group_label", "label", "kind", "tags"],
      searchUUID: "url"
    };
  },
  methods: {
    initialize: function() {
      this.fetchRecommendations();
    },
    groupBy: function(xs, key) {
      // https://stackoverflow.com/a/38575908
      return xs.reduce(function(rv, x) {
        (rv[x[key]] = rv[x[key]] || []).push(x);
        return rv;
      }, {});
    },
    fetchRecommendations: function() {
      getRecommendations().then(response => {
        this.recommendations = response.data;
        this.searchResults = response.data;
      });
    }
  },
  created() {
    this.initialize();
  }
};
</script>

<style>
.recommendations__search {
  margin-left: auto;
  margin-right: auto;
}

.recommendations__groups {
  margin-top: 5rem;
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
