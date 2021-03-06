import Vue from "vue";
import "./plugins/vuetify";
import App from "./App.vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

Vue.config.productionTip = false;

import AppArtistes from "./components/AppArtistes";
import AppDemo from "./components/AppDemo";
import AppMedia from "./components/AppMedia";
import AppHome from "./components/AppHome";
import AppPlaylist from "./components/AppPlaylist";
import AppConditions from "./components/AppConditions";
import AppLegal from "./components/AppLegal";
import AppTraitement from "./components/AppTraitement";
import AppDetailsFromArtistes from "./components/AppDetailsFromArtistes";
import AppContact from "./components/AppContact";
import AppBioFromDetails from "./components/AppBioFromDetails";
import AppSocialFromBio from "./components/AppSocialFromBio";
import AppMediaFromDetails from "./components/AppMediaFromDetails";

let router = new VueRouter({
  mode: "hash",
  scrollBehavior() {
    return new Promise(resolve =>
      setTimeout(() => resolve({ x: 0, y: 0 }), 250)
    );
  },
  routes: [
    {
      path: "/artistes",
      name: "Artistes",
      component: AppArtistes,
      props: true
    },
    {
      path: "/artistes/:name",
      name: "Artistes Details",
      component: AppDetailsFromArtistes,
      props: true,
      children: [
        {
          path: "bio",
          name: "Biographie",
          component: AppBioFromDetails,
          props: true
        },
        {
          path: "media",
          name: "media",
          component: AppMediaFromDetails,
          props: true
        },
        {
          path: "social",
          name: "Social",
          component: AppSocialFromBio,
          props: true
        }
      ]
    },
    {
      path: "/demo",
      name: "Demo",
      component: AppDemo,
      props: true
    },
    {
      path: "/playlist",
      name: "Playlist",
      component: AppPlaylist
    },
    {
      path: "/sorties",
      name: "Sorties",
      component: AppMedia
    },
    {
      path: "/contact",
      name: "Contact",
      component: AppContact
    },
    {
      path: "/home",
      name: "Accueuil",
      component: AppHome
    },
    {
      path: "/mentions-legales",
      name: "Mentions Légales",
      component: AppLegal
    },
    {
      path: "/conditions-generales",
      name: "Conditions générales",
      component: AppConditions
    },
    {
      path: "/politique-traitement",
      name: "Politique de traitement",
      component: AppTraitement
    },
    { path: "*", redirect: "/home" }
  ]
});

new Vue({
  render: h => h(App),
  router
}).$mount("#app");
