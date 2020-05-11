<template>
  <div class="navigation">
    <nav class="navigation__top">
      <ul class="navigation__top__right">
        <li class="navigation__top__item">
          <a><img class="navigation__home-icon" src="camen-logo-icon.svg"/></a>
        </li>
        <li class="navigation__top__item">
          <i v-on:click="open = true" class="fal fa-bars"></i>
        </li>
      </ul>
    </nav>

    <b-sidebar type="is-off-white" fullheight overlay right :open.sync="open">
      <b-menu>
        <b-menu-list class="sidebar__header" label="General">
          <b-menu-item class="sidebar__item" label="Home"></b-menu-item>
          <b-menu-item class="sidebar__item" label="About"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Recommendations"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="GitHub"></b-menu-item>
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="Projects">
          <b-menu-item class="sidebar__item" label="Blog"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Math Implementations"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Measurements for Humans"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Nature Identifications"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="RogueSky"></b-menu-item>
          <b-menu-item class="sidebar__item" label="TreeCount"></b-menu-item>
        </b-menu-list>
        <b-menu-list label="Blog Roll">
          <b-menu-item
            class="sidebar__item"
            label="SlateStarCodex"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Minding Our Way"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="EukaryoteWritesBlog"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="LessWrong"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="The Unit of Caring"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="BLDGBLOG"></b-menu-item>
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="YouTube">
          <b-menu-item class="sidebar__item" label="Vlogbrothers"></b-menu-item>
          <b-menu-item class="sidebar__item" label="MintueEarth"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Simone Giertz"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="CGP Grey"></b-menu-item>
          <b-menu-item class="sidebar__item" label="TierZoo"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="TheBrainScoop"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Crash Course Astronomy"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="Alec Steele"></b-menu-item>
        </b-menu-list>
        <b-menu-list class="sidebar__header" label="Web Fiction">
          <b-menu-item class="sidebar__item" label="Worm"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="A Practical Guide to Evil"
          ></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="The Wandering Inn"
          ></b-menu-item>
          <b-menu-item class="sidebar__item" label="Unsong"></b-menu-item>
          <b-menu-item
            class="sidebar__item"
            label="Harry Potter and the Methods of Rationality"
          ></b-menu-item>
        </b-menu-list>
      </b-menu>
    </b-sidebar>
  </div>
</template>

<script>
export default {
  props: ["transparent"],
  data() {
    return {
      open: false
    };
  }
};
</script>
<style>
.navigation__top {
  background-color: transparent;
  position: relative;
  height: 60px;
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  z-index: 30;
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

.navigation__home-icon {
  color: white;
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