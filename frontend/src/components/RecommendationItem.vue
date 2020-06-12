<template>
  <div class="recommendation">
    <div class="recommendation__title">
      <p>
        <a :href="href" target="_blank">{{ label }}</a>
        <span v-if="group !== null"> by {{ group }} </span>
      </p>
      <div class="tags">
        <span class="tag" v-for="tag in tags" :key="tag">{{ tag }}</span>
        <span
          v-if="info != null"
          class="tag recommendation__info-button"
          @click="toggleInfo(showInfo)"
          >why?</span>
      </div>
    </div>
    <div
      v-if="(info != null) & showInfo"
      class="recommendation__info is-size-7"
    >
      {{ info }}
    </div>
  </div>
</template>

<script>
export default {
  props: ["href", "label", "group", "tags", "info"],
  data() {
    return {
      showInfo: false
    };
  },
  methods: {
    toggleInfo: function() {
      this.showInfo = !this.showInfo;
    }
  }
};
</script>

<style>
.recommendation__title {
  text-indent: -1rem;
  padding-left: 1rem;
}

.recommendation__info-button {
  cursor: pointer;
}

.recommendation__info-button:hover {
  text-decoration: underline;
}

.recommendation__info {
  padding: 1rem 2rem;
}
</style>
