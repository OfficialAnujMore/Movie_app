<template>
  <div id="app">
    <table class="table">
      <thead>
        <th>Name</th>
        <th>Director</th>
        <th>Genere</th>
        <th>Rating</th>
        <th>Release Date</th>
      </thead>
      <tbody>
   
        <tr v-for="movie in movies" v-bind:key="movie.id" >
          <td>{{ movie.name }}</td>
          <td>{{ movie.director }}</td>
          <td>{{ movie.genere }}</td>
          <td>{{ movie.rating }}</td>
          <td>{{ movie.release_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",

  data() {
    return {
      movies: [],
    };
  },
  async created(){
    var response = await fetch('http://127.0.0.1:8000/api/movies/')
    this.movies = await response.json();
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
