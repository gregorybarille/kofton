  <template>
  <v-footer dark height="auto">
    <v-card flat tile class="primary accent-3 lighten-1 white--text text-xs-center" width="100%">
      <v-btn href="https://www.facebook.com/KoftonMusic/" target="_blank" icon>
        <i class="fab fa-facebook-square fa-2x"></i>
      </v-btn>
      <v-btn href="https://www.instagram.com/kofton_music/" target="_blank" icon>
        <i class="fab fa-instagram fa-2x"></i>
      </v-btn>
      <v-btn href="https://twitter.com/koftonmusic" target="_blank" icon>
        <i class="fab fa-twitter fa-2x"></i>
      </v-btn>
      <v-btn href="https://www.youtube.com/channel/UC_sVcEw4a9mZX2omxdDRhkA" target="_blank" icon>
        <i class="fab fa-youtube fa-2x"></i>
      </v-btn>
      <v-btn href="https://soundcloud.com/koftonmusic" target="_blank" icon>
        <i class="fab fa-soundcloud fa-2x"></i>
      </v-btn>

      <v-divider></v-divider>

      <v-card-text class="white--text py-0">
        &copy;2019 —
        <strong>Kofton Music</strong>
        <v-btn flat depressed :to="{path: '/mentions-legales' }">Mentions Légales</v-btn>
        <v-btn flat depressed :to="{path: '/politique-traitement' }">Politique de traitement</v-btn>
        <v-btn flat depressed :to="{path: '/conditions-generales' }">Conditions générales</v-btn>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

    <script>
export default {};
</script>

  <style scoped>
</style>
