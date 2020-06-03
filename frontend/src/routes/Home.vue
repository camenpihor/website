<template>
  <section class="home">
    <Background class="home__image" :filePath="backgroundFilePath" />
    <div class="home__text">
      <div class="section">
        <h1 class="title is-4 has-text-centered is-relative">
          Hai! I'm Camen :)
          <img class="person-wave" :src="personWaveFilePath" />
        </h1>

        <p class="subsection">
          And this is my short bio. I made this website for these reason, and it
          holds these types sorts of things because I like these sorts of
          things. To read more about me and what I like, check out my About
          page, which will also include a list of blogs and online resources
          that I like to peruse.
        </p>
        <p class="subsection">
          et aperta iudicari ea voluptate velit esse, quam interrogare aut
          contra sit, amet, consectetur, adipisci velit, sed quia consequuntur
          magni dolores et expedita distinctio nam libero tempore, cum
          memoriter, tum etiam erga nos amice et via.
        </p>
      </div>

      <hr />

      <div class="section">
        <h1 class="title is-4 has-text-centered">
          And these are my projects
        </h1>

        <div class="subsection">
          <router-link :to="{ name: 'blog' }">
            <span class="is-size-5 has-text-weight-bold">Blog</span>
          </router-link>
          <p class="subtitle is-6">
            et aperta iudicari ea voluptate velit esse, quam interrogare aut
            contra sit, amet, consectetur, adipisci velit
          </p>
        </div>
        <div class="subsection">
          <router-link :to="{ name: 'math' }">
            <span class="is-size-5 has-text-weight-bold"
              >Math Implementations</span
            >
          </router-link>
          <p class="subtitle is-6">
            et aperta iudicari ea voluptate velit esse, quam interrogare aut
            contra sit, amet, consectetur, adipisci velit
          </p>
        </div>
        <div class="subsection">
          <router-link :to="{ name: 'nature' }">
            <span class="is-size-5 has-text-weight-bold"
              >Nature Identification</span
            >
          </router-link>
          <p class="subtitle is-6">
            et aperta iudicari ea voluptate velit esse, quam interrogare aut
            contra sit, amet, consectetur, adipisci velit
          </p>
        </div>
        <div class="subsection">
          <router-link :to="{ name: 'rogue-sky' }">
            <span class="is-size-5 has-text-weight-bold">RogueSky</span>
          </router-link>
          <p class="subtitle is-6">
            et aperta iudicari ea voluptate velit esse, quam interrogare aut
            contra sit, amet, consectetur, adipisci velit
          </p>
        </div>
      </div>

      <hr />

      <div class="section">
        <div class="is-relative">
          <img class="person-parachute" :src="personParachuteFilePath" />
        </div>
        <h1 class="title is-4 has-text-centered">
          And this is my website
        </h1>
        <ul
          class="subsection has-text-centered"
          v-for="group in siteMapGroups"
          :key="group.groupLabel"
        >
          <p class="heading is-size-7">{{ group.groupLabel }}</p>
          <li v-for="route in group.routes" :key="route.label">
            <router-link :to="route.to">{{ route.label }}</router-link>
          </li>
        </ul>
      </div>
    </div>
    <img class="person-sitting" :src="personSittingFilePath" />
  </section>
</template>

<script>
import Background from "@/components/Background.vue";

import routeJson from "@/assets/json/routes.json";

export default {
  name: "home",
  components: {
    Background
  },
  data() {
    return {
      backgroundFilePath: require("@/assets/space.jpg"),
      personWaveFilePath: require("@/assets/people/person-wave.svg"),
      personParachuteFilePath: require("@/assets/people/person-parachute.svg"),
      personSittingFilePath: require("@/assets/people/person-sitting.svg"),
      isImageModalActive: false,
      siteMapGroups: [
        {
          groupLabel: "General",
          routes: routeJson.general
        },
        {
          groupLabel: "Projects",
          routes: routeJson.projects
        }
      ]
    };
  }
};
</script>

<style style="scss">
.home__image {
  position: absolute;
  top: -3.25rem; /*  offset navbar */
  left: 0;
  right: 0;
  height: 33vh;
}

.home__text {
  margin-top: 20vh;
}

.person-wave {
  position: absolute;
  margin-left: 1rem;
  top: 0.3rem;
}

.person-parachute {
  position: absolute;
  left: 1.5rem;
  top: -3.5rem;
}

.person-sitting {
  position: absolute;
  left: 10vw;
  bottom: calc(1rem + 4rem + 5rem - 0.3rem);
  /* footer fontsize + footer top padding + footer bottom padding - a smidgeon */
}
</style>
