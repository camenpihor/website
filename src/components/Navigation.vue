<template>
  <b-navbar type="is-primary" wrapper-class="container" transparent>
    <template slot="brand">
      <b-navbar-item tag="router-link" :to="{ name: 'home'}">Camen Piho</b-navbar-item>
    </template>
    <template slot="end">
      <b-navbar-dropdown label="Projects">
        <b-navbar-item href="#">Thoughts</b-navbar-item>
        <b-navbar-item href="#">Books</b-navbar-item>
        <b-navbar-item tag="router-link" :to="{ name: 'rogue-sky-home'}">RogueSky</b-navbar-item>
        <b-navbar-item href="#">TreeCount</b-navbar-item>
      </b-navbar-dropdown>
      <b-navbar-item tag="router-link" :to="{ name: 'documentation'}">Documentation</b-navbar-item>
    </template>
  </b-navbar>
</template>

<style>
.navbar-brand a {
  font-weight: bold;
}

a.navbar-item:hover {
  color: #002505 !important;
}

a.navbar-link:hover {
  color: #002505 !important;
}
</style>