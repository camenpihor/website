import Buefy from 'buefy'
import Vue from 'vue'
import VueRouter from 'vue-router'
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faCloudMoonRain, faSearch, faSnowflake, faMoon, faCloudShowersHeavy, faWind,
  faCloud, faCloudMoon, faArrowUp, faSyncAlt
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import 'buefy/dist/buefy.css'

import App from './App.vue'
import router from './routes/router.js'


library.add(
  faCloudMoonRain, faSearch, faSnowflake, faMoon, faCloudShowersHeavy, faWind,
  faCloud, faCloudMoon, faArrowUp, faSyncAlt
);
Vue.component('vue-fontawesome', FontAwesomeIcon);

Vue.use(Buefy, {
  defaultIconComponent: 'vue-fontawesome',
  defaultIconPack: 'fas',
})
Vue.use(require('vue-moment'));
Vue.use(VueRouter)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
