<template>
  <div class="search-bar">
    <b-input
      v-model="input"
      rounded
      :placeholder="placeholder"
      type="search"
      icon-pack="fal"
      icon="search"
      @input="search"
      @keyup.native.enter="blurThis"
      ref="search"
    />
    <img
      v-if="imageFilePath !== null"
      class="search__image"
      :src="imageFilePath"
    />
  </div>
</template>

<script>
import * as JsSearch from "js-search";

export default {
  props: {
    placeholder: {
      type: String,
      default: "search..."
    },
    imageFilePath: {},
    keys: {},
    json: {},
    jsonUUID: {},
    method: {}
  },
  data() {
    return {
      input: "",
      results: this.json,
      searcher: this.createSearcher()
    };
  },
  methods: {
    blurThis: function() {
      this.$refs.search.$el.getElementsByTagName("input")[0].blur();
    },
    search: function() {
      if (this.input === "") {
        this.results = this.json;
      } else {
        this.results = this.searcher.search(this.input);
      }
      this.$emit("output", this.results);
    },
    createSearcher: function() {
      var search = new JsSearch.Search(this.jsonUUID);
      for (let key of this.keys) {
        search.addIndex(key);
      }
      search.addDocuments(this.json);
      return search;
    }
  }
};
</script>

<style>
.search-bar {
  max-width: 20rem;
  padding-left: 1rem;
  padding-right: 1rem;
}

/* buefy class */
.search-bar .input {
  border-radius: 15px;
}

.search-bar input:not(:focus) {
  color: #b1b1b1;
}
</style>