<template>
  <div
    class="d-flex justify-center align-center !p-4"
    style="height: 100vh; width: 100%"
  >
    <v-card class="bg-[#4F359B] rounded-lg w-[32rem] !p-6">
      <div class="flex gap-2 justify-center">
        <img
          class="w-8 h-8"
          src="/Users/nisakocagenis/Downloads/album-pr/frontend/public/logo.png"
          alt="logo"
        />
        <div class="font-bold text-2xl text-[#4F359B] m-6">Login</div>
      </div>
      <!-- username -->
      <div>
        <div class="text-subtitle-1 text-medium-emphasis">Account</div>
        <v-text-field
          density="compact"
          placeholder="Username"
          variant="outlined"
          v-model="username"
          @keydown.enter="login"
        ></v-text-field>
      </div>
      <!-- password -->
      <div>
        <div
          class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
        >
          Password
        </div>
        <v-text-field
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          v-model="password"
          placeholder="Enter your password"
          variant="outlined"
          @click:append-inner="visible = !visible"
          @keydown.enter="login"
        ></v-text-field>

        <!-- login butonu -->
        <div>
          <v-btn
            class="mb-8"
            color="#4F359B"
            size="large"
            variant="tonal"
            @click="login"
            block
          >
            Log In
          </v-btn>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const visible = ref(false);
const router = useRouter();

export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: "",
      message: "",
      users: [],
      selectedUser: "",
    };
  },

  methods: {
    goHome() {
      this.$router.push("/Todos");
    },

    async login() {
      try {
        const res = await axios.post("http://127.0.0.1:8000/api/login/", {
          username: this.username,
          password: this.password,
        });

        if (res.data.success) {
          localStorage.setItem("token", res.data.token);
          localStorage.setItem("user", JSON.stringify(res.data.user));

          // header’a ekle
          axios.defaults.headers.common[
            "Authorization"
          ] = `Token ${res.data.token}`;

          this.message = "Giriş başarılı!";
          this.$router.push({ name: "Todos" });
        }
      } catch (err) {
        if (err.response && err.response.status === 401) {
          this.message = "Kullanıcı adı veya şifre yanlış!";
        } else {
          this.message = "Sunucu hatası!";
        }
      }
    },
  },
};

//   async login() {
//     try {
//       const res = await axios.get("http://localhost:8000/api/user/", {
//         username: this.selectedUser || this.username,
//         password: this.password,
//       });

//       if (res.data.success) {
//         this.message = "Giriş başarılı!";
//         this.$router.push("/Users");
//         localStorage.setItem(
//           "user",
//           JSON.stringify({
//             id: 1,
//             name: this.username,
//             email: this.email || "example@mail.com",
//             phone: this.phone || "12345678",
//             address: { street: "Test Street" },
//             company: { name: "Test Company" },
//             website: "www.example.com",
//           })
//         );
//       }
//     } catch (err) {
//       if (err.response && err.response.status === 401) {
//         this.message = "Kullanıcı adı veya şifre yanlış!";
//       } else {
//         this.message = "Sunucu hatası!";
//       }
//     }
//   },
// },
// };
</script>
