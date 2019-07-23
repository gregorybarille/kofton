<template>
  <v-card>
    <v-navigation-drawer
      class="hidden-md-and-up temporary"
      disable-resize-watcher
      v-model="drawer"
      width="150vw"
      right
      app
    >
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
              <v-btn flat :to="{path: '/playlist' }">Playlist</v-btn>
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
      <v-layout>
        <v-flex d-inline-flex xs10 sm8 md8 offset-xs2 offset-sm4 offset-md2>
          <v-toolbar-title>
            <v-btn flat class="logo_button" active-class="active" :to="{path: '/home'}">
              <img src="/assets/images/logo_kofton.png" />
            </v-btn>
          </v-toolbar-title>
          <v-toolbar-items class="hidden-sm-and-down py-0">
            <v-btn
              class="white-button"
              active-class="active"
              flat
              :to="{path: '/artistes'}"
              height="100%"
            >Artistes</v-btn>
            <v-btn
              class="white-button"
              active-class="active"
              flat
              depressed
              :to="{path: '/demo' }"
            >Demo</v-btn>
            <v-btn
              class="white-button"
              active-class="active"
              flat
              depressed
              :to="{path: '/playlist' }"
            >Playlist</v-btn>
            <v-btn
              class="white-button"
              active-class="active"
              flat
              depressed
              :to="{path: '/sorties' }"
            >Sorties</v-btn>
            <v-btn
              class="white-button"
              active-class="active"
              flat
              depressed
              :to="{path: '/contact' }"
            >Contact</v-btn>
          </v-toolbar-items>
        </v-flex>
      </v-layout>
      <v-toolbar-side-icon class="hidden-md-and-up" @click.stop="drawer = !drawer"></v-toolbar-side-icon>
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
  background-color: #357ab7;
}
.white-button {
  color: white;
}

.active {
  color: black;
}
</style>
