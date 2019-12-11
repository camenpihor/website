<template>
  <section id="footer">
    <div class="container">
      <div id="footer-info" class="columns is-centered">
          <aside class="menu column">
            <p class="menu-label">Website of Camen Piho</p>
            <ul class="menu-list">
              <li><router-link :to="{ name: 'about' }">About</router-link></li>
              <li><a href="https://github.com/camenpihor">GitHub</a></li>
            </ul>
          </aside>
          <aside class="menu column">
            <p class="menu-label">General</p>
            <ul class="menu-list">
              <li><router-link :to="{ name: 'home' }">Home</router-link></li>
              <li><router-link :to="{ name: 'documentation' }">Documentation</router-link></li>
            </ul>
          </aside>
          <aside class="menu column">
            <p class="menu-label">Projects</p>
            <ul class="menu-list">
              <li>
                <router-link :to="{ name: '404' }">Thoughts</router-link>
              </li>
              <li>
                <router-link :to="{ name: '404' }">Books</router-link>
              </li>
              <li>
                <router-link :to="{ name: 'rogue-sky-home' }">RogueSky</router-link>
              </li>
              <li>
                <router-link :to="{ name: '404' }">TreeCount</router-link>
              </li>
            </ul>
          </aside>
      </div>
    </div>
  </section>
</template>

<style>
#footer {
  background: #343434;
  color: #aaa;
}

#footer-info {
  padding-top: 50px;
  padding-bottom: 50px;
}

#footer-info .column {
  border: white 1px;
}

#footer-info .menu-list a {
    color: #4a4a4a;
}

#footer-info .menu-list a:hover {
    background-color: transparent;
    color: white;
}
</style>
