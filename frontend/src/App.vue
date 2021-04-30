<template>
  

  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Movie App</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="">Home</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <table class="table">
      <thead>
        <th>Name</th>
        <th>Director</th>
        <th>Genere</th>
        <th>Rating</th>
        <th>Release Date</th>
      </thead>
      <tbody>
        <tr v-for="movie in movies" v-bind:key="movie.id">
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
