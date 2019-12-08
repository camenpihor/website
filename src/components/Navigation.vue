<template>
  <b-navbar type="is-primary" wrapper-class="container" transparent>
    <template slot="brand">
      <b-navbar-item href="/">Camen Piho</b-navbar-item>
    </template>
    <template slot="end">
      <b-navbar-dropdown label="Projects" hoverable>
        <b-navbar-item href="#">Thoughts</b-navbar-item>
        <b-navbar-item href="#">Books</b-navbar-item>
        <b-navbar-item href="rogue-sky">RogueSky</b-navbar-item>
        <b-navbar-item href="#">TreeCount</b-navbar-item>
      </b-navbar-dropdown>
      <b-navbar-item href="#">Home</b-navbar-item>
      <b-navbar-item href="#">Documentation</b-navbar-item>
    </template>
  </b-navbar>
</template>

<style >
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