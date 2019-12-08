import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () =>
        import('./Home.vue'),
    },
    {
      path: '/rogue-sky',
      component: () =>
        import('./rogue_sky/Home.vue'),
    },
    {
      path: '/rogue-sky/:latitude/:longitude',
      component: () =>
        import('./rogue_sky/Forecast.vue'),
    },
    {
      path: '/404',
      meta: { title: '404' },
      component: () =>
        import('./Error.vue'),
    },
    {
      path: '*',
      redirect: '/404'
    },
  ],
});

export default router;