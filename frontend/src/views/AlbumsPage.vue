<template>
  <div class="flex h-screen w-full">
    <navigation-drawer></navigation-drawer>
    <div class="flex flex-col w-full h-screen !pl-8 !pb-7">
      <header class="w-full h-10 my-7 flex items-center">
        <v-col cols="auto">
          <v-btn class="rounded-xl bg-[#4F359B]" @click="openModal">
            + New Album
          </v-btn>
          <new-album ref="NewAlbumRef" @refresh="initial" />
        </v-col>
      </header>

      <div class="grid grid-cols-3 gap-6 w-full overflow-auto !mt-4">
        <albums-card
          v-for="albums in itemsList"
          :key="albums"
          :albums="albums"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import albumsCard from "../components/albumsCard.vue";
import NavigationDrawer from "../components/NavigationDrawer.vue";
import NewAlbum from "../components/NewAlbum.vue";
export default {
  data() {
    return {
      itemsList: [],
    };
  },
  components: { NavigationDrawer, albumsCard, NewAlbum },

  mounted() {
    this.initial();
  },

  methods: {
    initial() {
      axios
        .get(`http://127.0.0.1:8000/api/album/album_list/`)
        .then((response) => {
          this.itemsList = response.data;
        })
        .catch((error) => {
          console.error("Veri alınırken hata oluştu:", error);
        });
    },
    openModal() {
      this.$refs.NewAlbumRef.openModal();
    },
  },
};
</script>
