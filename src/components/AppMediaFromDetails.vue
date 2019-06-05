<template>
  <v-layout>
    <v-flex xs12 sm12>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex v-if="name == 'HezCut'">
              <iframe
                scrolling="no"
                frameborder="0"
                allowtransparency="true"
                :src="`https://www.deezer.com/plugins/player?format=square&autoplay=false&playlist=false&width=300&height=300&color=ff0000&layout=dark&size=medium&type=${artist.sortie.platform.deezer}&app_id=1`"
                width="600"
                height="600"
              ></iframe>
            </v-flex>
            <v-flex v-else>
              <iframe
                width="600"
                height="600"
                scrolling="no"
                frameborder="no"
                allow="autoplay"
                :src="`https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/${artist.sortie.platform.soundcloud}&color=%23007eff&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true`"
              ></iframe>
            </v-flex>
            <v-divider></v-divider>
            <v-flex>
              <iframe
                width="600"
                height="400"
                :src="`https://www.youtube-nocookie.com/embed/${artist.sortie.platform.youtube}`"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
              ></iframe>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    artist: {
      type: Object
    },
    name: {
      type: String
    }
  }
};
</script>

<style scoped>
#spotify {
  background: url(/assets/icons/spotify.png) no-repeat;
  background-size: contain;
  background-position: left;
}

#deezer {
  background: url(/assets/icons/deezer.png) no-repeat;
  background-size: contain;
  background-position: center;
}

#applemusic {
  background: url(/assets/icons/applemusic.png) no-repeat;
  background-size: contain;
  background-position: center;
}

#soundcloud {
  background: url(/assets/icons/soundcloud.png) no-repeat;
  background-size: contain;
  background-position: left;
}

#amazon {
  background: url(/assets/icons/amazon.png) no-repeat;
  background-size: contain;
  background-position: center;
}
</style>
