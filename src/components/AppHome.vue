<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat>
        <v-carousel height="75vh" hide-delimiters>
          <v-carousel-item
            v-for="{artiste} in jsonData.sorties"
            :key="artiste"
            :src="jsonData.artistes[artiste].images.titre"
          ></v-carousel-item>
        </v-carousel>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: {
    jsonData: {
      type: Object
    }
  }
};
</script>
<style scoped>
</style>
