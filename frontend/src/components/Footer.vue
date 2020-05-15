<template>
  <div class="footer-custom">
    <div class="footer-left">
      Camen © 2020
    </div>
    <div class="footer-right">
      Powered and publised by me
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.footer-custom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 2.5rem;
  background-color: #5b5b5f;
  color: black;
  font-size: 0.6rem;
  display: flex;
  z-index: 10;
}

.footer-left {
  margin: auto;
  display: flex;
  width: 50%;
  justify-content: center;
}

.footer-right {
  display: flex;
  margin: auto;
  width: 50%;
  justify-content: center;
}
</style>
