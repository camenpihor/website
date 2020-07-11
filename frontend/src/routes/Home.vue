<template>
  <section class="home">
    <div class="home__image__wrapper">
      <Background class="home__image" :filePath="backgroundFilePath" />
    </div>
    <img class="person-wave" :src="personWaveFilePath" />
    <div class="section">
      <h1 class="title is-2 has-text-centered is-relative">
        Hai! I’m Camen :)
      </h1>

      <div class="subsection">
        <h1 class="title is-4 has-text-centered">
          And this is a little about me
        </h1>
        <div class="content">
          <p>
            I’m a recently unemployed data scientist in my late 20s, who is
            taking some time to amble. My roaming is currently taking me to the
            stars, trees, birds, and the clouds, but I’m not too sure where I’ll
            end up. I like to think that I am a good Bayesian, but I also like
            seeking wonder which makes me want to talk about the world in
            different ways.
          </p>
          <p>
            I made this site as a collection for my amblings. Here, you’ll find
            some thoughts of mine, some projects, and some of the things that I
            enjoy. I try to link to as many things that I can, in order to
            spread my objectively good tastes.
          </p>
          <p>
            Anyways, if you’ve found this page, I hope that you enjoy it. If you
            feel like you want to, feel free to send me an email (<span
              class="is-size-7"
              >camen[dot]rogue[at]gmail[dot]com</span
            >) with a question! I like talking about most things for a short
            while, but I can talk forever about physics, statistics, astronomy,
            ecology, fantasy, and science fiction. I may even have a fun fact or
            two to share :)
          </p>
        </div>
      </div>
    </div>

    <hr />

    <div class="section">
      <div class="is-relative">
        <img class="person-parachute" :src="personParachuteFilePath" />
      </div>
      <h1 class="title is-4 has-text-centered">
        These are my projects
      </h1>

      <div class="subsection">
        <router-link :to="{ name: 'blog' }">
          <span class="is-size-5 has-text-weight-bold">Blog</span>
        </router-link>
        <p class="subtitle is-6">
          Just a space for my thoughts on things. Probably mostly on topics that
          I find interesting or wondrous, and probably not much on current
          events. I write some long-form entries on particular topics, and also
          <router-link
            :to="{
              name: 'blog-post',
              params: { id: 'introducing-nature-and-links' }
            }"
          >
            two series on nature and interesting links </router-link
          >.
        </p>
      </div>
      <div class="subsection">
        <router-link :to="{ name: 'math' }">
          <span class="is-size-5 has-text-weight-bold"
            >Math Implementations</span
          >
        </router-link>
        <p class="subtitle is-6">
          Every once in a while, I try to see how much I understand a math or
          stats topic by trying to implement something.
        </p>
      </div>
      <div class="subsection">
        <router-link :to="{ name: 'nature' }">
          <span class="is-size-5 has-text-weight-bold"
            >Nature Identification</span
          >
        </router-link>
        <p class="subtitle is-6">
          I used to find it really hard not to be trapped inside my own brain
          while walking through the natual world. So, I tried just being able to
          name the things I was seeing, and I actually found this incredibly
          enriching to my day-to-day. This is a place to gather the names I’ve
          learned and the things that make of the places I’ve been.
        </p>
      </div>
      <div class="subsection">
        <router-link :to="{ name: 'rogue-sky' }">
          <span class="is-size-5 has-text-weight-bold">RogueSky</span>
        </router-link>
        <p class="subtitle is-6">
          One of the places to where I can constantly go to feel wonder is the
          sky. Albeit not incredibly surprising, it took me a long while to
          learn this about myself. To aid my ability to look up, I created a
          forecast of star visibility over the short-term, and a collection of
          astronomical events over the long-term.
        </p>
      </div>
    </div>

    <hr />

    <div class="section">
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

<style>
.home__image__wrapper {
  margin-top: -3.25rem; /* amound of top padding on .route-view */
  height: 33vh; /* height of .home__image */
}

.home__image {
  position: absolute;
  left: 0;
  right: 0;
  height: 33vh;
}

.person-wave {
  position: absolute;
  width: 0.8rem;
  float: right;
  left: 10vw;
  top: 15vh;
}

.person-parachute {
  position: absolute;
  width: 2.5rem;
  left: 1.5rem;
  top: -3.5rem;
}

.person-sitting {
  width: 1rem;
  position: absolute;
  left: 10vw;
  /* footer fontsize + footer top padding + footer bottom padding - a smidgeon */
  bottom: calc(1rem + 4rem + 5rem - 0.5rem);
}
</style>
