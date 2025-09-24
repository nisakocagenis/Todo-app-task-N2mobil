<template>
  <v-app>
    <div
      class="bg-[#F5F5F5] w-[260px] border-r-gray-300 h-full py-8 flex flex-col justify-between"
    >
      <div class="flex flex-col">
        <div class="my-1" v-if="$route.name !== 'Users'">
          <div class="flex flex-col ml-4 mb-5 !pt-0">
            <div class="flex items-center">
              <img
                :src="`http://127.0.0.1:8000${photo}`"
                alt="user"
                class="w-12 h-12 rounded-full object-cover"
              />
              <div class="flex flex-col items-center justify-center ml-3">
                <div class="flex gap-1.5">
                  <p class="text-sm font-weight-bold capitalize">
                    {{ first_name }}
                  </p>
                  <p class="text-sm font-weight-bold capitalize">
                    {{ last_name }}
                  </p>
                  <div @click="openModal">
                    <img
                      src="/public/information-outline.png"
                      alt="info"
                      class="w-4 h-4 cursor-pointer"
                    />
                    <!-- Dialog Modal -->
                    <user-info ref="UserInfoRef"></user-info>
                  </div>
                </div>
                <p class="text-[#5C6672] text-xs underline">
                  {{ email }}
                </p>
              </div>
            </div>
          </div>
          <div class="mt-5 w-full">
            <v-divider class="bg-color-[#5C6672] mb-14 mx-4"></v-divider>
          </div>
        </div>

        <div class="flex flex-col gap-6 cursor-pointer">
          <div v-for="item in navItems" :key="item.path" class="gap-6">
            <div
              class="h-10 flex items-center pl-8"
              @click="go(item.name)"
              :class="{
                '!bg-white': item.name == $route.name,
              }"
            >
              <div
                class="absolute left-0 rounded-r-xl w-2 h-10 bg-[#4F359B]"
                v-if="$route.name === item.name"
              ></div>
              <div class="flex items-center">
                <component :is="item.meta.icon" class="mr-2" />

                <h1 :class="$route.name === item.name ? 'text-[#4F359B]' : ''">
                  {{ item.name }}
                </h1>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <div class="flex items-center justify-center">
          <v-col cols="auto">
            <v-btn variant="text" class="rounded-md elevation-0" @click="logout"
              >Log Out</v-btn
            >
          </v-col>
        </div>
        <v-divider class="bg-color-[#5C6672] mb-6 mx-4"></v-divider>
        <div class="flex justify-center h-10 mx-4">
          <div class="img">
            <img
              src="/public/logo.png"
              alt="logo"
              width="40"
              height="40"
              viewBox="0 0 40 40"
            />
          </div>
          <h1 class="text-black align-content-center pl-2">N2Mobil</h1>
        </div>
      </div>
    </div>
  </v-app>
</template>

<script>
import UsersIcon from "./usersIcon.vue";
import TodosIcon from "./todosIcon.vue";
import AlbumsIcon from "./albumsIcon.vue";
import PostsIcon from "./postsIcon.vue";
import UserInfo from "./UserInfo.vue";

export default {
  components: { UserInfo, UsersIcon, TodosIcon, AlbumsIcon, PostsIcon },

  data() {
    return {
      username: null,
      email: null,
      photo: null,
      showUserInfo: false,
    };
  },
  methods: {
    go(name) {
      this.$router.push({
        name: name,
      });
    },
    logout() {
      localStorage.clear();
      this.$router.push({
        name: "Login",
      });
    },
    openModal(info) {
      this.$refs.UserInfoRef.openModal(info);
    },
  },

  computed: {
    navItems() {
      if (this.$route.name == "Users") {
        return this.$router.getRoutes().filter((e) => e.meta.type == 1);
      }
      return this.$router.getRoutes().filter((e) => e.meta.type == 2);
    },
  },
  mounted() {
    const userString = localStorage.getItem("user");
    const user = userString ? JSON.parse(userString) : null;
    this.email = user && user.email ? user.email : "Bilinmiyor";
    this.photo = user && user.photo ? user.photo : "Bilinmiyor";
    this.first_name = user && user.first_name ? user.first_name : "Bilinmiyor";
    this.last_name = user && user.last_name ? user.last_name : "Bilinmiyor";
  },
};
</script>
