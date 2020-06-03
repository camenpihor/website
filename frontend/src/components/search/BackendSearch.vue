<template>
  <div class="search-bar">
    <b-input
      v-model="input"
      rounded
      :placeholder="placeholder"
      type="search"
      icon-pack="fal"
      icon="search"
      icon-clickable
      @icon-click="search"
      @keyup.native.enter="search"
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
export default {
  props: {
    placeholder: {
      type: String,
      default: "search..."
    },
    imageFilePath: {
      type: String,
      default: null
    },
    method: {
      type: Function
    }
  },
  data() {
    return {
      input: null
    };
  },
  methods: {
    blurThis: function() {
      this.$refs.search.$el.getElementsByTagName("input")[0].blur();
    },
    search: function() {
      this.blurThis();
      if (this.input != null) {
        return this.method(this.input);
      }
    }
  }
};
</script>

<style>
.search-bar {
  max-width: 20rem;
}

/* buefy class */
.search-bar .input {
  border-radius: 15px;
}

.search-bar input:not(:focus) {
  color: #b1b1b1;
}
</style>