<template>
  <section class="blog">
    <ClientSideSearch
      class="blog__search"
      :imageFilePath="personReadingFilePath"
      :keys="searchKeys"
      :jsonUUID="searchUUID"
      :json="blogPostsJson"
      v-on:output="searchResults = $event"
    />
    <div v-if="searchResults.length > 0" class="section">
      <div class="subsection" v-for="post in searchResults" :key="post.title">
        <h1 class="title is-4">{{ post.title }}</h1>
        <p class="subtitle is-7">{{ post.created }}</p>
        <div>{{ truncateText(post.intro) }}</div>
        <p>
          <router-link :to="{ name: 'blog-post', params: { id: post.url } }">
            read more
          </router-link>
        </p>
      </div>
      <img class="person-wave" :src="personWaveFilePath" />
    </div>
    <div v-else>
      <NoResults message="No Results :(" />
    </div>
  </section>
</template>

<script>
import NoResults from "@/components/NoResults.vue";
import ClientSideSearch from "@/components/search/ClientSideSearch.vue";

import blogPostsJson from "@/assets/json/blog_posts.json";

export default {
  components: {
    NoResults,
    ClientSideSearch
  },
  data() {
    return {
      blogPostsJson: blogPostsJson,
      personReadingFilePath: require("@/assets/people/person-reading.svg"),
      personWaveFilePath: require("@/assets/people/person-wave.svg"),
      isSmallWindow: window.innerWidth <= 1023,
      searchKeys: ["html", "title"],
      searchUUID: "url",
      searchResults: blogPostsJson
    };
  },
  methods: {
    truncateText: function(text) {
      return text.slice(3, 500) + "...";
    }
  }
};
</script>

<style>
.blog__search {
  margin-top: 3.25rem;
  margin-left: auto;
  margin-right: auto;
}

.person-wave {
  width: 1rem;
  position: absolute;
  bottom: calc(1rem + 4rem + 5rem);
  /* footer fontsize + footer top padding + footer bottom padding */
}

.blog__search .search__image {
  width: 1.5rem;
  float: right;
  position: relative;
  top: -1.5rem;
  left: 1.5rem;
}
</style>
