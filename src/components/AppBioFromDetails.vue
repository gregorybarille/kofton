<template>
  <v-card>
    <v-img class="white--text" height="200px" :src="`/${jsonData[$route.params.name].images.bio}`">
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
        <span v-html="decodeHTML(jsonData[$route.params.name].bio)"></span>
      </div>
    </v-card-title>
    <v-card-actions>
      <v-flex v-for="(value, key) in jsonData[$route.params.name].social" :key="key" xs4 d-flex>
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
      decodeHTML: function(html) {
        var txt = document.createElement("textarea");
        txt.innerHTML = html;
        return txt.value;
      }
    };
  },
  props: {
    jsonData: {
      type: Object
    },
    name: {
      type: String
    }
  }
};
</script>
