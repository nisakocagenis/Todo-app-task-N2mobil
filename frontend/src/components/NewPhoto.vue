<template>
  <v-dialog v-model="dialog">
    <v-card>
      <v-card-title class="d-flex justify-space-between align-center !mb-3">
        <h1 class="font-bold capitalize truncate w-100">New Photo</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>

      <v-file-input
        v-model="newPhoto"
        accept="image/*"
        label="Fotoğraf Seç"
        prepend-icon="mdi-camera"
      ></v-file-input>

      <v-card-actions class="w-full flex items-center justify-end">
        <v-btn @click="addPhoto()">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      dialog: false,
      newPhoto: null,
      newTitle: "",
      selectedAlbumId: null,
    };
  },
  mounted() {
    this.selectedAlbumId = this.$route.params.albumsId;
    console.log("Seçilen Albüm ID:", this.selectedAlbumId);
  },
  methods: {
    openModal() {
      this.dialog = true;
    },

    closeModal() {
      this.dialog = false;
    },
    async addPhoto() {
      try {
        // FormData kullanıyoruz
        const formData = new FormData();
        formData.append("title", this.newTitle);
        formData.append("photo", this.newPhoto); // burada this.newPhoto bir File objesi olmalı

        await axios.post(
          `http://127.0.0.1:8000/api/photo/new/${this.selectedAlbumId}/`, // Albüm id dinamik
          formData,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
              "Content-Type": "multipart/form-data",
            },
          }
        );

        // Temizleme
        this.newPhoto = null;
        this.newTitle = "";
        this.$emit("refresh");
        this.closeModal();
      } catch (error) {
        console.error(
          "Error creating photo:",
          error.response?.data || error.message
        );
      }
    },
  },
};
</script>
