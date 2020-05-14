<template>
  <div class="search-bar">
    <b-input
      @keyup.native.enter="search"
      v-model="input"
      rounded
      :placeholder="placeholder"
      type="search"
      icon-pack="fal"
      icon="search"
      icon-clickable
      @icon-click="search"
      maxlength="30"
      :has-counter="false"
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
    }
  },
  data() {
    return {
      input: null
    };
  },
  methods: {
    search() {
      console.log("Searching '" + this.input + "'");
    },
    clearInput() {
      this.input = null;
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