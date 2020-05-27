<template>
  <div class="blog">
    <SearchBar
      class="blog__search"
      placeholder="search..."
      :imageFilePath="personReadingFilePath"
      :keys="searchKeys"
      :jsonUUID="searchUUID"
      :json="blogPostsJson"
      v-on:output="searchResults = $event"
    />
    <div v-if="searchResults.length > 0" class="blog__posts">
      <div class="blog__posts__desktop">
        <div class="blog__post" v-for="post in searchResults" :key="post.title">
          <router-link :to="{ name: 'blog-post', params: { id: post.url } }">
            <h1 class="blog__post__title">{{ post.title }}</h1>
            <p class="blog__post__date">{{ post.created }}</p>
            <div class="blog__post__text">{{ truncateText(post.intro) }}</div>
          </router-link>
        </div>
      </div>
      <div class="blog__posts__touch">
        <div class="blog__post" v-for="post in searchResults" :key="post.title">
          <h1 class="blog__post__title">{{ post.title }}</h1>
          <p class="blog__post__date">{{ post.created }}</p>
          <div class="blog__post__text">{{ truncateText(post.intro) }}</div>
          <router-link :to="{ name: 'blog-post', params: { id: post.url } }">
            read more
          </router-link>
        </div>
      </div>
      <img class="person-wave" :src="personWaveFilePath" />
    </div>
    <div v-else>
      <NoResults message="No Results :(" />
    </div>
  </div>
</template>

<script>
import NoResults from "@/components/NoResults.vue";
import SearchBar from "@/components/SearchBar.vue";
import blogPostsJson from "@/assets/blog_posts.json";

export default {
  components: {
    NoResults,
    SearchBar
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
  margin-left: auto;
  margin-right: auto;
}

.blog__posts {
  margin-top: 5rem;
}

.blog__post:first-of-type {
  margin-top: 0rem;
}

.blog__post {
  margin-top: 3rem;
}

.blog__post__title {
  font-size: 1.5rem;
  font-weight: bold;
}

.blog__post__date {
  margin-top: 0.2rem;
  font-weight: lighter;
  font-size: 0.7rem;
}

.blog__post__text {
  margin-top: 1rem;
}

.person-wave {
  position: absolute;
  bottom: 2.5rem; /* footer height */
}

.search__image {
  float: right;
  position: relative;
  top: -25px;
  left: 23px;
}

.blog__posts__desktop {
  display: none;
}

.blog__posts__touch {
  display: none;
}

@media only screen and (max-width: 1024px) {
  .blog__posts__desktop {
    display: none;
  }

  .blog__posts__touch {
    display: inherit;
  }
}

@media only screen and (min-width: 1024px) {
  .blog__post:hover {
    margin-left: 10px;
    margin-right: -10px;
  }

  .blog__posts__touch {
    display: none;
  }

  .blog__posts__desktop {
    display: inherit;
  }
}
</style>
