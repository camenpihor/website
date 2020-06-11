<template>
  <div class="navigation">
    <EventListener :eventType="'scroll'" :method="onScroll" />
    <nav
      class="navbar"
      v-bind:class="{
        'is-transparent': isTransparent,
        'is-dark': !isTransparent,
        navbar__hidden: !showTopBar
      }"
    >
      <div class="navbar-brand">
        <div
          class="is-hidden-desktop navbar-item navigation__top__route-home"
          v-if="!isTransparent"
        >
          {{ formatName(routeHome) }}
        </div>

        <div
          role="button"
          class="navbar-burger burger"
          v-on:click="showSideBar = true"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </div>
      </div>

      <div class="navbar-menu">
        <div class="navbar-end">
          <router-link :to="{ name: 'home' }" class="navbar-item"
            >home
          </router-link>
          <router-link :to="{ name: 'about' }" class="navbar-item"
            >about
          </router-link>
          <router-link :to="{ name: 'recommendations' }" class="navbar-item"
            >recommendations
          </router-link>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link is-arrowless">
              projects
            </a>

            <div class="navbar-dropdown is-right">
              <router-link
                v-for="route in routes.projects"
                :key="route.label"
                :to="route.to"
                class="navbar-item"
                tag="li"
                >{{ route.label }}
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <b-sidebar
      type="is-off-white"
      fullheight
      overlay
      right
      :open.sync="showSideBar"
    >
      <b-menu>
        <b-menu-list
          v-for="(groupRoutes, groupName) in routes"
          :key="groupName"
        >
          <p class="heading  has-text-weight-bold is-size-6">
            {{ groupName }}
          </p>
          <div v-for="route in groupRoutes" :key="route.label">
            <b-menu-item
              v-if="route.internal"
              v-on:click="initialize()"
              :label="route.label"
              :to="route.to"
              tag="router-link"
            />
          </div>
        </b-menu-list>
      </b-menu>
    </b-sidebar>
  </div>
</template>

<script>
import EventListener from "@/components/EventListener.vue";

import routeJson from "@/assets/json/routes.json";

export default {
  components: {
    EventListener
  },
  data() {
    return {
      showTopBar: true,
      showSideBar: false,
      originallyTransparent: false,
      isTransparent: false,
      routeHome: this.$route.meta.pageHome,
      currentRoute: this.$route.name,
      routes: routeJson,
      siteIconFilePath: require("@/assets/icons/site-icon.svg"),
      lastScrollPosition: 0
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
        this.originallyTransparent = true;
        this.isTransparent = true;
      }
    },
    formatName: function(name) {
      if (name != null) {
        return name
          .toLowerCase()
          .split("-")
          .map(s => s.charAt(0).toUpperCase() + s.substring(1))
          .join("");
      }
    },
    onScroll: function() {
      let currentScrollPosition =
        window.pageYOffset || document.documentElement.scrollTop;

      if (currentScrollPosition < 0) {
        return;
      }

      if (Math.abs(currentScrollPosition - this.lastScrollPosition) < 60) {
        return;
      }
      if (this.originallyTransparent) {
        if (currentScrollPosition > 150) {
          this.isTransparent = false;
        } else {
          this.isTransparent = true;
        }
      }
      this.showTopBar = currentScrollPosition < this.lastScrollPosition;
      this.lastScrollPosition = currentScrollPosition;
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
.navigation .navbar {
  width: 100%;
  position: fixed;
  transform: translate3d(0, 0, 0);
  transition: 0.3s all ease-out;
}

.navigation .navbar.navbar__hidden {
  transform: translate3d(0, -100%, 0);
}

.navigation__top__route-home {
  color: white;
}

@media only screen and (min-width: 1024px) {
  .navigation .navbar {
    padding-left: 15rem;
    padding-right: 15rem;
  }
}

li.navbar-item {
  cursor: pointer;
}

.navigation__top__route-home {
  font-size: 20px;
  text-transform: capitalize;
  font-weight: bold;
}

.navbar-dropdown .navbar-item:hover {
  background-color: #f5f5f5;
}

/* buefy class */
.menu-list {
  margin: 3rem 1.5rem;
}

.menu-list a:hover {
  color: black !important;
}

.sidebar-content {
  transition-duration: 0.4s !important;
}

.sidebar-content a {
  color: hsl(0, 0%, 35%) !important;
  padding: 0.75rem !important;
}

.navbar.is-transparent a {
  color: rgb(168, 168, 168) !important;
}

.navbar.is-transparent a:hover {
  color: white !important;
}

.navbar.is-transparent .navbar-burger {
  color: rgb(168, 168, 168) !important;
}
.navbar.is-transparent .navbar-burger:hover {
  color: white !important;
}

.navbar.is-transparent a:hover {
  color: white !important;
}
</style>