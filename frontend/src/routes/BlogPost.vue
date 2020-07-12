<template>
  <section class="blog-post">
    <NotFound v-if="error === true" :requestedPath="this.$route.fullPath" />
    <div v-if="postTitle != null" class="section">
      <h1 class="title is-3">{{ postTitle }}</h1>
      <p class="subtitle is-7">{{ postDate }}</p>
      <div class="content" v-html="postContent" />
      <img class="person-bowling" :src="personBowlingFilepath" />
    </div>
  </section>
</template>

<script>
import NotFound from "@/routes/NotFound.vue";

import { getBlogPost } from "@/assets/js/api.js";

export default {
  components: {
    NotFound
  },
  data() {
    return {
      error: false,
      postTitle: null,
      postContent: null,
      postDate: null,
      personBowlingFilepath: require("@/assets/people/person-bowling.svg")
    };
  },
  methods: {
    initialize: function() {
      this.error = false;
      this.postID = this.$route.params.id;
      this.getPost(this.postID);
    },
    getPost: function(postID) {
      getBlogPost(postID).then(response => {
        if (response.data != null) {
          this.postTitle = response.data.title;
          this.postDate = response.data.date;
          this.postContent = response.data.content;
        } else {
          this.error = true;
          return null;
        }
      });
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
