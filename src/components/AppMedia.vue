<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex v-for="{artiste} in jsonData.sorties" :key="artiste">
              <v-card :to="{path: `/artistes/${artiste}/media`}">
                <v-img aspect-ratio="1.5" contain :src="jsonData.artistes[artiste].images.titre"></v-img>
                <v-divider light></v-divider>
                <v-layout>
                  <v-flex xs12 sm8 offset-sm2 v-if="artiste == 'HezCut'">
                    <iframe
                      scrolling="no"
                      frameborder="0"
                      allowtransparency="true"
                      src="https://www.deezer.com/plugins/player?format=classic&autoplay=false&playlist=true&width=700&height=350&color=ff0000&layout=&size=medium&type=tracks&id=660748242&app_id=1"
                      width="100%"
                      height="166"
                    ></iframe>
                  </v-flex>

                  <v-flex xs12 sm8 offset-sm2 v-else>
                    <iframe
                      width="100%"
                      height="166"
                      scrolling="no"
                      frameborder="no"
                      allow="autoplay"
                      :src="`https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/${jsonData.artistes[artiste].sortie.platform.soundcloud}&color=%23007eff&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true`"
                    ></iframe>
                  </v-flex>
                </v-layout>
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

iframe {
}
</style>
