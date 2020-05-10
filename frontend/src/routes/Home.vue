<template>
  <div class="home">
    <Background class="background" :filePath="backgroundFilePath" />
    <div class="page">
      <div class="life-summary">
        <div
          class="life-summary-icons columns is-mobile is-vcentered is-centered"
        >
          <div class="column" v-on:click="activeLifeIcon = 'wolf'">
            <LifeIcon
              :filePath="wolfFilePath"
              v-bind:class="{ highlight: activeLifeIcon === 'wolf' }"
            />
          </div>
          <div class="column" v-on:click="activeLifeIcon = 'sunset'">
            <LifeIcon
              :filePath="sunsetFilePath"
              v-bind:class="{ highlight: activeLifeIcon === 'sunset' }"
            />
          </div>
          <div class="column" v-on:click="activeLifeIcon = 'unknown'">
            <LifeIcon
              :filePath="unknownLifeFilePath"
              v-bind:class="{ highlight: activeLifeIcon === 'unknown' }"
            />
          </div>
          <div class="column" v-on:click="activeLifeIcon = 'stairs'">
            <LifeIcon
              :filePath="currentLifeFilePath"
              v-bind:class="{ highlight: activeLifeIcon === 'stairs' }"
            />
          </div>
        </div>
        <div class="life-summary-text">
          <p v-if="activeLifeIcon === 'wolf'">
            This is for the wolf. Torquatos nostros? quos tu tam egregios viros
            censes tantas res gessisse sine dubio praeclara sunt, explicabo nemo
            enim ad modum, quaeso, interpretaris? sicine eos censes tantas res
            gessisse sine dubio praeclara sunt, fecerint, virtutem iis per. Tap
            the sunset next!
          </p>
          <p v-if="activeLifeIcon === 'sunset'">
            This is for the sunset. Torquatos nostros? quos tu tam egregios
            viros censes tantas res gessisse sine dubio praeclara sunt,
            explicabo nemo enim ad modum, quaeso, interpretaris? sicine eos
            censes tantas res gessisse sine dubio praeclara sunt, fecerint,
            virtutem iis per. Tap the red circle next!
          </p>
          <p v-if="activeLifeIcon === 'unknown'">
            This is for the unknown. Torquatos nostros? quos tu tam egregios
            viros censes tantas res gessisse sine dubio praeclara sunt,
            explicabo nemo enim ad modum, quaeso, interpretaris? sicine eos
            censes tantas res gessisse sine dubio praeclara sunt, fecerint,
            virtutem iis per. Tap the stairs next!
          </p>
          <p v-if="activeLifeIcon === 'stairs'">
            This is for the stairs. Torquatos nostros? quos tu tam egregios
            viros censes tantas res gessisse sine dubio praeclara sunt,
            explicabo nemo enim ad modum, quaeso, interpretaris? sicine eos
            censes tantas res gessisse sine dubio praeclara sunt, fecerint,
            virtutem iis per. Tap the wolf next!
          </p>
        </div>
      </div>
      <hr class="break-line" />
      <div class="bio-info">
        <h1 class="section-title">Hai! I'm Camen :)</h1>
        <img class="person-wave-image" :src="personWaveFilePath" />
        <p>
          And this is my short bio. I made this website for these reason, and it
          holds these types sorts of things because I like these sorts of
          things. To read more about me and what I like, check out my About
          page, which will also include a list of blogs and online resources
          that I like to peruse.
        </p>
        <p class="bio-text">
          et aperta iudicari ea voluptate velit esse, quam interrogare aut
          contra sit, amet, consectetur, adipisci velit, sed quia consequuntur
          magni dolores et expedita distinctio nam libero tempore, cum
          memoriter, tum etiam erga nos amice et via.
        </p>
      </div>
      <hr class="break-line" />
      <div class="website-info">
        <h1 class="section-title">And this is my website</h1>
        <img class="person-parachute-image" :src="personParachuteFilePath" />
        <div class="site-map columns is-mobile is-centered">
          <div class="column site-map-section">
            <h1 class="site-map-header">General</h1>
            <ul class="site-map-list">
              <li class="site-map-item">Home</li>
              <li class="site-map-item">About</li>
              <li class="site-map-item">Recommendations</li>
              <li class="site-map-item">GitHub</li>
            </ul>
          </div>

          <div class="column site-map-section">
            <h1 class="site-map-header">Projects</h1>
            <ul class="site-map-list">
              <li class="site-map-item">Blog</li>
              <li class="site-map-item">Math Implementations</li>
              <li class="site-map-item">Measurements for Humans</li>
              <li class="site-map-item">Nature Identifications</li>
              <li class="site-map-item">RogueSky</li>
              <li class="site-map-item">TreeCount</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <img class="person-sitting-image" :src="personSittingFilePath" />
  </div>
</template>

<script>
import Background from "@/components/Background.vue";
import LifeIcon from "@/components/LifeIcon.vue";

export default {
  name: "home",
  components: {
    Background,
    LifeIcon
  },
  data() {
    return {
      backgroundFilePath: require("@/assets/space.jpg"),
      wolfFilePath: require("@/assets/wolf-icon.svg"),
      unknownLifeFilePath: require("@/assets/unknown-life-icon.svg"),
      sunsetFilePath: require("@/assets/sunset-icon.svg"),
      currentLifeFilePath: require("@/assets/current-life-icon.svg"),
      personWaveFilePath: require("@/assets/person-wave.svg"),
      personParachuteFilePath: require("@/assets/person-parachute.svg"),
      personSittingFilePath: require("@/assets/person-sitting.svg"),
      activeLifeIcon: "wolf"
    };
  }
};
</script>

<style>
.background {
  position: relative;
  top: -60px;
  height: 33vh;
}

.page {
  margin-top: -60px;
  margin-left: 10px;
  margin-right: 10px;
  padding-bottom: 40px;
  max-width: 700px;
  margin: auto;
}

.life-summary {
  margin-top: 20px;
}

.life-summary-icons {
  width: 100%;
}

.highlight {
  border: 2px solid rgb(0, 110, 255);
  border-radius: 50%;
}

.life-summary-text {
  margin-top: 8px;
}

.break-line {
  margin-top: 40px;
  margin-left: 39.5px;
  margin-right: 39.5px;
  margin-bottom: 40px;
  color: #979797;
  background-color: #979797;
  height: 1px;
  border: none;
}

.section-title {
  font-weight: bold;
  font-size: 16px;
}

.bio-text {
  margin-top: 20px;
}

.person-wave-image {
  position: relative;
  right: -105px;
  top: -26px;
}

.site-map {
  margin-top: 10px;
  width: 100%;
}

.person-parachute-image {
  position: relative;
  right: -105px;
  top: -26px;
}

.site-map-header {
  font-size: 14px;
  font-weight: bold;
}

.site-map-item {
  padding: 10px;
  font-size: 14px;
}

.site-map-section {
  padding: 0;
}

.person-sitting-image {
  position: relative;
  right: 135px;
  top: 75px;
}
</style>
