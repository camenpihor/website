<template>
  <section class="about">
    <div class="section has-text-centered">
      <img class="about__image" :src="meFilePath" />
      <p class="title is-3">Camen</p>
      <p class="subtitle is-5">Data Scientist</p>
      <ul class="about__externals">
        <router-link :to="{ name: 'github' }" tag="li" class="about__external">
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

    <div class="is-relative">
      <img class="person-hot-air-balloon" :src="personHotAirBalloonFilePath" />
    </div>
    <div class="section">
      <p class="title is-5">And here is some stuff about me…</p>
      <div class="content">
        <p>
          Hai! My background is in math, physics, and greek classics. My
          foreground is in... well, I’m not sure yet. I currently really enjoy
          learning about the natural world, atmospheric physics, and astronomy.
          I think the kindest things I can say about myself are that I actively
          seek wonder and laughter.
        </p>
        <p>
          Every now and then, I get really excited about a topic, and then do a
          bunch of research. This website started out as a way to collect these thoughts.
        </p>
        <p>
          Like most people, I would describe myself as being really bad at describing
          myself, so instead of a longer narrative, I’m going to just list fun
          facts about me. Maybe one day I’ll get better at it...
        </p>
        <div class="has-text-centered section">
          <p class="button is-marginless" v-on:click="setRandomFacts()">
            Random Facts
          </p>
          <div class="subsection">
            <p v-for="(fact, idx) in randomFacts" :key="idx">
              {{ fact }}
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="section about__recommendations">
      <p class="title is-5">And here are some things that I like…</p>
      <p class="subtitle is-7">
        <span>(I post a lot more recommendations </span>
        <router-link :to="{ name: 'recommendations' }" class="hyper-link"
          >here</router-link
        >
        <span>!)</span>
      </p>
      <div>
        <p class="heading is-size-7">Blogs</p>
        <ul class="about__me__list__sub">
          <li v-for="blog in blogRoutes" :key="blog.label">
            <a :href="blog.to">
              {{ blog.label }}
            </a>
          </li>
        </ul>
      </div>
      <div class="subsection">
        <p class="heading is-size-7">Books</p>
        <ul class="about__me__list__sub">
          <li v-for="book in bookRoutes" :key="book.label">
            <a :href="book.to">
              {{ book.label }}
            </a>
            <span> by {{ book.author }}</span>
          </li>
        </ul>
      </div>
    </div>
    <img class="person-tree-reading" :src="personTreeReadingFilePath" />
  </section>
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
      camenFacts: require("@/assets/json/camen_facts.json"),
      numRandomFacts: 3,
      randomFacts: this.setRandomFacts(),
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
          label: "the way of kings",
          author: "brandon sanderson"
        },
        {
          to: "https://en.wikipedia.org/wiki/The_Fifth_Season_(novel)",
          label: "the fifth season",
          author: "n.k. jemisin"
        },
        {
          to: "https://wanderinginn.com/",
          label: "the wandering inn",
          author: "pirateaba"
        },
        {
          to:
            "https://www.goodreads.com/en/book/show/38746152-the-book-of-delights",
          label: "the book of delights",
          author: "ross gay"
        },
        {
          to:
            "https://www.goodreads.com/book/show/28256439-the-hidden-life-of-trees",
          label: "the hidden life of trees",
          author: "peter wohlleben"
        }
      ]
    };
  },
  mounted() {
    this.setRandomFacts();
  },
  methods: {
    setRandomFacts: function() {
      if (this.camenFacts != null) {
        let size = this.numRandomFacts;
        var arr = Array.from(this.camenFacts);

        var result = new Array(size);

        for (let i = 0; i < size; i++) {
          let randomIdx = Math.floor(Math.random() * arr.length);
          let random = arr.splice(randomIdx, 1);
          result[i] = random[0];
        }
        this.randomFacts = result;
      } else {
        this.randomFacts = null;
      }
    }
  }
};
</script>

<style>
.about__image {
  height: 10rem;
  width: 10rem;
}

.about__externals {
  margin-top: 3rem;
}

.about__external {
  display: inline-block;
}

.about__icon {
  cursor: pointer;
  margin-right: 1rem;
  margin-left: 1rem;
  height: 3rem;
  width: 3rem;
}

.about__icon:hover {
  background-color: rgba(165, 159, 159, 0.199);
  border-radius: 6px;
}

.about__recommendations {
  padding-top: 0;
}

.person-hot-air-balloon {
  position: absolute;
  float: left;
  top: 0;
  left: -2rem;
}

.about__me__list__sub {
  margin-left: 10px;
}

.person-tree-reading {
  z-index: -1;
  position: absolute;
  right: 0.5rem;
  bottom: calc(1rem + 4rem + 5rem - 0.15rem);
  /* footer fontsize + footer top padding + footer bottom padding - a smidgeon */
}
</style>
