<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat>
        <v-container grid-list-sm fluid>
          <v-layout row wrap>
            <v-flex v-for="(value, key) in jsonData.artistes" :key="key" xs12 md4 d-flex pa-2>
              <v-hover>
                <v-card
                  slot-scope="{ hover }"
                  flat
                  tile
                  :class="`d-flex elevation-${hover ? 5 : 0}`"
                  :to="{path: `/artistes/${key}/bio`}"
                >
                  <v-img :src="value.images.artiste" aspect-ratio="1" class="grey lighten-2"></v-img>
                </v-card>
              </v-hover>
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
    jsonData: {
      type: Object
    }
  }
};
</script>

<style scoped>
</style>
