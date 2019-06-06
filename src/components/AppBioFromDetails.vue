<template>
  <div>
    <v-card-title class="text-xs-left">
      <div>
        <span v-html="decodeHTML(artist.bio)"></span>
      </div>
    </v-card-title>
  </div>
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
    artist: {
      type: Object
    },
    name: {
      type: String
    }
  }
};
</script>
