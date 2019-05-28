import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

Vue.config.productionTip = false

import AppArtistes from './components/AppArtistes'
import AppContest from './components/AppContest'
import AppDemo from './components/AppDemo'
import AppPlaylists from './components/AppPlaylists'
import AppSorties from './components/AppSorties'
import AppVideos from './components/AppVideos'
import AppHome from './components/AppHome'
import AppConditions from './components/AppConditions'
import AppLegal from './components/AppLegal'
import AppTraitement from './components/AppTraitement'
import AppBioFromArtistes from './components/AppBioFromArtistes'
import AppContact from './components/AppContact'

let router = new VueRouter({
  mode: 'history',
  scrollBehavior() {
    return new Promise(resolve =>
      setTimeout(() => resolve({ x: 0, y: 0 }), 250)
    );
  },
  routes: [
    {
      path: '/artistes',
      name: 'Artistes',
      component: AppArtistes,
      props: true,
    },
    {
      path: '/artistes/:name',
      name: 'Artistes Bio',
      component: AppBioFromArtistes,
      props: true
    },
    {
      path: '/contest',
      name: 'Contest',
      component: AppContest,
    },
    {
      path: '/demo',
      name: 'Demo',
      component: AppDemo,
    },
    {
      path: '/playlists',
      name: 'Playlists',
      component: AppPlaylists,
    },
    {
      path: '/sorties',
      name: 'Sorties',
      component: AppSorties,
    },
    {
      path: '/videos',
      name: 'Videos',
      component: AppVideos,
    },
    {
      path: '/contact',
      name: 'Contact',
      component: AppContact,
    },
    {
      path: '/home',
      name: 'Accueuil',
      component: AppHome,
    },
    {
      path: '/mentions-legales',
      name: 'Mentions Légales',
      component: AppLegal,
    },
    {
      path: '/conditions-generales',
      name: 'Conditions générales',
      component: AppConditions,
    },
    {
      path: '/politique-traitement',
      name: 'Politique de traitement',
      component: AppTraitement,
    },
    { path: '*', redirect: '/home' }
  ]
})

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
