<template>
  <div class="search-bar">
    <EventListener :method="focusSearch" />

    <b-input
      v-model="input"
      rounded
      :placeholder="placeholder"
      type="search"
      @keyup.native.enter="search"
      @keyup.native.esc="blurSearch"
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
import EventListener from "@/components/EventListener.vue";

export default {
  components: {
    EventListener,
  },
  props: {
    placeholder: {
      type: String,
      default: "search...",
    },
    imageFilePath: {
      type: String,
      default: null,
    },
    method: {
      type: Function,
    },
  },
  data() {
    return {
      input: null,
    };
  },
  methods: {
    search: function() {
      this.blurSearch();
      if (this.input != null) {
        return this.method(this.input);
      }
    },
    blurSearch: function() {
      this.$refs.search.$el.getElementsByTagName("input")[0].blur();
    },
    focusSearch: function(event) {
      let badTags = ["INPUT", "TEXTAREA"];
      if ((event.code === "Slash") & !badTags.includes(event.target.tagName)) {
        this.$refs.search.$el.getElementsByTagName("input")[0].focus();
      }
    },
  },
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
