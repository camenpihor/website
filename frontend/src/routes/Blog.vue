<template>
  <section class="blog">
    <div v-if="searchResults != null">
      <ClientSideSearch
        class="blog__search"
        :imageFilePath="personReadingFilePath"
        :keys="searchKeys"
        :jsonUUID="searchUUID"
        :json="blogPostsJson"
        v-on:output="searchResults = $event"
      />
      <div v-if="searchResults.length > 0" class="section">
        <div
          class="blog__post subsection"
          v-for="post in searchResults"
          :key="post.title"
        >
          <h1 class="title is-4 is-capitalized">{{ post.title }}</h1>
          <p class="subtitle is-7">{{ post.date }}</p>
          <div>{{ post.summary }}</div>
          <p>
            <router-link :to="{ name: 'blog-post', params: { id: post.url } }">
              read more
            </router-link>
          </p>
        </div>
      </div>
      <div v-else>
        <NoResults message="No Results :(" />
      </div>
    </div>
  </section>
</template>

<script>
import NoResults from "@/components/NoResults.vue";
import ClientSideSearch from "@/components/search/ClientSideSearch.vue";

import { getBlogPosts } from "@/assets/js/api.js";

export default {
  components: {
    NoResults,
    ClientSideSearch
  },
  data() {
    return {
      blogPostsJson: null,
      personReadingFilePath: require("@/assets/people/person-reading.svg"),
      isSmallWindow: window.innerWidth <= 1023,
      searchKeys: ["html", "title"],
      searchUUID: "url",
      searchResults: null
    };
  },
  methods: {
    initialize: function() {
      getBlogPosts().then(response => {
        this.blogPostsJson = response.data;
        this.searchResults = response.data;
      });
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>

<style>
.blog__search {
  margin-top: 3.25rem;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 2.5rem;
}

.blog__post:first-of-type {
  padding-top: 0;
}

.blog__search .search__image {
  width: 1.5rem;
  float: right;
  position: relative;
  top: -1.5rem;
  left: 1.5rem;
}

.blog__post .subtitle {
  margin-top: -1.05rem !important;
}
</style>
