<template>
  <div id="app">
    <div class="content">
      <div class="top-bar">
        <Navigation />
      </div>
    </div>
    <div class="content">
      <div class="top-bar">
        <Home />
      </div>
    </div>
  </div>
</template>



<script>
import Navigation from "./components/Navigation.vue";
import Home from "./components/HomePage.vue";
export default {
  name: "App",

  components: {
    Navigation,
    Home,
  },

  data() {
    return {
      movies: [],
    };
  },
  async created() {
    var response = await fetch("http://127.0.0.1:8000/api/movies/");
    this.movies = await response.json();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>








  