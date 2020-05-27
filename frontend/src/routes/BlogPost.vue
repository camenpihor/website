<template>
  <div>
    <NotFound v-if="error === true" :requestedPath="this.$route.fullPath" />
    <div v-if="post !== null" class="blog-post">
      <h1 class="blog-post__title">
        {{ post.title }}
        <img class="person-wave-move-image" :src="personWaveMoveFilePath" />
      </h1>
      <p class="blog-post__date">{{ post.created }}</p>
      <div class="blog-post__text" v-html="post.html" />
      <img class="person-bowling" :src="personBowlingFilepath" />
    </div>
  </div>
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
.blog-post {
  margin-top: 1rem;
  padding-bottom: 7rem;
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

.person-wave-move-image {
  float: right;
  width: 1rem;
  margin-right: 4rem;
}

.person-bowling {
  position: absolute;
  bottom: 2.5rem; /* height of footer */
  left: 2rem;
}
</style>
