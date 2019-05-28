<template>
  <v-card>
    <v-img class="white--text" height="200px" :src="`/${artist.images.bio}`">
      <v-container fill-height fluid>
        <v-layout fill-height>
          <v-flex xs12 align-end flexbox>
            <span class="headline">{{ $route.params.name }}</span>
          </v-flex>
        </v-layout>
      </v-container>
    </v-img>
    <v-card-title class="text-xs-left">
      <div>
        <span v-html="decodeHTML(artist.bio)"></span>
      </div>
    </v-card-title>
    <v-card-actions>
      <v-flex v-for="(value, key) in artist.social" :key="key" xs4 d-flex>
        <v-btn flat :href="value">
          <i v-bind:class="icons[key]"></i>
        </v-btn>
      </v-flex>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      icons: {
        facebook: 'fab fa-facebook-square fa-2x',
        instagram: 'fab fa-instagram fa-2x',
        twitter: 'fab fa-twitter fa-2x',
        youtube: 'fab fa-youtube fa-2x',
        soundcloud: 'fab fa-soundcloud fa-2x'
      },
      decodeHTML: function(html) {
        var txt = document.createElement("textarea");
        txt.innerHTML = html;
        return txt.value;
      }
    };
  },
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
