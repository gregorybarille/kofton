<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat :img="`/${this.jsonData.artistes[this.name].images.bio}`">
        <v-flex xs12>
          <v-card class="black--text">
            <v-card-title primary-title class="py-0 artisteInfo">
              <span class="headline">{{ $route.params.name }}</span>
              <v-spacer></v-spacer>
              <v-btn
                v-for="(value, key) in this.jsonData.artistes[this.name].social"
                :key="value"
                :href="`${value}`"
                target="_blank"
                icon
              >
                <v-icon>{{icons[key]}}</v-icon>
              </v-btn>
            </v-card-title>
            <v-layout>
              <v-flex xs2 offset-xs5></v-flex>
            </v-layout>
          </v-card>
        </v-flex>
        <v-tabs v-model="active" color="grey lighten-5" light slider-color="yellow">
          <v-tab :to="{path: `/artistes/${name}/bio`}">Biographie</v-tab>
          <v-tab :to="{path: `/artistes/${name}/media`}">Titre</v-tab>
        </v-tabs>
        <router-view :artist="this.jsonData.artistes[this.name]"></router-view>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      icons: {
        facebook: "fab fa-facebook-square fa-2x",
        instagram: "fab fa-instagram fa-2x",
        twitter: "fab fa-twitter fa-2x",
        youtube: "fab fa-youtube fa-2x",
        soundcloud: "fab fa-soundcloud fa-2x"
      }
    };
  },
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
<style scoped>
.artisteInfo {
  background-color: white;
  opacity: 0.8;
}
</style>
