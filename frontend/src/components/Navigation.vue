<template>
  <div class="navigation">
    <nav class="navigation__top" v-bind:class="{ transparent: isTransparent }">
      <div class="navigation__top__wrapper">
        <ul v-if="currentRoute !== 'home'" class="navigation__top__left">
          <router-link
            class="navigation__top__item"
            tag="li"
            :to="{ name: routeHome }"
            ><span class="navigation__top__route-home">{{
              routeHome
            }}</span></router-link
          >
        </ul>
        <ul class="navigation__top__right">
          <router-link
            :to="{ name: 'home' }"
            tag="li"
            class="navigation__top__item"
            ><img class="navigation__home-icon" :src="siteIconFilePath"
          /></router-link>
          <li class="navigation__top__item" v-on:click="open = true">
            <i class="fal fa-bars"></i>
          </li>
        </ul>
      </div>
    </nav>

    <b-sidebar type="is-off-white" fullheight overlay right :open.sync="open">
      <b-menu>
        <b-menu-list
          v-for="(groupRoutes, groupName) in routes"
          :key="groupName"
          :label="groupName"
        >
          <div v-for="route in groupRoutes" :key="route.label">
            <b-menu-item
              v-if="route.internal"
              v-on:click="initialize()"
              :label="route.label"
              :to="route.to"
              tag="router-link"
            />
            <b-menu-item
              v-else
              v-on:click="initialize()"
              :label="route.label"
              :href="route.to"
              tag="a"
            />
          </div>
        </b-menu-list>
      </b-menu>
    </b-sidebar>
  </div>
</template>

<script>
import routeJson from "@/assets/routes.json";

export default {
  data() {
    return {
      open: false,
      isTransparent: false,
      routeHome: this.$route.meta.pageHome,
      currentRoute: this.$route.name,
      routes: routeJson,
      siteIconFilePath: require("@/assets/icons/site-icon.svg")
    };
  },
  methods: {
    initialize: function() {
      let transparentRoutes = ["home"];
      let currentRoute = this.$route.name;

      this.open = false;
      this.routeHome = this.$route.meta.pageHome;
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
  z-index: 10;
}

.navigation__top__wrapper {
  max-width: 800px;
  margin: auto;
}

.transparent {
  background-color: transparent;
  color: white;
}

.navigation__top__left {
  float: left;
  list-style-type: none;
}

.navigation__top__route-home {
  font-size: 20px;
  text-transform: capitalize;
  font-weight: bold;
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
  border-radius: 18px;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

@media (hover: hover) and (pointer: fine) {
  .navigation__top__item:hover {
    background-color: rgba(128, 128, 128, 0.521);
  }
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
  text-transform: capitalize;
  font-size: 18px;
  color: #000000;
}

.sidebar-content a {
  color: inherit !important;
}
</style>