import Buefy from 'buefy'
import Vue from 'vue'
import VueRouter from 'vue-router'

import 'buefy/dist/buefy.css'

import App from './App.vue'
import router from './routes/router.js'

Vue.use(Buefy)
Vue.use(VueRouter)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
