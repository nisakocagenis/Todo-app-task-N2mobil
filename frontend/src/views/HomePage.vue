<template>
  <div class="flex h-screen w-full">
    <navigation-drawer></navigation-drawer>

    <div class="flex flex-col w-full h-screen !pl-7 !pb-7">
      <header class="w-full h-10 mt-8 px-8 flex items-center justify-between">
        <h1 class="text-2xl font-bold">All Users</h1>
      </header>

      <div class="grid grid-cols-3 gap-6 w-full overflow-auto !mt-4">
        <userCard
          v-for="user in itemsList"
          :key="user.id"
          :user="user"
          @click="goTodo(user)"
        ></userCard>
      </div>
    </div>
  </div>
</template>

<script>
import userCard from "../components/UserCard.vue";
import axios from "axios";
import NavigationDrawer from "../components/NavigationDrawer.vue";

export default {
  data() {
    return {
      itemsList: [],
    };
  },
  components: { NavigationDrawer, userCard },

  mounted() {
    axios
      .get("http://localhost:8000/api/user/")
      .then((response) => {
        this.itemsList = response.data;
      })
      .catch((error) => {
        console.error("Veri alınırken hata oluştu:", error);
      });
  },

  methods: {
    goTodo(user) {
      this.$store.commit("setSelectedUser", user);
      this.$router.push({ name: "Todos" });
    },
  },
};
</script>
