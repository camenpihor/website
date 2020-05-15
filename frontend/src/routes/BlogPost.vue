<template>
  <div>
    <NotFound
      v-if="(post === null) & (error === true)"
      :requestedPath="this.$route.fullPath"
    />
    <div v-if="post !== null" class="blog-post">
      <SearchBar class="blog-post__search" />
      <div class="blog-post__body">
        <h1 class="blog-post__title">{{ post.title }}</h1>
        <p class="blog-post__date">{{ post.created }}</p>
        <div class="blog-post__text" v-html="post.html" />
      </div>
      <img class="person-bowling" :src="personBowlingFilepath" />
    </div>
  </div>
</template>

<script>
import NotFound from "@/routes/NotFound.vue";
import SearchBar from "@/components/SearchBar.vue";

import blogPostsJson from "@/assets/blog_posts.json";

export default {
  components: {
    NotFound,
    SearchBar
  },
  data() {
    return {
      error: false,
      postURL: null,
      post: null,
      personBowlingFilepath: require("@/assets/people/person-bowling.svg")
    };
  },
  methods: {
    initialize: function() {
      this.error = false;
      this.postURL = this.$route.params.id;
      this.post = this.getPost(blogPostsJson, this.postURL);
    },
    getPost: function(allPosts, postID) {
      for (var i = 0; i < allPosts.length; i++) {
        if (allPosts[i]["url"] == postID) {
          return allPosts[i];
        }
      }
      this.error = true;
      return null;
    }
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        this.initialize();
      }
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>

<style>
.blog-post {
  padding-bottom: 7rem;
}

.blog-post__search {
  margin-left: auto;
  margin-right: auto;
}

.blog-post__body {
  margin-top: 5rem;
}

.blog-post__title {
  font-size: 1.5rem;
  font-weight: bold;
}

.blog-post__date {
  margin-top: 0.2rem;
  font-weight: lighter;
  font-size: 0.7rem;
}

.blog-post__text {
  margin-top: 1rem;
}

.blog-post__text p {
  margin-top: 1rem;
}

.person-bowling {
  position: absolute;
  bottom: 2.5rem; /* height of footer */
  left: 2rem;
}
</style>
