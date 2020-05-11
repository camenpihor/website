<template>
  <div class="home">
    <div v-on:click="isImageModalActive = true">
      <Background class="home__image" :filePath="backgroundFilePath" />
    </div>
    <b-modal full-screen can-cancel :active.sync="isImageModalActive">
      <ForeverBackground :filePath="backgroundFilePath" />
    </b-modal>
    <div class="home__text">
      <div class="section">
        <LifeIcons />
      </div>

      <hr class="home__break-line" />

      <div class="section">
        <h1 class="section__title">Hai! I'm Camen :)</h1>
        <img class="person-wave-image" :src="personWaveFilePath" />
        <p>
          And this is my short bio. I made this website for these reason, and it
          holds these types sorts of things because I like these sorts of
          things. To read more about me and what I like, check out my About
          page, which will also include a list of blogs and online resources
          that I like to peruse.
        </p>
        <p style="margin-top: 20px;">
          et aperta iudicari ea voluptate velit esse, quam interrogare aut
          contra sit, amet, consectetur, adipisci velit, sed quia consequuntur
          magni dolores et expedita distinctio nam libero tempore, cum
          memoriter, tum etiam erga nos amice et via.
        </p>
      </div>

      <hr class="home__break-line" />

      <div class="section">
        <h1 class="section__title">And this is my website</h1>
        <img class="person-parachute-image" :src="personParachuteFilePath" />
        <div class="columns is-mobile">
          <div class="column">
            <h1 class="home__site-map__header">General</h1>
            <ul class="home__site-map__list">
              <li class="home__site-map__item">
                <router-link to="/foo">Home</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">About</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">Recommendations</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">GitHub</router-link>
              </li>
            </ul>
          </div>
          <div class="column">
            <h1 class="home__site-map__header">Projects</h1>
            <ul class="home__site-map__group">
              <li class="home__site-map__item">
                <router-link to="/foo">Blog</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">Math Implementations</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">Measurements for Humans</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">Nature Identifications</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">RogueSky</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link to="/foo">TreeCount</router-link>
              </li>
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
import ForeverBackground from "@/components/ForeverBackground.vue";
import LifeIcons from "@/components/LifeIcons.vue";

export default {
  name: "home",
  components: {
    Background,
    ForeverBackground,
    LifeIcons
  },
  data() {
    return {
      backgroundFilePath: require("@/assets/space.jpg"),
      personWaveFilePath: require("@/assets/person-wave.svg"),
      personParachuteFilePath: require("@/assets/person-parachute.svg"),
      personSittingFilePath: require("@/assets/person-sitting.svg"),
      isImageModalActive: false
    };
  }
};
</script>

<style style="scss">
.home__image {
  position: relative;
  top: -60px; /* offset navbar */
  height: 33vh;
}

.home__text {
  position: relative;
  top: -60px; /* offset navbar */
  max-width: 700px;
  margin: auto;
}

.home__site-map__header {
  font-size: 0.8rem;
  font-weight: bold;
}

.home__site-map__item {
  font-size: 0.8rem;
  padding: 10px;
}

.home__site-map__item a:hover {
  color: #3273dc;
}

.home__break-line {
  margin-left: 39.5px;
  margin-right: 39.5px;
  color: #979797;
  background-color: #979797;
  height: 1px;
  border: none;
}

.section__title {
  font-weight: bold;
  font-size: 1rem;
}

.person-sitting-image {
  position: relative;
  right: 135px;
  top: 75px;
}

.person-wave-image {
  position: relative;
  right: -105px;
  top: -26px;
}

.person-parachute-image {
  position: relative;
  right: -105px;
  top: 10px;
}
</style>
