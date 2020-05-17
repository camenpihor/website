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
        <router-link
          v-if="!isTransparent"
          :to="{ name: routeHome }"
          class="navbar-item"
          tag="li"
          ><span class="navigation__top__route-home">{{
            formatName(routeHome)
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
          <router-link :to="{ name: 'home' }" class="navbar-item" tag="li"
            >home
          </router-link>
          <router-link :to="{ name: 'about' }" class="navbar-item" tag="li"
            >about
          </router-link>
          <router-link
            :to="{ name: 'recommendations' }"
            class="navbar-item"
            tag="li"
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
                tag="li"
                class="navbar-item"
                >{{ route.label }}
              </router-link>
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
              class="sidebar__item"
              v-on:click="initialize()"
              :label="route.label"
              :to="route.to"
              tag="router-link"
            />
            <b-menu-item
              v-else
              class="sidebar__item"
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
    },
    formatName: function(name) {
      if (name != null) {
        return name
          .toLowerCase()
          .split("-")
          .map(s => s.charAt(0).toUpperCase() + s.substring(1))
          .join("");
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

@media only screen and (min-width: 1023px) {
  .navbar {
    padding-left: 15rem;
    padding-right: 15rem;
  }
}

li.navbar-item:hover {
  background-color: #4f4f52;
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
  padding: 0.75rem !important
}

.sidebar__item:hover {
  color: #3273dc;
}
</style>