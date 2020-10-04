import Buefy from "buefy";
import Vue from "vue";
import VCalendar from "v-calendar";
import VueRouter from "vue-router";

import "buefy/dist/buefy.css";

import App from "./App.vue";
import router from "./routes/index.js";

Vue.use(Buefy);
Vue.use(VCalendar, { componentPrefix: "vc" });
Vue.use(VueRouter);

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
