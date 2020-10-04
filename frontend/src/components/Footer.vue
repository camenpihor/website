<template>
  <div class="footer">
    <div class="content has-text-centered">
      <p class="is-size-7">
        Website by <router-link :to="{ name: 'about' }">me</router-link>. The
        <a href="https://github.com/camenpihor/website" target="_blank"
          >source code</a
        >
        is licensed
        <a href="http://opensource.org/licenses/mit-license.php" target="_blank"
          >MIT</a
        >.
      </p>
    </div>
  </div>
</template>

<script>
export default {};
</script>
