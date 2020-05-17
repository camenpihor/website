<template>
  <div class="about">
    <div class="about__wrapper">
      <div class="about__intro">
        <img class="about__image" :src="meFilePath" />
        <p class="about__name">Camen</p>
        <p class="about__job">Data Scientist</p>
        <ul class="about__externals">
          <router-link
            :to="{ name: 'github' }"
            tag="li"
            class="about__external"
          >
            <img :src="githubIconFilePath" class="about__icon"
          /></router-link>
          <li class="about__external">
            <a href="camen_piho_resume.pdf" target="_blank"
              ><img :src="resumeIconFilePath" class="about__icon"
            /></a>
          </li>
          <li class="about__external">
            <a href="mailto:camenrogue@gmail.com">
              <img :src="emailIconFilePath" class="about__icon" />
            </a>
          </li>
        </ul>
      </div>
      <img class="person-hot-air-balloon" :src="personHotAirBalloonFilePath" />
      <div class="about__me">
        <div class="about__me__section">
          <p class="about__me__header">And here is some stuff about me…</p>
          <p class="about__me__text">
            Space, earth systems, nature, wonder, thinking, speaking. Laudem et
            impetus quo minus id, de homine sensibus reliqui nihil impedit, quo
            ignorare vos arbitrer, sed et dolorum effugiendorum gratia et
            dolorem? sunt autem nusquam hoc epicurus in armatum hostem impetum
            fecisse aut ad respondendum reddidisti quorum facta quem modo ista
            sis aequitate.
          </p>
        </div>
        <div class="about__me__section">
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
    </div>
    <img class="person-tree-reading" :src="personTreeReadingFilePath" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      meFilePath: require("@/assets/me.svg"),
      personHotAirBalloonFilePath: require("@/assets/people/person-hot-air-balloon.svg"),
      personTreeReadingFilePath: require("@/assets/people/person-tree-reading.svg"),
      resumeIconFilePath: require("@/assets/icons/resume-icon.svg"),
      githubIconFilePath: require("@/assets/icons/github-icon.svg"),
      emailIconFilePath: require("@/assets/icons/email-icon.svg"),
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
.about__wrapper {
  padding-bottom: 1rem;
}

.about__intro {
  text-align: center;
}

.about__image {
  height: 10rem;
  width: 10rem;
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
}

.about__external {
  display: inline-block;
  cursor: pointer;
  margin-right: 0.5rem;
  margin-left: 0.5rem;
}

.about__icon {
  height: 3rem;
  width: 3rem;
}

.about__icon:hover {
  background-color: rgba(165, 159, 159, 0.199);
  border-radius: 6px;
}

.person-hot-air-balloon {
  position: relative;
  top: 0;
  left: -2rem;
}

.about__me {
  text-align: left;
}

.about__me__section {
  margin-top: 3.75rem;
}

.about__me__section:first-of-type {
  margin-top: 0;
}

.about__me__header {
  font-weight: bold;
  color: black;
}

.about__me__text a {
  color: #3273dc;
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

.person-tree-reading {
  position: absolute;
  bottom: 2.3rem; /* height of footer - a smidgeon */
  right: 2rem;
  z-index: -1;
}
</style>
