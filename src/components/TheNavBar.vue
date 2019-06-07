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
      <v-toolbar-title>
        <img src="/assets/images/logo_kofton.png">
      </v-toolbar-title>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn class="white-button" flat :to="{path: '/artistes'}">Artistes</v-btn>
        <v-btn class="white-button" flat :to="{path: '/demo' }">Demo</v-btn>
        <v-btn class="white-button" flat :to="{path: '/playlist' }">Playlist</v-btn>
        <v-btn class="white-button" flat :to="{path: '/sorties' }">Sorties</v-btn>
        <v-btn class="white-button" flat :to="{path: '/contact' }">Contact</v-btn>
      </v-toolbar-items>
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
.v-toolbar__title {
  margin-left: 25%;
}
.v-toolbar__items {
  /* margin-left: auto; */
  /* margin-left: auto; */
}

img {
  margin-top: 5px;
  height: 60px;
}
.v-toolbar {
  background-color: #305b9e;
}
.white-button {
  color: white;
}
</style>
