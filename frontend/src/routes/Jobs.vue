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
              <a href="mailto:camen.piho.r@gmail.com">
                <img :src="emailIconFilePath" class="job__icon" />
              </a>
            </li>
            <li class="job__external">
              <a href="https://www.linkedin.com/in/camen-piho/" target="_blank"
                ><img :src="linkedinIconFilePath" class="job__icon"
              /></a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="section">
      <div class="content">
        <p class="has-text-centered is-size-3">
          I’m on the job market!
        </p>
        <p>
          I’m a Data Scientist who’s passionate about improving how we interact
          with and affect the world we inhabit at planetary scale.
        </p>
        <p>
          After
          <a href="camen_piho_resume.pdf" target="_blank">4 years of training</a
          >, I want to use the tools that I’ve learned to take on what I see as
          the one of the most important questions in science:
          <strong
            >How far can we push our understanding of planetary climates using
            state-of-the-art machine learning and numerical simulation?</strong
          >
          I look not just at humanity’s current planet, Earth, but beyond --
          developing a fundamental understanding of climatology is instrumental
          to humanity’s longevity, wherever we may be.
        </p>
        <p>
          <strong
            >I am looking for a job that will allow me to continue learning
            about climate science and to stay abreast of new techniques in
            machine learning, computer vision, and numerical simulation</strong
          >
          until beginning graduate school, which I aim to do in Fall 2022.
        </p>
        <p>
          In my career so far, I’ve applied MCMC predictive modeling, causal
          inference, computer vision, data pipelining, and satellite imagery
          analysis to study how humans and weather systems impact one another.
        </p>
        <p>
          With NASA, I built computer vision models for wildfire detection using
          geostationary satellite imagery; with Freebird, I built computational
          models to understand extreme weather events and how they impact air
          travel; and in a long-running personal project, I’ve studied how
          evapotranspiration in trees affects global weather patterns.
        </p>
        <p>
          In addition to trying to find the best job for the next two years,
          <strong
            >I’m also broadly interested in talking to climate researchers
            working in academia or industry</strong
          >.
        </p>
        <p>
          I think continued fundamental research into climatology is critical
          and any opportunity to talk more about it is a great opportunity to
          me. If you think I could contribute to your work or you would be open
          to receive questions about the intersection between machine learning
          and climatology, please reach out to me at
          <a href="mailto:camen.piho.r@gmail.com"
            >camen[dot]piho[dot]r@gmail.com</a
          >.
        </p>
        <div class="job__questions">
          <h1 class="title is-4">
            Some specific questions
          </h1>
          <b-collapse
            animation="slide"
            v-for="(collapse, index) of collapses"
            :key="index"
            :open="isOpen == index"
            @open="isOpen = index"
          >
            <div
              slot="trigger"
              slot-scope="props"
              class="card-header"
              role="button"
            >
              <a class="card-header-icon">
                <b-icon
                  pack="fas"
                  :icon="props.open ? 'chevron-down' : 'chevron-right'"
                >
                </b-icon>
              </a>
              <p class="card-header-title">{{ collapse.title }}</p>
            </div>
            <div class="card-content">
              <ul>
                <li v-for="question in collapse.questions" :key="question">
                  {{ question }}
                </li>
              </ul>
            </div>
          </b-collapse>
        </div>
        <ul class="jobs__links">
          <li>
            <span class="has-text-weight-bold">GitHub</span>:
            <router-link :to="{ name: 'github' }" target="_blank"
              >github.com/camenpihor</router-link
            >
          </li>
          <li>
            <span class="has-text-weight-bold">Resume</span>:
            <a href="camen_piho_resume.pdf" target="_blank"
              >camenpiho.com/camen_piho_resume.pdf</a
            >
          </li>
          <li>
            <span class="has-text-weight-bold">Email</span>:
            <a href="mailto:camen.piho.r@gmail.com"
              >camen[dot]piho[dot]r@gmail.com</a
            >
          </li>
          <li>
            <span class="has-text-weight-bold">LinkedIn</span>:
            <a href="https://www.linkedin.com/in/camen-piho/" target="_blank">
              linkedin.com/in/camen-piho/
            </a>
          </li>
        </ul>
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
      linkedinIconFilePath: require("@/assets/icons/linkedin-icon.svg"),
      isOpen: -1,
      collapses: [
        {
          title: "Jobs",
          questions: [
            "Do you know of any academic labs that would be interested in an industrially trained data scientist?",
            "Do you know of any companies inhabiting the intersection between machine learning and earth science?",
            "Do you know of any geospatial companies looking for a data scientist or python engineer?",
            "Do you know any people that would be interested in talking more with me?",
          ],
        },
        {
          title: "Earth Sciences",
          questions: [
            "Do you know any active researchers that would be interested in talking with me about their work and path?",
            "Do you know of any interesting projects that I should check out?",
            "Do you know of any labs that would be interested in a data scientist?",
          ],
        },
        {
          title: "Machine Learning in Earth Sciences",
          questions: [
            "What are the effects of pursuing a graduate degree in earth science versus applied statistics?",
            "What tools are currently being developed?",
            "Do you know of any departments, labs, or people inhabiting this space that I should reach out to?",
            "What's the bread-and-butter toolbox used?",
            "Do you know of any interesting papers or research being conducted in this space?",
          ],
        },
        {
          title: "Applied Statistics Graduate Study",
          questions: [
            "What does a program tend to look like?",
            "How much freedom is there to work with other departments while pursuing your degree?",
            "What type of experience is useful when applying?",
            "Do you know anyone with a graduate degree in applied statistics who might be willing to talk with me about their work and path?",
          ],
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
  margin-top: 1rem;
}

.job__external {
  display: inline-block;
}

.job__icon {
  cursor: pointer;
  margin-right: 0.5rem;
  margin-left: 0.5rem;
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

.jobs__links {
  list-style: none !important;
  margin-left: 0 !important;
}
</style>
