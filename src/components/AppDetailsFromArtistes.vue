<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-img class="white--text" height="200px" :src="`/${this.jsonData[this.name].images.bio}`">
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xs12 align-end flexbox>
                <span class="headline">{{ $route.params.name }}</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <v-tabs v-model="active" color="primary" dark slider-color="yellow">
          <v-tab :to="{path: `/artistes/${name}/bio`}">Biographie</v-tab>
          <v-tab :to="{path: `/artistes/${name}/titre`}">Titre</v-tab>
          <v-tab :to="{path: `/artistes/${name}/videos`}">Videos</v-tab>
          <v-tab :to="{path: `/artistes/${name}/social`}">Social</v-tab>
        </v-tabs>
        <router-view :artist="this.jsonData[this.name]"></router-view>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    jsonData: {
      type: Object
    },
    name: {
      type: String
    }
  }
};
</script>
