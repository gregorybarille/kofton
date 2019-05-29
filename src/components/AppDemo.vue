<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card flat>
        <v-img src="/assets/images/unclesam.png" contain></v-img>

        <v-card-title primary-title>
          <v-card-text>
            <v-icon>fas fa-feather-alt</v-icon>
            <span>Songwriter</span>
            <v-icon>fas fa-microphone-alt</v-icon>
            <span>Chanteur</span>
            <v-icon>fas fa-guitar</v-icon>
            <span>Groupe ou Beatmeaker</span>
            <v-icon>fas fa-magic</v-icon>
            <span>Artistes</span>
          </v-card-text>
          <v-card-text>
            <h2>Vous êtres au bon endroit !</h2>
          </v-card-text>
        </v-card-title>
        <v-divider></v-divider>
        <v-card flat>
          <v-card-title primary-title class="justify-center">
            <h3 class="headline mb-0">Contactez-nous</h3>
          </v-card-title>
          <v-card-text>
            <div>
              <p>
                <strong>
                  <u>Comment nous transmettre vos maquettes ?</u>
                </strong>
                <br>Kofton Music met à votre disposition une adresse dédiée :
                <br>
                <a href="mailto:contact@kofton-music.com">contact@kofton-music.com</a>
                <br>
              </p>
              <div class="text-xs-left">
                <p>Dans la mesure du possible n'envoyez pas un fichier son ou vidéo en pièce jointe de l'email, car il risque de ne pas pouvoir être reçu du fait de sa taille importante (taille maximum pour envoie par email est de 5 Mo, en Mp3 et un titre par email).</p>
                <p>Insérez dans votre email un lien vers un blog ou un site où nous pourrons écouter votre musique (si vous n'avez pas de blog, vous pouvez utiliser Soundcloud ou We Transfer).</p>
                <p>Si votre maquette venait à susciter l'intérêt de notre label, nous ne manquerions pas de vous recontacter. Aucune autre réponse ou information relative à ces maquettes ne sera transmise par téléphone ou par email.</p>
              </div>
            </div>
          </v-card-text>
        </v-card>
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
span {
  font-size: 1.5rem;
  margin-right: 15px;
}
</style>
