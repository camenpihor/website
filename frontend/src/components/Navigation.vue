<template>
  <div class="navigation">
    <nav class="navigation__top" v-bind:class="{ transparent: isTransparent }">
      <ul class="navigation__top__left">
        <li class="navigation__top__item">{{ currentRoute }}</li>
      </ul>
      <ul class="navigation__top__right">
        <router-link
          :to="{ name: 'home' }"
          tag="li"
          class="navigation__top__item"
          ><img class="navigation__home-icon" src="camen-logo-icon.svg"
        /></router-link>
        <li class="navigation__top__item">
          <i v-on:click="open = true" class="fal fa-bars"></i>
        </li>
      </ul>
    </nav>

    <b-sidebar type="is-off-white" fullheight overlay right :open.sync="open">
      <b-menu>
        <b-menu-list class="sidebar__header" label="General">
          <b-menu-item
            v-for="route in generalRoutes"
            :key="route.label"
            :to="{ name: route.name }"
            :label="route.label"
            class="sidebar__item"
            tag="router-link"
          />
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="Projects">
          <b-menu-item
            v-for="route in projectRoutes"
            :key="route.label"
            :to="{ name: route.name }"
            :label="route.label"
            class="sidebar__item"
            tag="router-link"
          />
        </b-menu-list>
        <b-menu-list label="Blog Roll">
          <b-menu-item
            v-for="route in blogRoutes"
            :key="route.label"
            :href="route.to"
            :label="route.label"
            class="sidebar__item"
            tag="a"
          />
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="YouTube">
          <b-menu-item
            v-for="route in youtubeRoutes"
            :key="route.label"
            :href="route.to"
            :label="route.label"
            class="sidebar__item"
            tag="a"
          />
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="Web Fiction">
          <b-menu-item
            v-for="route in webfictionRoutes"
            :key="route.label"
            :href="route.to"
            :label="route.label"
            class="sidebar__item"
            tag="a"
          />
        </b-menu-list>
      </b-menu>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      open: false,
      isTransparent: false,
      currentRoute: this.$route.name,
      generalRoutes: [
        {
          name: "home",
          label: "Home"
        },
        {
          name: "about",
          label: "About"
        },
        {
          name: "error",
          label: "Recommendations"
        },
        {
          name: "error",
          label: "GitHub"
        }
      ],
      projectRoutes: [
        {
          name: "error",
          label: "Blog"
        },
        {
          name: "error",
          label: "Math Implementations"
        },
        {
          name: "error",
          label: "Measurements for Humans"
        },
        {
          name: "error",
          label: "Nature Identification"
        },
        {
          name: "error",
          label: "RogueSky"
        },
        {
          name: "error",
          label: "TreeCount"
        }
      ],
      blogRoutes: [
        {
          to: "https://slatestarcodex.com/",
          label: "SlateStarCodex"
        },
        {
          to: "http://mindingourway.com/",
          label: "Minding Our Way"
        },
        {
          to: "https://eukaryotewritesblog.com/",
          label: "EukaryoteWritesBlog"
        },
        {
          to: "https://www.lesswrong.com/",
          label: "LessWrong"
        },
        {
          to: "https://theunitofcaring.tumblr.com/",
          label: "The Unit of Caring"
        },
        {
          to: "http://www.bldgblog.com/",
          label: "BLDGBLOG"
        }
      ],
      youtubeRoutes: [
        {
          to: "https://www.youtube.com/user/vlogbrothers",
          label: "VlogBrothers"
        },
        {
          to: "https://www.youtube.com/user/minuteearth",
          label: "MinuteEarth"
        },
        {
          to: "https://www.youtube.com/channel/UC3KEoMzNz8eYnwBC34RaKCQ",
          label: "Simone Giertz"
        },
        {
          to: "https://www.youtube.com/user/CGPGrey",
          label: "CGP Grey"
        },
        {
          to: "https://www.youtube.com/channel/UCHsRtomD4twRf5WVHHk-cMw",
          label: "TierZoo"
        },
        {
          to: "https://www.youtube.com/user/thebrainscoop",
          label: "TheBrainScoop"
        },
        {
          to:
            "https://www.youtube.com/watch?v=0rHUDWjR5gg&list=PL8dPuuaLjXtPAJr1ysd5yGIyiSFuh0mIL",
          label: "Crash Course - Astronomy"
        },
        {
          to: "https://www.youtube.com/user/alectheblacksmith",
          label: "Alec Steele"
        }
      ],
      webfictionRoutes: [
        {
          to: "https://slatestarcodex.com/",
          label: "A Practical Guide to Evil"
        },
        {
          to: "http://mindingourway.com/",
          label: "The Wandering Inn"
        },
        {
          to: "https://eukaryotewritesblog.com/",
          label: "Harry Potter and the Methods of Rationality"
        }
      ]
    };
  },
  methods: {
    initialize: function() {
      let transparentRoutes = ["home"];
      let currentRoute = this.$route.name;

      this.open = false;
      this.currentRoute = currentRoute;

      if (transparentRoutes.includes(currentRoute)) {
        this.isTransparent = true;
      } else {
        this.isTransparent = false;
      }
    }
  },
  watch: {
    $route(to, from) {
      if (to !== from) {
        this.initialize();
      }
    }
  },
  mounted() {
    this.initialize();
  }
};
</script>
<style>
.navigation__top {
  background-color: #5b5b5f;
  color: white;
  position: relative;
  height: 60px;
  padding-left: 10px;
  padding-right: 10px;
  z-index: 30;
}

.transparent {
  background-color: transparent;
  color: white;
}

.navigation__top__left {
  float: left;
  list-style-type: none;
}

.navigation__top__right {
  float: right;
  list-style-type: none;
}

.navigation__top__item {
  color: white;
  float: left;
  font-size: 25px;
  padding: 12px;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.navigation__top__item:hover {
  background-color: rgba(128, 128, 128, 0.521);
}

.navigation__home-icon {
  height: 18px;
  width: 24px;
}

.sidebar__item {
  font-size: 1rem;
  color: black;
}

/* buefy class */
.sidebar-content {
  padding: 32px;
  transition: ease-in-out 0.5s !important;
}

.sidebar-content p {
  font-weight: bold;
  text-transform: none;
  font-size: 18px;
  color: #000000;
}
</style>