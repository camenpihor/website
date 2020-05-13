<template>
  <div class="about">
    <img class="about__image" :src="meFilePath" />
    <p class="about__name">Camen</p>
    <p class="about__job">Data Scientist</p>
    <ul class="about__externals">
      <router-link :to="{ name: 'github' }" tag="li" class="about__external"
        ><i class="fab fa-github"
      /></router-link>
      <li class="about__external"><i class="fal fa-file-user" /></li>
      <li class="about__external">
        <div class="about__email">
          <p class="about__email__text">camenrogue[at]</p>
          <p class="about__email__text">gmail[dot]com</p>
        </div>
      </li>
    </ul>
    <img class="person-hot-air-balloon" :src="personHotAirBalloonFilePath" />
    <div class="about__me">
      <div class="section">
        <p class="about__me__header">And here is some stuff about me…</p>
        <p class="about__me__text">
          Space, earth systems, nature, wonder, thinking, speaking. Laudem et
          impetus quo minus id, de homine sensibus reliqui nihil impedit, quo
          ignorare vos arbitrer, sed et dolorum effugiendorum gratia et dolorem?
          sunt autem nusquam hoc epicurus in armatum hostem impetum fecisse aut
          ad respondendum reddidisti quorum facta quem modo ista sis aequitate.
        </p>
      </div>
      <div class="section">
        <p class="about__me__header">And here are some things that I like…</p>
        <p class="about__me__text">
          <span>(I post a lot more recommendations </span>
          <router-link :to="{ name: 'recommendations' }">here</router-link>
          <span>!)</span>
        </p>
        <ul class="about__me__list">
          <li class="about__me__list__header">Blogs</li>
          <ul class="about__me__list__sub">
            <li v-for="blog in blogRoutes" :key="blog.label">
              <a class="about__me__list__item" :href="blog.to">
                {{ blog.label }}
              </a>
            </li>
          </ul>
          <li class="about__me__list__header">Books</li>
          <ul class="about__me__list__sub">
            <li v-for="book in bookRoutes" :key="book.label">
              <a class="about__me__list__item" :href="book.to">
                {{ book.label }}
              </a>
            </li>
          </ul>
        </ul>
      </div>
    </div>
    <img class="person-tree-reading" :src="personTreeReadingFilePath" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      meFilePath: require("@/assets/me.svg"),
      personHotAirBalloonFilePath: require("@/assets/person-hot-air-balloon.svg"),
      personTreeReadingFilePath: require("@/assets/person-tree-reading.svg"),
      blogRoutes: [
        {
          to: "https://slatestarcodex.com/",
          label: "slatestarcodex.com"
        },
        {
          to: "http://mindingourway.com/",
          label: "mindingourway.com"
        },
        {
          to: "https://eukaryotewritesblog.com/",
          label: "eukaryotewritesblog.com"
        },
        {
          to: "https://theunitofcaring.tumblr.com/",
          label: "theunitofcaring.com"
        },
        {
          to: "http://www.bldgblog.com/",
          label: "bldgblog.com"
        }
      ],
      bookRoutes: [
        {
          to: "https://en.wikipedia.org/wiki/The_Way_of_Kings",
          label: "the way of kings by brandon sanderson"
        },
        {
          to: "https://en.wikipedia.org/wiki/The_Fifth_Season_(novel)",
          label: "the fifth season by n.k. jemisin"
        },
        {
          to: "https://wanderinginn.com/",
          label: "the wandering inn by pirateaba"
        },
        {
          to:
            "https://www.goodreads.com/en/book/show/38746152-the-book-of-delights",
          label: "the book of delights by ross gay"
        },
        {
          to:
            "https://www.goodreads.com/book/show/28256439-the-hidden-life-of-trees",
          label: "the hidden life of trees by peter wohlleben"
        }
      ]
    };
  }
};
</script>

<style>
.about {
  margin-top: 60px;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.about__image {
  height: 150px;
  width: 150px;
}

.about__name {
  margin-top: 10px;
  font-weight: bold;
  font-size: 2rem;
}

.about__job {
  font-size: 0.8rem;
  margin-top: -8px;
}

.about__externals {
  margin-top: 35px;
  -webkit-tap-highlight-color: transparent;
}

.about__external {
  padding-right: 20px;
  padding-left: 20px;
  font-size: 3rem;
  display: inline-block;
  cursor: pointer;
}

.about__external i:hover {
  color: #3273dc;
}

.about__email {
  font-size: 0.8rem;
  margin-top: 20px;
  cursor: default;
}

.person-hot-air-balloon {
  position: relative;
  top: 35px;
  left: -9rem;
}

.about__me {
  text-align: left;
}

.about__me__header {
  font-weight: bold;
  color: black;
}

.about__me__text a {
  color: #3273dc;
}

.about__me__text a:hover {
  text-decoration: underline;
}

.about__me__list {
  margin-top: 30px;
}

.about__me__list__header {
  margin-top: 1rem;
}

.about__me__list__sub {
  margin-left: 10px;
}

.about__me__list__item:hover {
  color: #3273dc;
}

.person-tree-reading {
  position: relative;
  bottom: -73px;
  right: -100px;
  z-index: -1;
}
</style>
