<template>
  <div>
    <div v-if="allRecommendations != null" class="recommendations">
      <div class="recommendations__filters">
        <img
          class="person-computer"
          :src="personComputerFilePath"
        />
        <b-dropdown multiple>
          <button class="button is-dark" type="button" slot="trigger">
            <span>Kinds</span>
          </button>

          <b-dropdown-item
            custom
            paddingless
            v-for="kind in allKinds"
            :key="kind"
          >
            <label class="checkbox dropdown__item">
              <input
                type="checkbox"
                :name="kind"
                :checked="selectedKinds.includes(kind)"
                v-on:click="handleKindChange"
              />
              {{ kind }}
            </label>
          </b-dropdown-item>
        </b-dropdown>
      </div>

      <div class="recommendations__groups">
        <ul
          class="recommendation__group"
          v-for="(groupData, groupLabel) in selectedRecommendations"
          :key="groupLabel"
        >
          <p class="recommendation__group__header">
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
    </div>
  </div>
</template>

<script>
import { getRecommendations } from "@/api.js";

export default {
  data() {
    return {
      personComputerFilePath: require("@/assets/people/person-computer.svg"),
      allRecommendations: null,
      allKinds: null,
      selectedKinds: null,
      allTags: null,
      selectedTags: null,
      searchError: false
    };
  },
  methods: {
    initialize: function() {
      this.fetchRecommendations();
      this.fetchTags();
    },
    groupBy: function(xs, key) {
      // https://stackoverflow.com/a/38575908
      return xs.reduce(function(rv, x) {
        (rv[x[key]] = rv[x[key]] || []).push(x);
        return rv;
      }, {});
    },
    fetchRecommendations: function() {
      getRecommendations()
        .then(response => {
          let data = this.groupBy(response.data, "kind");
          this.allRecommendations = data;
          this.allKinds = Object.keys(data);
          this.selectedKinds = Object.keys(data);
        })
        .catch(() => {
          this.searchError = true;
        });
    },
    fetchTags: function() {
      getRecommendations("tag=unique").then(response => {
        this.allTags = response.data;
        this.selectedTags = response.data;
      });
    },
    handleKindChange: function(e) {
      let kind = e.target.name;

      if (e.target.checked) {
        this.selectedKinds.push(kind);
      } else {
        this.selectedKinds.splice(this.selectedKinds.indexOf(kind), 1);
      }
    }
  },
  computed: {
    selectedRecommendations() {
      if (this.allRecommendations != null) {
        var recommendations = JSON.parse(
          JSON.stringify(this.allRecommendations)
        );

        for (let key of Object.keys(recommendations)) {
          if (!this.selectedKinds.includes(key)) {
            delete recommendations[key];
          }
        }

        return recommendations;
      }
      return null;
    }
  },
  created() {
    this.initialize();
  }
};
</script>

<style>
.recommendations__filters {
  text-align: right;
}

.recommendations .button {
  width: 5rem;
}

.recommendations__groups {
  margin-top: -2rem;
}

.recommendation__group:first-of-type {
  margin-top: 0rem;
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
  position: relative;
  top: 1rem;
}

.search__image {
  float: right;
  position: relative;
  top: -12px;
}

.dropdown__item {
  width: 100%;
  padding: 7px 20px;
  margin-top: 5px;
  text-align: left;
}

.dropdown__item:hover {
  background-color: #9797971a;
}
</style>
