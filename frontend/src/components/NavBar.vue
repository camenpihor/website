<template>
  <div>
    <nav class="navbar-custom">
      <ul class="navbar-right">
        <li class="navbar-custom-item">
          <a><img src="camen-logo-icon.svg" class="home-icon"/></a>
        </li>
        <li class="navbar-custom-item">
          <i v-on:click="open = true" class="fal fa-bars"></i>
        </li>
      </ul>
    </nav>

    <b-sidebar type="is-off-white" fullheight overlay right :open.sync="open">
      <div class="sidebar">
        <b-menu>
          <b-menu-list label="General">
            <b-menu-item class="menu-list-item" label="Home"></b-menu-item>
            <b-menu-item class="menu-list-item" label="About"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Recommendations"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="GitHub"></b-menu-item>
          </b-menu-list>
          <b-menu-list label="Projects">
            <b-menu-item class="menu-list-item" label="Blog"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Math Implementations"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Measurements for Humans"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Nature Identifications"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="RogueSky"></b-menu-item>
            <b-menu-item class="menu-list-item" label="TreeCount"></b-menu-item>
          </b-menu-list>
          <b-menu-list label="Blog Roll">
            <b-menu-item
              class="menu-list-item"
              label="SlateStarCodex"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Minding Our Way"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="EukaryoteWritesBlog"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="LessWrong"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="The Unit of Caring"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="BLDGBLOG"></b-menu-item>
          </b-menu-list>
          <b-menu-list label="YouTube">
            <b-menu-item
              class="menu-list-item"
              label="Vlogbrothers"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="MintueEarth"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Simone Giertz"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="CGP Grey"></b-menu-item>
            <b-menu-item class="menu-list-item" label="TierZoo"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="TheBrainScoop"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Crash Course Astronomy"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Alec Steele"
            ></b-menu-item>
          </b-menu-list>
          <b-menu-list label="Web Fiction">
            <b-menu-item class="menu-list-item" label="Worm"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="A Practical Guide to Evil"
            ></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="The Wandering Inn"
            ></b-menu-item>
            <b-menu-item class="menu-list-item" label="Unsong"></b-menu-item>
            <b-menu-item
              class="menu-list-item"
              label="Harry Potter and the Methods of Rationality"
            ></b-menu-item>
          </b-menu-list>
        </b-menu>
      </div>
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
.navbar-custom {
  background-color: transparent;
  position: relative;
  height: 60px;
  padding-left: 10px;
  padding-right: 10px;
  color: white;
  z-index: 30;
}

.navbar-right {
  float: right;
  list-style-type: none;
}

.navbar-custom-item {
  color: white;
  float: left;
  font-size: 25px;
  padding: 12px;
}

.home-icon {
  color: white;
  height: 18px;
  width: 24px;
}

.sidebar {
  padding: 32px;
}

.menu-label {
  font-weight: bold;
  text-transform: none;
  font-size: 18px;
  color: #000000;
}

.menu-list-item {
  font-size: 16px;
  color: black;
}
</style>