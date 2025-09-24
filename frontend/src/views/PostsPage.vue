<template>
  <div class="flex h-screen w-full">
    <navigation-drawer></navigation-drawer>
    <!-- header kısmı -->
    <div class="flex flex-col w-full h-screen !pl-8 !pb-7">
      <header class="w-full h-10 my-7 flex items-center">
        <v-col cols="auto">
          <v-btn class="rounded-xl bg-[#4F359B]" @click="openPostModal">
            + New Post
          </v-btn>
          <new-post ref="newPostRef" @refresh="initial" />
        </v-col>
      </header>
      <!-- post yazıları  -->
      <div class="flex flex-col overflow-auto !pl-8 w-full">
        <div v-for="post in itemsList" :key="post.id" class="mb-6">
          <div class=" ">
            <h1 class="font-bold font capitalize">{{ post.title }}</h1>
            <div class="my-3">
              <div class="w-1/2">
                <p class="first-letter:uppercase font-thin">
                  {{ post.body.split(" ").slice(0, 14).join(" ") }} ...
                </p>
              </div>
              <div
                class="flex justify-end items-end cursor-pointer"
                @click="openModal(post)"
              >
                See More
                <right-ok-icon class="ml-6 mr-6" />
              </div>
            </div>
            <v-divider class="bg-color-[#5C6672] w-full mt-8"></v-divider>
          </div>
        </div>
      </div>
      <!-- Dialog Modal -->
      <more-details ref="moreDetailsRef"></more-details>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PostsIcon from "../components/postsIcon.vue";
import RightOkIcon from "../components/rightOkIcon.vue";
import moreDetails from "../components/moreDetails.vue";
import NavigationDrawer from "../components/NavigationDrawer.vue";
import NewPost from "../components/NewPost.vue";

export default {
  components: {
    NavigationDrawer,
    RightOkIcon,
    PostsIcon,
    moreDetails,
    NewPost,
  },

  data() {
    return {
      itemsList: [],
    };
  },

  mounted() {
    this.initial();
  },

  computed: {
    selectedUser() {
      return this.$store.state.selectedUser;
    },
  },
  methods: {
    openModal(post) {
      this.$refs.moreDetailsRef.openModal(post);
    },
    openPostModal() {
      this.$refs.newPostRef.openModal();
    },
    initial() {
      axios
        .get(`http://127.0.0.1:8000/api/post/post_list/`)
        .then((response) => {
          this.itemsList = response.data;
        })
        .catch((error) => {
          console.error("Veri alınırken hata oluştu:", error);
        });
    },
  },
};
</script>
