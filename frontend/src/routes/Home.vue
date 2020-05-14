<template>
  <div class="home">
    <div v-on:click="isImageModalActive = true">
      <Background class="home__image" :filePath="backgroundFilePath" />
    </div>
    <b-modal full-screen can-cancel :active.sync="isImageModalActive">
      <ForeverBackground :filePath="backgroundFilePath" />
    </b-modal>
    <div class="home__page">
      <LifeIcons class="home__section" />

      <hr class="home__break-line" />

      <div class="home__section">
        <h1 class="home__section__title">
          Hai! I'm Camen :)
          <img class="person-wave-image" :src="personWaveFilePath" />
        </h1>

        <div class="home__section__bio__text">
          <p>
            And this is my short bio. I made this website for these reason, and
            it holds these types sorts of things because I like these sorts of
            things. To read more about me and what I like, check out my About
            page, which will also include a list of blogs and online resources
            that I like to peruse.
          </p>
          <p>
            et aperta iudicari ea voluptate velit esse, quam interrogare aut
            contra sit, amet, consectetur, adipisci velit, sed quia consequuntur
            magni dolores et expedita distinctio nam libero tempore, cum
            memoriter, tum etiam erga nos amice et via.
          </p>
        </div>
      </div>

      <hr class="home__break-line" />

      <div class="home__section home__site-map">
        <h1 class="home__section__title">
          And this is my website<img
            class="person-parachute-image"
            :src="personParachuteFilePath"
          />
        </h1>
        <div class="columns is-mobile">
          <div class="column">
            <h1 class="home__site-map__header">General</h1>
            <ul class="home__site-map__list">
              <li class="home__site-map__item">
                <router-link :to="{ name: 'home' }">Home</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'about' }">About</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'recommendations' }"
                  >Recommendations</router-link
                >
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'github' }">GitHub</router-link>
              </li>
            </ul>
          </div>
          <div class="column">
            <h1 class="home__site-map__header">Projects</h1>
            <ul class="home__site-map__group">
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }">Blog</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }"
                  >Math Implementations</router-link
                >
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }"
                  >Measurements for Humans</router-link
                >
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }"
                  >Nature Identifications</router-link
                >
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }">RogueSky</router-link>
              </li>
              <li class="home__site-map__item">
                <router-link :to="{ name: 'error' }">TreeCount</router-link>
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
      personWaveFilePath: require("@/assets/people/person-wave.svg"),
      personParachuteFilePath: require("@/assets/people/person-parachute.svg"),
      personSittingFilePath: require("@/assets/people/person-sitting.svg"),
      isImageModalActive: false
    };
  }
};
</script>

<style style="scss">
.home {
  padding-top: 0;
}

.section:first-of-type {
  padding-top: 0;
}

.home__image {
  position: absolute;
  top: -60px; /* offset navbar */
  left: 0;
  right: 0;
  margin: 0;
  height: 33vh;
}

.home__page {
  padding-top: calc(
    33vh - (2 * 60px)
  ); /* home__image height - navbar height */
}

.home__section {
  margin-top: 4rem;
  margin-bottom: 4rem;
}

.home__section:first-of-type {
  margin-top: 2.5rem;
  margin-left: -1rem;
  margin-right: -1rem;
}

.home__section__title {
  text-align: center;
  font-weight: bold;
  font-size: 1.2rem;
  margin-bottom: 3rem;
}

.home__break-line {
  margin-left: 39.5px;
  margin-right: 39.5px;
  color: #979797;
  background-color: #979797;
  height: 1px;
  border: none;
}

.home__section__bio__text p {
  margin-top: 1rem;
}

.home__site-map__header {
  font-size: 1rem;
  font-weight: bold;
}

.home__site-map__item {
  font-size: 1rem;
  padding: 10px;
}

.home__site-map__item a:hover {
  color: #3273dc;
}

.person-sitting-image {
  position: relative;
  left: -10rem;
  top: 0.85rem;
}

.person-wave-image {
  position: relative;
  left: 1rem;
  top: 0.3rem;
}

.person-parachute-image {
  position: relative;
  left: 1.5rem;
  top: 1.5rem;
}
</style>
