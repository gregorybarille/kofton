<template>
  <v-card>
    <v-navigation-drawer class="hidden-md-and-up" v-model="drawer" width="150px" left app>
      <v-layout>
        <v-flex>
          <v-list>
            <v-list-tile>
              <v-btn flat :to="{path: '/artistes'}">Artistes</v-btn>
            </v-list-tile>
            <v-list-tile>
              <v-btn flat :to="{path: '/demo' }">Demo</v-btn>
            </v-list-tile>
            <v-list-tile>
              <v-btn flat :to="{path: '/sorties' }">Sorties</v-btn>
            </v-list-tile>
            <v-list-tile>
              <v-btn flat :to="{path: '/contact' }">Contact</v-btn>
            </v-list-tile>
          </v-list>
        </v-flex>
      </v-layout>
    </v-navigation-drawer>
    <v-toolbar app fixed flat>
      <v-toolbar-side-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-layout>
        <v-flex d-inline-flex xs10 sm8 md8 offset-xs2 offset-sm4 offset-md2>
          <v-toolbar-title>
            <v-btn flat class="logo_button" :to="{path: '/home'}">
              <img src="/assets/images/logo_kofton.png">
            </v-btn>
          </v-toolbar-title>
          <v-toolbar-items class="hidden-sm-and-down">
            <v-btn class="white-button" flat :to="{path: '/artistes'}">Artistes</v-btn>
            <v-btn class="white-button" flat :to="{path: '/demo' }">Demo</v-btn>
            <v-btn class="white-button" flat :to="{path: '/playlist' }">Playlist</v-btn>
            <v-btn class="white-button" flat :to="{path: '/sorties' }">Sorties</v-btn>
            <v-btn class="white-button" flat :to="{path: '/contact' }">Contact</v-btn>
          </v-toolbar-items>
        </v-flex>
      </v-layout>
    </v-toolbar>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    drawer: false
  })
};
</script>

<style scoped>
.logo_button {
  height: 100%;
  margin: 0;
}
img {
  margin: 0;
  height: 60px;
}
.v-toolbar {
  background-color: #305b9e;
}
.white-button {
  color: white;
}
</style>
