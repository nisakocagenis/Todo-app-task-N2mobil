<template>
  <v-dialog
    v-model="dialog"
    width="67%"
    height="75%"
    class="h-full p-8"
    persistent
  >
    <v-card class="rounded-xl pa-4 overflow-hidden">
      <v-card-title class="d-flex justify-space-between align-center !mb-3">
        <h1 class="font-bold capitalize truncate w-100">{{ post?.title }}</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>

      <div class="h-full">
        <v-row>
          <!-- Sol taraf -->
          <v-col class="overflow-y-auto ma-2 h-[550px]">
            <p class="first-letter:uppercase m-5">{{ post?.body }}</p>
          </v-col>

          <v-divider vertical class="mx-2" />

          <!-- Sağ taraf -->
          <v-col class="overflow-y-auto p-8 h-[550px]">
            <h1 class="font-bold px-4 pb-5 text-xl">Comment</h1>
            <div v-for="comment in itemList" :key="comment.id">
              <div class="flex items-start gap-3">
                <img
                  v-if="comment.photo"
                  :src="`http://127.0.0.1:8000${comment.photo}`"
                  alt="comment-photo"
                  class="rounded-full h-12 w-12 object-cover"
                />
                <div class="flex flex-col justify-start px-3 pb-6">
                  <h3 class="font-bold capitalize">{{ comment.name }}</h3>
                  <p>{{ comment.body }}</p>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </div>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      itemList: [],
      dialog: false,
      post: null,
    };
  },
  methods: {
    openModal(post) {
      this.post = post;

      axios
        .get(`http://127.0.0.1:8000/api/comment/yorum/${post.id}/`)
        .then((response) => {
          this.itemList = response.data;
        })
        .catch((error) => {
          console.error("Veri alınırken hata oluştu:", error);
        });
      this.dialog = true;
    },
    closeModal() {
      this.dialog = false;
      this.post = null;
    },
  },
};
</script>
