<template>
  <v-dialog v-model="dialog" width="55rem" persistent>
    <v-card class="rounded-xl !p-0">
      <v-card-title
        class="d-flex justify-space-between align-center !p-4 border-b"
      >
        <h1 class="font-bold capitalize truncate w-100">New Post</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>
      <v-card-text class="!px-8 !py-12">
        <v-form ref="form" lazy-validation>
          <v-text-field
            class="!pb-5"
            v-model="newPostTitle"
            placeholder="Enter your new posts title..."
            @keydown.enter="addPost"
            variant="outlined"
            density="compact"
            hide-details="auto"
            :rules="[(v) => !!v?.trim() || '* This field cannot be left blank']"
          />

          <v-textarea
            v-model="newPostBody"
            label="Enter your paragraph here..."
            rows="3"
            density="compact"
            variant="outlined"
            no-resize
            auto-grow
            @keydown.enter="addPost"
            hide-details="auto"
            :rules="[(v) => !!v?.trim() || '* This field cannot be left blank']"
          ></v-textarea>
        </v-form>
      </v-card-text>
      <v-card-actions class="!p-4 border-t">
        <div class="w-full flex items-center justify-end">
          <v-btn @click="addPost">Save</v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  name: "NewPost",
  data() {
    return {
      dialog: false,
      newPostTitle: "",
      newPostBody: "",
    };
  },

  methods: {
    openModal() {
      this.dialog = true;
    },
    closeModal() {
      this.dialog = false;
    },

    async addPost() {
      const isValid = await this.$refs.form.validate();
      if (!isValid?.valid) {
        return;
      } else {
        try {
          const response = await axios.post(
            "http://127.0.0.1:8000/api/post/new/",
            {
              title: this.newPostTitle,
              body: this.newPostBody,
            },
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
              },
            }
          );

          // input temizleme
          this.newPost = "";
          this.$emit("refresh");
          this.closeModal();
        } catch (error) {
          console.error(
            "Error creating todo:",
            error.response?.data || error.message
          );
        }
      }
    },
  },
};
</script>
