import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    name: "Login",
    path: "/",
    component: () => import("./views/LoginPage.vue"),
  },
  {
    name: "Users",
    path: "/Users",
    component: () => import("./views/HomePage.vue"),
    meta: {
      icon: usersIcon,
      title: "Users",
      type: 1,
      requiresAuth: true,
    },
  },

  {
    name: "Todos",
    path: "/Todos",
    component: () => import("./views/TodosPage.vue"),

    meta: {
      icon: todosIcon,
      title: "Todos",
      type: 2,
      requiresAuth: true,
    },
  },
  {
    name: "Posts",
    path: "/Posts",
    component: () => import("./views/PostsPage.vue"),
    meta: {
      icon: postsIcon,
      title: "Posts",
      type: 2,
      requiresAuth: true,
    },
  },
  {
    name: "Albums",
    path: "/Albums",
    component: () => import("./views/AlbumsPage.vue"),
    meta: {
      icon: albumsIcon,
      title: "Albums",
      type: 2,
      requiresAuth: true,
    },
  },
  {
    name: "Photos",
    path: "/Photos/:albumsId",
    component: () => import("./views/PhotosPage.vue"),
  },
];

import usersIcon from "./components/usersIcon.vue";
import todosIcon from "./components/todosIcon.vue";
import postsIcon from "./components/postsIcon.vue";
import albumsIcon from "./components/albumsIcon.vue";

const router = createRouter({
  routes,
  history: createWebHistory(),
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem("user");

  if (to.meta.requiresAuth && !isAuthenticated) {
    next("/");
  } else {
    next();
  }
});

export default router;
