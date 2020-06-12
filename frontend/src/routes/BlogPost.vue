<template>
  <section class="blog-post">
    <NotFound v-if="error === true" :requestedPath="this.$route.fullPath" />
    <div v-if="post !== null" class="section">
      <h1 class="title is-3">
        {{ post.title }}
      </h1>
      <p class="subtitle is-7">{{ post.created }}</p>
      <img class="person-wave-move-image" :src="personWaveMoveFilePath" />
      <div class="content" v-html="post.html" />
      <img class="person-bowling" :src="personBowlingFilepath" />
    </div>
  </section>
</template>

<script>
import NotFound from "@/routes/NotFound.vue";

import blogPostsJson from "@/assets/json/blog_posts.json";

export default {
  components: {
    NotFound
  },
  data() {
    return {
      personWaveMoveFilePath: require("@/assets/people/person-wave-move.svg"),
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
.blog-post .subtitle {
  margin-top: -1.05rem !important;
}

.person-wave-move-image {
  float: right;
  width: 1rem;
  margin-right: 1rem;
}

.person-bowling {
  position: absolute;
  left: 2rem;
  bottom: calc(1rem + 4rem + 5rem);
  /* footer fontsize + footer top padding + footer bottom padding */
}
</style>
