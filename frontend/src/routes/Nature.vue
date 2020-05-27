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
