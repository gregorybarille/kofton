<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex v-for="{artiste} in jsonData.sorties" :key="artiste">
              <v-card :to="{path: `/artistes/${artiste}/media`}">
                <!-- <v-card flat> -->
                <iframe
                  scrolling="no"
                  frameborder="0"
                  allowtransparency="true"
                  :src="`https://www.deezer.com/plugins/player?format=square&autoplay=false&playlist=false&width=300&height=300&color=ff0000&layout=dark&size=medium&type=${jsonData.artistes[artiste].sortie.platform.deezer}&app_id=1`"
                  width="300"
                  height="300"
                ></iframe>
              </v-card>
              <v-divider></v-divider>
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
