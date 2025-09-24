<template>
  <div v-if="!loading" class="flex h-screen w-full">
    <navigation-drawer></navigation-drawer>
    <div class="flex flex-col w-full h-screen !pl-8 !pb-7">
      <header class="justify-between w-full h-10 my-7 px-8 flex items-center">
        <div class="flex items-center cursor-pointer" @click="goAlbums">
          <img
            src="../../public/leftok.png"
            class="w-8 h-8"
            @click="goAlbums"
          />
          <h1 class="text-2xl font-bold ml-6 my-1">Go Albums</h1>
        </div>
        <div class="flex justify-end">
          <v-col cols="auto">
            <v-btn class="rounded-xl bg-[#4F359B]" @click="openModal">
              + New Photos
            </v-btn>
            <new-photo ref="newPhotosRef" @refresh="initial" />
          </v-col>
        </div>
      </header>

      <div class="grid grid-cols-4 gap-4 w-full overflow-auto !p-4">
        <img
          v-for="photo in itemsList"
          :key="photo.albumId"
          :src="`http://127.0.0.1:8000${photo.photo}`"
          alt="photo.title"
          class="object-cover w-full h-40 rounded"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavigationDrawer from "../components/NavigationDrawer.vue";
import NewPhoto from "../components/NewPhoto.vue";

export default {
  components: { NavigationDrawer, NewPhoto },
  data() {
    return {
      itemsList: [],
      loading: true,
    };
  },

  mounted() {
    this.initial();
  },

  methods: {
    initial() {
      const albumId = this.$route.params.albumsId;
      axios
        .get(`http://127.0.0.1:8000/api/photo/foto/${albumId}/`)
        .then((response) => {
          this.itemsList = response.data;
        })
        .catch((error) => {
          console.error("Veri alınırken hata oluştu:", error);
        });
      this.loading = false;
    },
    openModal() {
      this.$refs.newPhotosRef.openModal();
    },

    goAlbums() {
      this.$router.push({
        name: "Albums",
      });
    },
  },
};
</script>
