<template>
  <v-layout>
    <v-flex xs12 sm12>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex>
              <iframe
                scrolling="no"
                frameborder="0"
                allowtransparency="true"
                :src="`https://www.deezer.com/plugins/player?format=square&autoplay=false&playlist=false&width=300&height=300&color=ff0000&layout=dark&size=medium&type=${artist.sortie.platform.deezer}&app_id=1`"
                width="600"
                height="600"
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
