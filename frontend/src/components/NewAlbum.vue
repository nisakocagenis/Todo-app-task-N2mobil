<template>
  <v-dialog v-model="dialog" width="55rem" persistent>
    <v-card class="rounded-xl !p-0">
      <v-card-title
        class="d-flex justify-space-between align-center !p-4 border-b"
      >
        <h1 class="font-bold capitalize truncate w-100">New Album</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>
      <v-card-text>
        <v-text-field
          class="!pb-5"
          v-model="newTitle"
          label="Enter your new albums title"
          @keydown.enter="addPhoto"
          variant="outlined"
          density="compact"
          hide-details="auto"
        />
        <v-file-input
          :multiple="true"
          v-model="newPhoto"
          accept="image/*"
          label="Pick your photos"
          variant="outlined"
          density="compact"
          hide-details="auto"
          prepend-icon=""
        ></v-file-input>
        <!-- Önizleme Grid -->
        <div
          v-if="previews.length > 0"
          class="grid grid-cols-3 gap-4 mt-4 max-h-60 overflow-y-auto"
        >
          <div
            v-for="(preview, index) in previews"
            :key="index"
            class="relative border rounded-lg overflow-hidden group"
          >
            <img
              :src="preview"
              alt="preview"
              class="w-full h-32 object-cover"
            />
          </div>
        </div>
      </v-card-text>
      <v-card-actions class="w-full flex items-center justify-end">
        <v-btn @click="addPhoto()">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";
export default {
  name: "NewAlbum",

  data() {
    return {
      dialog: false,
      newPhoto: [],
      newTitle: "",
      previews: [], // Sadece önizleme URL'leri tutulur
    };
  },
  methods: {
    generatePreviews() {
      this.previews.forEach((url) => URL.revokeObjectURL(url));

      this.previews = this.newPhoto.map((file) => URL.createObjectURL(file));
    },

    openModal() {
      this.dialog = true;
    },
    closeModal() {
      this.dialog = false;
    },
    async addPhoto() {
      try {
        // 1. Adım -> Albüm oluşturma
        const albumData = new FormData();
        albumData.append("title", this.newTitle);

        this.newPhoto.forEach((file) => {
          albumData.append("files", file);
        });

        const albumResponse = await axios.post(
          `http://127.0.0.1:8000/api/album/new/`,
          albumData,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
              "Content-Type": "multipart/form-data",
            },
          }
        );

        const createdAlbumId = albumResponse.data.id;

        console.log("Albüm oluşturuldu:", createdAlbumId);

        const photoFormData = new FormData();

        if (Array.isArray(this.newPhoto)) {
          this.newPhoto.forEach((photo) => {
            photoFormData.append("photo", photo);
          });
        } else {
          photoFormData.append("photo", this.newPhoto);
        }

        await axios.post(
          `http://127.0.0.1:8000/api/photo/new/${createdAlbumId}/`,
          photoFormData,
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("token")}`,
              "Content-Type": "multipart/form-data",
            },
          }
        );

        console.log("Fotoğraf(lar) başarıyla yüklendi!");

        this.newPhoto = null;
        this.newTitle = "";
        this.$emit("refresh");
        this.closeModal();
      } catch (error) {
        console.error(
          "Error creating album or photo:",
          error.response?.data || error.message
        );
      }
    },
  },
};
</script>
