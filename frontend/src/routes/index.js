import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: "history",
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: "/",
      component: () => import("./Home.vue"),
      name: "home"
    },
    {
      path: "/about",
      component: () => import("./About.vue"),
      name: "about"
    },
    {
      path: "/404",
      component: () => import("./NotFound.vue"),
      props: (route) => ({ requestedPath: route.fullPath }),
      name: "error",
    },
    {
      path: '*',
      component: () => import("./NotFound.vue"),
      props: (route) => ({ requestedPath: route.fullPath }),
      alias: "/404"
    },
  ],
});

export default router;