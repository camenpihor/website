<template>
  <section class="jobs">
    <div class="section has-text-centered">
      <div class="columns is-vcentered">
        <div class="column">
          <img class="job__image" :src="meFilePath" />
        </div>
        <div class="column">
          <p class="title is-3">Camen Piho</p>
          <p class="subtitle is-5">Data Scientist</p>
          <ul class="job__externals">
            <router-link
              :to="{ name: 'github' }"
              tag="li"
              class="job__external"
            >
              <img :src="githubIconFilePath" class="job__icon"
            /></router-link>
            <li class="job__external">
              <a href="camen_piho_resume.pdf" target="_blank"
                ><img :src="resumeIconFilePath" class="job__icon"
              /></a>
            </li>
            <li class="job__external">
              <a href="mailto:camenrogue@gmail.com">
                <img :src="emailIconFilePath" class="job__icon" />
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="content">
        <p class="has-text-centered is-size-3">
          I'm on the job market!
        </p>
        <p>
          I'm a Data Scientist with about
          <a href="camen_piho_resume.pdf">4 years of training</a> who's all about
          improving the ways in which we interact with and affect the world we inhabit.
        </p>
        <p>I'm on the job market looking for a platform that will allow me to continue my
          practice and research into climatological phenomena using tools like machine
        learning, computer vision, and numerical simulation before entering graduate study
        in Fall 2022. During my graduate study I plan to use numerical simulation and machine
        learning to pursue
          fundamental research into the earth's atmosphere and climate.
        </p>
        <p>I look not just at
          humanity's current planet, Earth, but beyond -- developing fundamental
          understanding of climatology is instrumental to humanity's longevity, wherever
          we may be.
        </p>
        <p class="job__questions">
        <b-collapse
            animation="slide"
            v-for="(collapse, index) of collapses"
            :key="index"
            :open="isOpen == index"
            @open="isOpen = index"
            >
            <div slot="trigger" slot-scope="props" class="card-header"
                role="button">
              <a class="card-header-icon">
                    <b-icon
                        pack="fas" :icon="props.open ? 'chevron-down' : 'chevron-right'">
                    </b-icon>
                </a>
                <p class="card-header-title">
                    {{ collapse.title }}
                </p>
            </div>
            <div class="card-content">
                <ul>
                  <li v-for="question in collapse.questions" :key="question">
                    {{ question }}
                  </li>
                </ul>
            </div>
        </b-collapse>
        </p>
        <p>
          I've worked in multiple research and industrial settings using tools like MCMC predictive
          modeling, causal inference, computer vision, data pipelining, and satellite
          imagery looking at critical interactions between humans and weather.
          </p>
          <p>With NASA
          we built computer vision models for wildfire detection using geostationary
          satellite imagery. With Freebird we built computational models to understand
          extreme weather events and how they impact air travel. And in my own time I've
          maintained a long term study of how evapotranspiration in trees global
          weather patterns.
        </p>
        <p>
          Currently, I am looking for places where I can continue to learn about
          climatological phenomena and practice state-of-the-art
          techniques in machine learning, computer vision, and numerical simulation over the next 2 years.
        </p>
        <p>Outside of jobs over the next 2 years, I am also extremely interested in talking
        about academia, possible research directions, and life as a career scientist.
        </p>
        <p>
          Some experiences that I think it would be helpful to hear about (this, however,
         is not an exhaustive list):
          <ul>
            <li>Research or industrial application in the domain of complex planetary
            systems (atmosphere, ecology, biosphere, ocean sciences, etc.)</li>
            <li>Chicago-based data scientists</li>
            <li>Research into scalable Bayesian modeling</li>
            <li>Research into applied statistics</li>
          </ul>
        </p>
        <p>
          Reach out to me at <a href="mailto://camen.piho.r@gamil.com">camen[dot]piho[dot]r@gmail.com</a>, if you are interested in
          talking. I think continued fundamental research into climatology is
          critical and any opportunity to talk more about it is a good
          opportunity to me!
        </p>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      meFilePath: require("@/assets/me.svg"),
      resumeIconFilePath: require("@/assets/icons/resume-icon.svg"),
      githubIconFilePath: require("@/assets/icons/github-icon.svg"),
      emailIconFilePath: require("@/assets/icons/email-icon.svg"),
      isOpen: 0,
      collapses: [
        {
          title: "Jobs",
          questions: ["This is a question?", "And this is another question?", "But this is also a question?"],
        },
        {
          title: "Earth Sciences",
          questions: ["This is a question?", "And this is another question?", "But this is also a question?"],
        },
        {
          title: "Machine Learning in Earth Sciences",
          questions: ["This is a question?", "And this is another question?", "But this is also a question?"],
        },
        {
          title: "Bayesian Statistics in Academia",
          questions: ["This is a question?", "And this is another question?", "But this is also a question?"],
        },
        {
          title: "Applied Statistics Graduate Study",
          questions: ["This is a question?", "And this is another question?", "But this is also a question?"],
        },
      ],
    };
  },
};
</script>

<style>
.job__image {
  height: 12rem;
  width: 12rem;
}

.job__externals {
  margin-top: 3rem;
}

.job__external {
  display: inline-block;
}

.job__icon {
  cursor: pointer;
  margin-right: 1rem;
  margin-left: 1rem;
  height: 3rem;
  width: 3rem;
}

.job__icon:hover {
  background-color: rgba(165, 159, 159, 0.199);
  border-radius: 6px;
}

.job__questions {
  margin-top: 3rem !important;
  margin-bottom: 3rem !important;
}
</style>
