<template>
  <div class="flex h-screen w-full">
    <navigation-drawer></navigation-drawer>
    <div class="flex flex-col w-full h-screen !pl-8 !pb-7">
      <header class="w-full h-10 my-7 flex items-center">
        <v-col cols="auto">
          <v-btn class="rounded-xl bg-[#4F359B]" @click="openModal">
            + New Todo
          </v-btn>
          <new-todo ref="newTodoRef" @refresh="initial" />
        </v-col>
      </header>

      <div class="w-full overflow-auto mt-13">
        <div v-for="list in itemsList" :key="list.id" class="flex items-center">
          <label class="flex items-center cursor-pointer">
            <input
              type="checkbox"
              v-model="list.completed"
              @change="toggleCompleted(list)"
              class="mr-2"
            />
            <div class="pa-2 first-letter:uppercase text-[#5C6672]">
              {{ list.title }}
            </div>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import NavigationDrawer from "../components/NavigationDrawer.vue";
import NewTodo from "../components/NewTodo.vue";

export default {
  components: { NavigationDrawer, NewTodo },
  data() {
    return {
      itemsList: [],
      showCard: false,
    };
  },
  mounted() {
    this.initial();
  },

  methods: {
    initial() {
      axios
        .get(`http://127.0.0.1:8000/api/todo/todo_list/`)
        .then((response) => {
          this.itemsList = response.data;
        })
        .catch((error) => {
          console.error("Veri alınırken hata oluştu:", error);
        });
    },
    openModal() {
      this.$refs.newTodoRef.openModal();
    },

    async toggleCompleted(item) {
      try {
        await axios.patch(`http://localhost:8000/api/todo/${item.id}/`, {
          completed: item.completed,
        });
        console.log("Güncellendi:", item);
      } catch (err) {
        console.error("Güncelleme hatası:", err);
      }
    },
  },
  computed: {
    selectedUser() {
      return this.$store.state.selectedUser.id;
    },
  },
};
</script>
