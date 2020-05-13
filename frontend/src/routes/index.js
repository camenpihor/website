import VueRouter from 'vue-router'

const router = new VueRouter({
  mode: "history",
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("./Home.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("./About.vue")
    },
    {
      path: "/recommendations",
      name: "recommendations",
      component: () => import("./Recommendations.vue")
    },
    {
      path: "/github",
      name: "github",
      beforeEnter() { location.href = "http://github.com/camenpihor" }
    },
    {
      path: "/404",
      name: "error",
      component: () => import("./NotFound.vue"),
      props: (route) => ({ requestedPath: route.fullPath }),
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