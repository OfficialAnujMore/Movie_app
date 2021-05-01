<template>
  <div id="container ">
    <div class="card-columns p-5 border">
      <div
        class="card mb-3"
        style="max-width: 540px"
        v-for="movie in movies"
        v-bind:key="movie.id"
      >
        <div class="row no-gutters">
          <div class="col-md-4">
            <img
              src="https://lifewithmorecowbell.files.wordpress.com/2016/12/theatre-sign.jpg"
              class="card-img"
              alt="Image"
            />
          </div>
          <div class="col-md-8 p-2" id="movie_card">
            <div class="card-body">
              <div class="row d-flex justify-content-start">
                <h2
                  class="card-title d-flex justify-content-start"
                  id="movie_name"
                >
                  {{ movie.name }}
                </h2>
              </div>

              <div class="row d-flex justify-content-start">
                <h5
                  class="card-title d-flex justify-content-start"
                  id="director_name"
                >
                  Directed by - {{ movie.director }}
                </h5>
              </div>

              <div class="row d-flex justify-content-start">
                <h5 class="card-title" id="genere">
                  Genere - {{ movie.genere }}
                </h5>
              </div>

              <div class="row d-flex justify-content-start">
                <span
                  class="star fa fa-star fa-lg"
                  v-for="star in movie.rating"
                  v-bind:key="star.id"
                >
                </span>
              </div>

              <div class="row d-flex justify-content-end" id="release_date">
                <h10 class="card-title">{{ movie.release_date }}</h10>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped src= "../assets/css/homepage.css">
</style>
<script>
export default {
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