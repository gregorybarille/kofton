<template>
<v-layout>
      <v-flex xs12 sm6 offset-sm3>
        <v-card>
          <v-container grid-list-sm fluid>
            <v-layout row wrap>
              <v-flex
                v-for="(value, key) in jsonData"
                :key="key"
                xs4
                d-flex
              >
                <v-card flat tile class="d-flex">
                  <v-img
                    :src="jsonData[key].images.artiste"
                    aspect-ratio="1"
                    class="grey lighten-2"
                  >
                  </v-img>
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
  props: {
    jsonData: {
      type: Object
    }
  }
};
</script>

<style scoped>

</style>