<template>
  <v-dialog v-model="dialog" width="67%" persistent>
    <v-card class="rounded-xl pa-4">
      <v-card-title class="d-flex justify-space-between align-center !mb-3">
        <h1 class="font-bold capitalize truncate w-100">New Todo</h1>
        <img
          src="../../public/close.png"
          alt="close"
          class="h-6 w-6 cursor-pointer"
          @click="closeModal"
        />
      </v-card-title>

      <v-card-text>
        <v-form ref="form" lazy-validation>
          <v-text-field
            v-model="newTodo"
            label="Enter your new posts title..."
            @keydown.enter="addTodo"
            variant="outlined"
            density="compact"
            hide-details="auto"
            :rules="[(v) => !!v?.trim() || '* This field cannot be left blank']"
          />
        </v-form>
      </v-card-text>
      <v-card-actions class="w-full flex items-center justify-end">
        <v-btn @click="addTodo()">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import axios from "axios";

export default {
  name: "NewTodo",
  data() {
    return {
      dialog: false,
      newTodo: "",
    };
  },

  methods: {
    openModal() {
      this.dialog = true;
    },

    closeModal() {
      this.dialog = false;
    },

    async addTodo() {
      const isValid = await this.$refs.form.validate();
      if (!isValid?.valid) {
        return;
      } else {
        try {
          await axios.post(
            "http://127.0.0.1:8000/api/todo/new/",
            {
              title: this.newTodo,
              completed: false,
            },
            {
              headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
              },
            }
          );

          this.newTodo = "";
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
