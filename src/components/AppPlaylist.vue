<template>
  <v-layout>
    <v-flex xs12 sm8 offset-sm2>
      <v-card flat id="playlist">
        <iframe
          width="100%"
          height="100%"
          scrolling="no"
          frameborder="no"
          allow="autoplay"
          src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/users/554426010&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"
        ></iframe>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {};
</script>
<style scoped>
html {
  overflow-y: auto;
}
#playlist {
  top: 0;
  bottom: 0;
  height: 75vh;
}
</style>
