<template>
  <div class="navigation">
    <nav
      class="navbar"
      v-bind:class="{
        'is-transparent-2': isTransparent,
        'is-dark': !isTransparent
      }"
    >
      <div class="navbar-brand">
        <router-link :to="{ name: routeHome }" class="navbar-item" tag="li"
          ><span class="navigation__top__route-home">{{
            routeHome
          }}</span></router-link
        >

        <div
          role="button"
          class="navbar-burger burger"
          v-on:click="open = true"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </div>
      </div>

      <div class="navbar-menu">
        <div class="navbar-end">
          <div
            class="navbar-item has-dropdown is-hoverable"
            v-for="(groupRoutes, groupName) in routes"
            :key="groupName"
          >
            <a class="navbar-link is-arrowless">
              {{ groupName }}
            </a>

            <div class="navbar-dropdown is-right">
              <div v-for="route in groupRoutes" :key="route.label">
                <router-link
                  v-if="route.internal"
                  :to="route.to"
                  class="navbar-item"
                  tag="li"
                  >{{ route.label }}
                </router-link>
                <a v-else class="navbar-item" :href="route.to">
                  {{ route.label }}
                </a>
              </div>
            </div>
          </div>
        </div>
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
.navbar {
  height: 3.25rem;
}

.navbar-brand .navbar-item {
  color: white !important;
  cursor: pointer;
}

.navbar-brand .navbar-item:hover {
  background-color: #4f4f52;
}

.navigation__top__route-home {
  font-size: 20px;
  text-transform: capitalize;
  font-weight: bold;
}

.navbar-dropdown .navbar-item:hover {
  background-color: #f5f5f5;
}

.navbar-dropdown .navbar-item {
  cursor: pointer;
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