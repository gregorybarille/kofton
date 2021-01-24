import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

const opts = {
  iconfont: "md",
  theme: {
    primary: "#458AAB",
  },
};

export default new Vuetify(opts);
