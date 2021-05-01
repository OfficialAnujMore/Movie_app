<template>
  <div id="container ">
    

    

    <div class="card-columns center">
      <div
        class="card mb-3"
        style="max-width: 540px"
        v-for="movie in movies"
        v-bind:key="movie.id"
      >
        <div class="row no-gutters">
          <div class="col-md-4">
            <img
              src="https://thumbs.dreamstime.com/b/cinema-movie-reel-clapper-board-mm-film-background-unrolled-filmstrip-vertical-frame-56381025.jpg"
              class="card-img"
              alt="Image"
            />
          </div>
          <div class="col-md-8">
            <div class="card-body">
              <h2 class="card-title d-flex justify-content-center">
                {{ movie.name }}
              </h2>
              <h5 class="card-title">{{ movie.director }}</h5>

              <div class="row d-flex justify-content-center">
                <h4 class="">Genere</h4>
                <h4 class="card-title">. {{ movie.genere }}</h4>
              </div>

              <h4 class="card-title">Rating {{ movie.rating }} Outof 5</h4>
              <span
                class="star fa fa-star"
                v-for="star in movie.rating"
                v-bind:key="star.id"
              >
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<style>
.star {
  color: #f3d23e;
}
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