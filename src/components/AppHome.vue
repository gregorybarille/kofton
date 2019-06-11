<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat>
        <v-card-text class="text-xs-center">
          <h1 primary-title>Dernières Sorties</h1>
        </v-card-text>
        <carousel :autoplay="true" :centerMode="true" :loop="true" :perPage="1">
          <slide v-for="{artiste} in jsonData.sorties.slice(0,3)" :key="artiste">
            <v-card flat :to="{path: `/artistes/${artiste}/media`}">
              <v-img
                :src="jsonData.artistes[artiste].images.titre"
                :alt="`${artiste} - ${jsonData.artistes[artiste].sortie.titre} `"
                :title="`${artiste} - ${jsonData.artistes[artiste].sortie.titre}`"
                contain
                flat
                height="65vh"
              ></v-img>
            </v-card>
          </slide>
        </carousel>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";

export default {
  components: {
    Carousel,
    Slide
  },
  props: {
    jsonData: {
      type: Object
    }
  }
};
</script>
<style scoped>
.carrousel_click {
  width: "100%";
  height: "100%";
}
</style>
