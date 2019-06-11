<template>
  <div id="app">
    <v-app id="inspire">
      <TheNavBar></TheNavBar>
      <v-content>
        <v-container fluid>
          <v-fade-transition mode="out-in">
            <router-view class="text-xs-center" :jsonData="jsonData"></router-view>
          </v-fade-transition>
        </v-container>
      </v-content>
      <TheFooter></TheFooter>
    </v-app>
  </div>
</template>

<script>
import TheNavBar from "./components/TheNavBar.vue";
import TheFooter from "./components/TheFooter.vue";
import json from "../public/data.json";
export default {
  name: "App",
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
