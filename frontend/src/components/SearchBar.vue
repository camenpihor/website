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
      @click.native="clearInput"
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
    clearInput: function() {
      this.input = null;
    },
    search: function() {
      if (this.input != null) {
        return this.method(this.input);
      } else {
        this.$refs.search.$el.getElementsByTagName("input")[0].blur();
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
</style>