<template>
  <v-toolbar app flat>
    <v-toolbar-title>
      <img src="/assets/images/logo_kofton.png">
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat :to="{path: '/artistes'}">Artistes</v-btn>
      <v-btn flat :to="{path: '/contest' }">Contest</v-btn>
      <v-btn flat :to="{path: '/demo' }">Demo</v-btn>
      <v-btn flat :to="{path: '/playlists' }">Playlists</v-btn>
      <v-btn flat :to="{path: '/sorties' }">Sorties</v-btn>
      <v-btn flat :to="{path: '/contact' }">Contact</v-btn>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>search</v-icon>
      </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {};
</script>

<style scoped>
.v-toolbar__title {
  margin-left: 20%;
}

.v-toolbar__items {
  margin-right: 30%;
}

img {
  margin-top: 5px;
  height: 60px;
}
</style>
