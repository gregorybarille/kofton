<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-tabs v-model="active" color="primary" dark slider-color="yellow">
        <v-tab :to="{path: `/artistes/${name}/bio`}">Biographie</v-tab>
        <v-tab :to="{path: `/artistes/${name}/titre`}">Titre</v-tab>
        <v-tab :to="{path: `/artistes/${name}/videos`}">Videos</v-tab>
        <v-tab :to="{path: `/artistes/${name}/social`}">Social</v-tab>
      </v-tabs>
      <router-view :artist="this.jsonData[this.name]"></router-view>
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
