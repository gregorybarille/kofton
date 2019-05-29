<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex v-for="{artiste} in jsonData.sorties" :key="artiste">
              <v-card>
                <v-img aspect-ratio="1.5" contain :src="jsonData.artistes[artiste].images.titre"></v-img>
                <v-divider light></v-divider>
                <v-card-actions>
                  <v-flex
                    v-for="(value, key) in jsonData.artistes[artiste].sortie.platform"
                    :key="key"
                    xs4
                    d-flex
                    justify-space-around
                  >
                    <v-btn flat small :href="value" target="_blank">
                      <v-icon>{{icons[key]}}</v-icon>
                    </v-btn>
                  </v-flex>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
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
        soundcloud: "fab fa-soundcloud fa-2x",
        spotify: "fab fa-spotify fa-2x",
        amazon: "fab fa-amazon fa-2x",
        itunes: "fab fa-itunes fa-2x",
        "google music": "fab fa-google-play fa-2x",
        deezer: "fab fa-music fa-2x"
      }
    };
  },
  props: {
    jsonData: {
      type: Object
    }
  }
};
</script>
<style scoped>
.fab {
  color: lightslategray;
}
.v-btn {
  padding: 0;
}
</style>
