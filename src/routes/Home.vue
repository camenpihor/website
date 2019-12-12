<template>
  <section class="hero is-large has-background-image">
    <div class="hero-body"></div>
  </section>
</template>

<style>
.has-background-image {
  background-image: url("../assets/space.jpg");
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-color: #999;
}

.title {
  font-size: 300%;
  color: rgba(170, 170, 170, 0.575);
}

.has-background-image .navbar {
  display: none;
}
</style>