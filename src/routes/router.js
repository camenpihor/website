import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () => import('./Home.vue'),
      name: "home"
    },
    {
      path: '/documentation',
      component: () => import('./Documentation.vue'),
      name: "documentation"
    },
    {
      path: '/rogue-sky',
      component: () => import('./rogue_sky/Home.vue'),
      name: "rogue-sky-home"
    },
    {
      path: '/rogue-sky/:latitude/:longitude',
      component: () => import('./rogue_sky/Forecast.vue'),
    },
    {
      path: '/404',
      component: () => import('./Error.vue'),
      name: "404"
    },
    {
      path: '*',
      redirect: '/404'
    },
  ],
});

export default router;