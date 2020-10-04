<template>
  <div class="search-bar is-relative">
    <EventListener :method="focusSearch" />

    <b-input
      v-model="input"
      rounded
      :placeholder="placeholder"
      type="search"
      @input="search"
      @keyup.native.enter="blurSearch"
      @keyup.native.esc="blurSearch"
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
import EventListener from "@/components/EventListener.vue";

import * as JsSearch from "js-search";

export default {
  components: {
    EventListener,
  },
  props: {
    placeholder: {
      type: String,
      default: "search...",
    },
    imageFilePath: {},
    keys: {},
    json: {},
    jsonUUID: {},
    initial: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      input: this.initial,
      results: this.json,
      searcher: this.createSearcher(),
    };
  },
  methods: {
    search: function() {
      if (this.input === "") {
        this.results = this.json;
      } else {
        this.results = this.searcher.search(this.input);
      }
      this.$emit("output", this.results);
    },
    blurSearch: function() {
      this.$refs.search.$el.getElementsByTagName("input")[0].blur();
    },
    focusSearch: function(event) {
      let badTags = ["INPUT", "TEXTAREA"];
      if ((event.code === "Slash") & !badTags.includes(event.target.tagName)) {
        this.$refs.search.$el.getElementsByTagName("input")[0].focus();
      }
    },
    createSearcher: function() {
      var search = new JsSearch.Search(this.jsonUUID);
      for (let key of this.keys) {
        search.addIndex(key);
      }
      search.addDocuments(this.json);
      return search;
    },
  },
  mounted() {
    this.search();
  },
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
