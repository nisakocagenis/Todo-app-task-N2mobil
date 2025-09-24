import { createStore } from "vuex";
import axios from "axios";

const token = localStorage.getItem("token");
if (token) {
  axios.defaults.headers.common["Authorization"] = `Token ${token}`;
}

const store = createStore({
  state() {
    return {
      selectedUser: null,
    };
  },
  mutations: {
    setSelectedUser(state, user) {
      state.selectedUser = user;
    },
  },
  getters: {
    getSelectedUser(state) {
      return state.selectedUser;
    },
  },
  actions: {
    async setSelectedUserById({ state, commit }, userId) {
      if (state.selectedUser && state.selectedUser.id === Number(userId))
        return;

      try {
        const response = await axios.get("http://127.0.0.1:8000/api/user/");

        const user = response.data.find((u) => u.id === Number(userId));

        if (user) {
          commit("setSelectedUser", user);
        } else {
          console.warn(`Kullanıcı bulunamadı (id=${userId})`);
        }
      } catch (error) {
        console.error("Kullanıcı listesi alınırken hata:", error);
      }
    },
  },
});

export { store };
