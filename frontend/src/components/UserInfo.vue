<template>
  <v-dialog v-model="dialog" width="55%" persistent>
    <v-card class="rounded-xl pa-4 modal">
      <v-card-title class="d-flex justify-space-between align-center !mb-3">
        <h1 class="font-bold capitalize truncate w-100">Information</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>
      <div>
        <div class="flex items-center">
          <img
            :src="`http://127.0.0.1:8000${photo}`"
            alt="User photo"
            class="w-22 h-22 rounded-full object-cover"
          />
          <div class="pl-8 flex flex-col truncate ...">
            <div class="flex gap-2 capitalize">
              <p class="font-bold">{{ first_name }}</p>
              <p class="font-bold">{{ last_name }}</p>
            </div>
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
              {{ item.value }}
            </p>
          </div>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  name: "UserInfo",
  data() {
    return {
      dialog: false,
      info: null,
      isOpen: false,
      photo: null,
      email: null,
      first_name: null,
      last_name: null,
      location: null,
      company: null,
      website: null,
      phone: null,
      items: [],
    };
  },
  mounted() {
    const userString = localStorage.getItem("user");
    const user = userString ? JSON.parse(userString) : null;
    this.photo = user && user.photo ? user.photo : "Bilinmiyor";
    this.first_name = user && user.first_name ? user.first_name : "Bilinmiyor";
    this.last_name = user && user.last_name ? user.last_name : "Bilinmiyor";
    this.email = user && user.email ? user.email : "Bilinmiyor";
    this.company = user && user.company ? user.company : "Bilinmiyor";
    this.location = user && user.location ? user.location : "Bilinmiyor";
    this.website = user && user.website ? user.website : "Bilinmiyor";
    this.phone = user && user.phone_no ? user.phone_no : "Bilinmiyor";

    this.items = [
      { icon: "location", title: "Location", value: this.location },
      { icon: "company", title: "Company", value: this.company },
      { icon: "website", title: "Website", value: this.website },
    ];
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
