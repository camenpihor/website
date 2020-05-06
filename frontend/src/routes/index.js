import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: 'history',
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      component: () => import('./Home.vue'),
      name: "home"
    },
  ],
});

export default router;