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
        import('./RogueSky.vue'),
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