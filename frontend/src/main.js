import Buefy from 'buefy'
import moment from 'moment-timezone'
import Vue from 'vue'
import VueRouter from 'vue-router'
import VueMoment from 'vue-moment'
import VCalendar from 'v-calendar';

import 'buefy/dist/buefy.css'

import App from './App.vue'
import router from './routes/index.js'


Vue.use(Buefy);
Vue.use(VueRouter);
Vue.use(VueMoment, {
  moment,
})
Vue.use(VCalendar, { componentPrefix: 'vc' });

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
