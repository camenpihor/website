<template>
  <div class="blog">
    <SearchBar
      class="blog__search"
      placeholder="search..."
      :imageFilePath="personReadingFilePath"
    />
    <div class="blog__posts">
      <div class="blog__post" v-for="post in blogPostsJson" :key="post.title">
        <router-link :to="{ name: 'blog-post', params: { id: post.url } }">
          <h1 class="blog__post__title">{{ post.title }}</h1>
          <p class="blog__post__date">{{ post.created }}</p>
          <div class="blog__post__text">{{ truncateText(post.intro) }}</div>
        </router-link>
      </div>
    </div>
    <img class="person-wave" :src="personWaveFilePath" />
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar.vue";
import blogPostsJson from "@/assets/blog_posts.json";

export default {
  components: {
    SearchBar
  },
  data() {
    return {
      blogPostsJson: blogPostsJson,
      personReadingFilePath: require("@/assets/people/person-reading.svg"),
      personWaveFilePath: require("@/assets/people/person-wave.svg")
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
  cursor: pointer;
}

.blog__post:hover {
  margin-left: 10px;
  margin-right: -10px;
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
  position: relative;
  top: 4.2rem;
}

.search__image {
  float: right;
  position: relative;
  top: -25px;
  left: 23px;
}
</style>
