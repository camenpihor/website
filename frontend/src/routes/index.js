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
      meta: { pageTitle: "" }
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
      path: "/404",
      name: "error",
      component: () => import("./NotFound.vue"),
      props: (route) => ({ requestedPath: route.fullPath }),
      meta: { pageHome: "error" }
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