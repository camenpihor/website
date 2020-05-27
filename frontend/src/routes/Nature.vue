<template>
  <div class="nature">
    <p class="nature__intro">
      This is a page that tracks my nature identification pursuits. Alii autem,
      quibus ego assentior, cum soluta nobis est cur nec in bonis sit extremum
      et dolorem eum iure reprehenderit, qui haec ratio late patet in quo minus
      id, quod maxime placeat, facere nondum depravatum ipsa natura ipsa
      iudicari etenim quoniam detractis de voluptate et.
    </p>
    <div class="nature__items">
      <div class="nature__page-info">
        <h1 class="nature__page-header">Nature Identification</h1>
        <b-dropdown v-model="displayType" multiple scrollable max-height="100">
          <button class="button is-blue" slot="trigger" slot-scope="{ active }">
            <span class="button__label">By Type</span>
            <b-icon
              class="button__icon"
              pack="fas"
              :icon="active ? 'sort-up' : 'sort-down'"
            />
          </button>
          <b-dropdown-item value="trees">Trees</b-dropdown-item>
          <b-dropdown-item value="birds">Birds</b-dropdown-item>
          <b-dropdown-item value="rocks">Rocks</b-dropdown-item>
        </b-dropdown>
        <b-dropdown
          v-model="displayLocation"
          multiple
          scrollable
          max-height="100"
        >
          <button class="button is-blue" slot="trigger" slot-scope="{ active }">
            <span class="button__label">By Location</span>
            <b-icon
              class="button__icon"
              pack="fas"
              :icon="active ? 'sort-up' : 'sort-down'"
            />
          </button>
          <b-dropdown-item value="seattle">Seattle</b-dropdown-item>
          <b-dropdown-item value="chicago">Chicago</b-dropdown-item>
          <b-dropdown-item value="south-bend">South Bend</b-dropdown-item>
        </b-dropdown>
      </div>
      <div class="nature__section">
        <h1 class="nature__section__heading">Trees</h1>
      </div>
      <div class="nature__section">
        <h1 class="nature__section__heading">Birds</h1>
      </div>

      <div class="nature__section">
        <h1 class="nature__section__heading">Rocks</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      displayType: [],
      displayLocation: []
    };
  }
};
</script>

<style>
.nature__items {
  margin-top: 3rem;
}

.nature__page-info {
  text-align: center;
}

.nature__page-header {
  font-size: 2rem;
  font-weight: bold;
}

.nature__section {
  margin-top: 3rem;
}

.nature__section__heading {
  font-size: 1.5rem;
  font-weight: bold;
}
</style>
