import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { store } from "./store.js";
import vuetify from "./plugins/vuetify";
import router from "./router.js";

const app = createApp(App);
app.use(store);
app.use(vuetify);
app.use(router);

app.mount("#app");
