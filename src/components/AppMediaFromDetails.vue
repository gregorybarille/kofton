<template>
  <v-layout>
    <v-flex xs10 sm6>
      <v-img aspect-ratio="1" contain :src="`/${artist.images.titre}`"></v-img>
      <v-divider light></v-divider>
    </v-flex>
    <v-flex xs2 sm6>
      <v-layout column align-center justify-center fill-height>
        <v-btn flat small :href="value" target="_blank">
          <v-icon>fa facebook</v-icon>
        </v-btn>
        <v-btn flat small :href="value" target="_blank">
          <v-icon>fa facebook</v-icon>
        </v-btn>
        <v-btn flat small :href="value" target="_blank">
          <v-icon>fa facebook</v-icon>
        </v-btn>
        <v-btn flat small :href="value" target="_blank">
          <v-icon>fa facebook</v-icon>
        </v-btn>
      </v-layout>
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
