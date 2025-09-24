<template>
  <div
    class="border rounded-lg p-6 transition-shadow duration-300 hover:shadow-2xl cursor-pointer"
  >
    <div class="ma-5">
      <div class="flex items-center">
        <img
          :src="`http://127.0.0.1:8000${photo}`"
          alt="User photo"
          class="w-22 h-22 rounded-full object-cover"
        />
        <div class="pl-8 flex flex-col truncate ...">
          <p class="font-bold">{{ username }}</p>
          <p>{{ email }}</p>
          <p>{{ phone }}</p>
        </div>
      </div>

      <div class="mt-8">
        <div v-for="item in items" :key="item.title" class="truncate ...">
          <div class="flex gap-2 items-center mt-3">
            <img
              class="h-5 flex items-center"
              :src="`${item.icon}.png`"
              alt="location"
            />
            <h1 class="font-bold">{{ item.title }}</h1>
          </div>
          <p class="mt-2 font-weight-[300]">
            {{ getValueByKey(user, item.value) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "UserCard",
  data() {
    return {
      photo: null,
      username: null,
      email: null,
      dialog: false,
      newTodo: "",

      items: [
        { icon: "location", title: "Location", value: "location" },
        { icon: "company", title: "Company", value: "company" },
        { icon: "website", title: "Website", value: "website" },
      ],
    };
  },
  mounted() {
    const userString = localStorage.getItem("user");
    const user = userString ? JSON.parse(userString) : null;
    this.email = user && user.email ? user.email : "Bilinmiyor";
    this.photo = user && user.photo ? user.photo : "Bilinmiyor";
    this.first_name = user && user.first_name ? user.first_name : "Bilinmiyor";
    this.last_name = user && user.last_name ? user.last_name : "Bilinmiyor";
  },

  methods: {
    openModal() {
      this.dialog = true;
    },
    closeModal() {
      this.dialog = false;
    },
  },
};
</script>
