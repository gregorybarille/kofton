<template>
  <v-app id="inspire">
      <TheNavBar></TheNavBar>
      <v-main>
        <v-container fluid>
          <v-fade-transition mode="out-in">
            <router-view class="text-xs-center" :jsonData="jsonData"></router-view>
          </v-fade-transition>
        </v-container>
      </v-main>
      <TheFooter></TheFooter>
    </v-app>
</template>

<script>
import TheNavBar from "./components/TheNavBar.vue";
import TheFooter from "./components/TheFooter.vue";
import json from "../public/data.json";
console.log('toto')
export default {
  name: "app",
  data() {
    return {
      jsonData: json
    };
  },
  components: {
    TheNavBar,
    TheFooter
  }
};
</script>

<style>
h1,
strong {
  color: #357ab7;
}
</style>
