<template>
  <div class="life">
    <div class="columns is-mobile is-gapless">
      <div class="column">
        <img
          :src="wolfFilePath"
          v-on:click="activeIcon = 'wolf'"
          class="life__icon"
          v-bind:class="{ highlight: activeIcon === 'wolf' }"
        />
      </div>
      <div class="column">
        <img
          :src="sunsetFilePath"
          v-on:click="activeIcon = 'sunset'"
          class="life__icon"
          v-bind:class="{ highlight: activeIcon === 'sunset' }"
        />
      </div>
      <div class="column">
        <img
          :src="unknownFilePath"
          v-on:click="activeIcon = 'unknown'"
          class="life__icon"
          v-bind:class="{ highlight: activeIcon === 'unknown' }"
        />
      </div>
      <div class="column">
        <img
          :src="stairsFilePath"
          v-on:click="activeIcon = 'stairs'"
          class="life__icon"
          v-bind:class="{ highlight: activeIcon === 'stairs' }"
        />
      </div>
    </div>
    <div class="life__text">
      <p v-if="activeIcon === 'wolf'">
        This is for the wolf. Torquatos nostros? quos tu tam egregios viros
        censes tantas res gessisse sine dubio praeclara sunt, explicabo nemo
        enim ad modum, quaeso, interpretaris? sicine eos censes tantas res
        gessisse sine dubio praeclara sunt, fecerint, virtutem iis per. Tap the
        sunset next!
      </p>
      <p v-if="activeIcon === 'sunset'">
        This is for the sunset. Torquatos nostros? quos tu tam egregios viros
        censes tantas res gessisse sine dubio praeclara sunt, explicabo nemo
        enim ad modum, quaeso, interpretaris? sicine eos censes tantas res
        gessisse sine dubio praeclara sunt, fecerint, virtutem iis per. Tap the
        red circle next!
      </p>
      <p v-if="activeIcon === 'unknown'">
        This is for the unknown. Torquatos nostros? quos tu tam egregios viros
        censes tantas res gessisse sine dubio praeclara sunt, explicabo nemo
        enim ad modum, quaeso, interpretaris? sicine eos censes tantas res
        gessisse sine dubio praeclara sunt, fecerint, virtutem iis per. Tap the
        stairs next!
      </p>
      <p v-if="activeIcon === 'stairs'">
        This is for the stairs. Torquatos nostros? quos tu tam egregios viros
        censes tantas res gessisse sine dubio praeclara sunt, explicabo nemo
        enim ad modum, quaeso, interpretaris? sicine eos censes tantas res
        gessisse sine dubio praeclara sunt, fecerint, virtutem iis per. Tap the
        wolf next!
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      wolfFilePath: require("@/assets/icons/wolf-icon.svg"),
      unknownFilePath: require("@/assets/icons/unknown-life-icon.svg"),
      sunsetFilePath: require("@/assets/icons/sunset-icon.svg"),
      stairsFilePath: require("@/assets/icons/current-life-icon.svg"),
      activeIcon: "wolf"
    };
  }
};
</script>

<style>
.life__icon {
  height: 3.75rem;
  width: 3.75rem;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.life__text {
  font-size: 1rem;
}

.highlight {
  border: 2px solid #3273dc;
  border-radius: 50%;
}
</style>
