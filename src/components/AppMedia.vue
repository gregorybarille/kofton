<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-container fluid grid-list-md>
          <v-layout column nowrap>
            <v-flex v-for="key in jsonData.sorties" :key="key">
              <v-card flat>
                <v-img contain :src="jsonData[key.artiste].images.titre"></v-img>
                <v-card-text></v-card-text>
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