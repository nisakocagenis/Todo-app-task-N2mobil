<template>
  <div
    class="border rounded-lg p-6 transition-shadow duration-300 hover:shadow-2xl cursor-pointer"
    @click="goPhotos"
  >
    <!-- Kolaj -->
    <div class="flex pa-5">
      <div class="grid grid-cols-2 w-full">
        <img
          v-for="photo in photosList.slice(0, 4)"
          :key="photo.id"
          :src="`http://127.0.0.1:8000${photo.photo}`"
          alt="photo"
          class="w-full h-33 object-cover"
        />
      </div>
    </div>
    <div class="pa-3 text-center">{{ albums.title }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      photosList: [],
    };
  },

  provide() {
    return {
      albums: this.photosList,
    };
  },
  props: {
    albums: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    const albumId = this.albums.id;
    axios
      .get(`http://127.0.0.1:8000/api/photo/foto/${albumId}/`)
      .then((response) => {
        this.photosList = response.data;
      })
      .catch((error) => {
        console.error("Veri alınırken hata oluştu:", error);
      });
  },
  methods: {
    goPhotos() {
      this.$router.push({
        name: "Photos",
        params: { albumsId: this.albums.id },
      });
    },
  },
};
</script>
