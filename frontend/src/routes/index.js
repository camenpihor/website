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
      meta: { pageHome: "home" }
    },
    {
      path: "/about",
      name: "about",
      component: () => import("./About.vue"),
      meta: { pageHome: "about" }
    },
    {
      path: "/recommendations",
      name: "recommendations",
      component: () => import("./Recommendations.vue"),
      meta: { pageHome: "recommendations" }
    },
    {
      path: "/github",
      name: "github",
      beforeEnter() { location.href = "http://github.com/camenpihor" }
    },
    {
      path: "/jobs",
      name: "jobs",
      component: () => import("./Jobs.vue"),
      meta: { pageHome: "jobs" }
    },
    {
      path: "/blog",
      name: "blog",
      component: () => import("./Blog.vue"),
      meta: { pageHome: "blog" }
    },
    {
      path: "/blog/:id",
      name: "blog-post",
      component: () => import("./BlogPost.vue"),
      meta: { pageHome: "blog" }
    },
    {
      path: "/math",
      name: "math",
      beforeEnter() { location.href = "https://github.com/camenpihor/math-implementations/tree/master/notebooks" }
    },
    {
      path: "/roguesky",
      name: "rogue-sky",
      meta: { pageHome: "rogue-sky" },
      component: () => import("./RogueSky.vue"),
    },
    {
      path: '/roguesky/:latitude/:longitude',
      name: "rogue-sky-location",
      component: () => import("./RogueSky.vue"),
      meta: { pageHome: "rogue-sky" },
    },
    {
      path: "/404",
      name: "error",
      component: () => import("./NotFound.vue"),
      meta: { pageHome: "error" }
    },
    {
      path: '*',
      component: () => import("./NotFound.vue"),
      props: (route) => ({ requestedPath: route.fullPath }),
      alias: "/404",
      meta: { pageHome: "error" }
    },
  ],
})

export default router;