<template>
  <div class="container">
    <form @submit.prevent="createMovie" name="Form">
      <!-- @submit.prevent="createMovie" -->
      <div class="form-group">
        <br />
        <input
          type="text"
          minlength="2"
          maxlength="100"
          name="movieName"
          class="form-control  field"
          id="movieName"
          aria-describedby="emailHelp"
          placeholder="Movie Name"
          v-model="movie.name"
        />
      </div>
      <div class="form-group">
        <br />
        <input
          type="text"
          minlength="2"
          maxlength="100"
          class="form-control field"
          name="directorName"
          id="directorName"
          aria-describedby="emailHelp"
          placeholder="Director Name"
          v-model="movie.director"
        />
      </div>
      <div class="form-group">
        <br />
        <input
          type="text"
          minlength="2"
          maxlength="100"
          class="form-control field"
          id="genere"
          name="genere"
          aria-describedby="emailHelp"
          placeholder="Genere"
          v-model="movie.genere"
        />
      </div>
      <div class="form-group">
        <br />
        <input
          type="number"
          min="1"
          max="5"
          class="form-control field"
          id="rating"
          name="rating"
          aria-describedby="emailHelp"
          placeholder="Rating"
          v-model="movie.rating"
        />
      </div>
      <div class="form-group">
        <br />
        <input
          type="date"
          class="form-control field"
          id="date"
          name="date"
          aria-describedby="emailHelp"
          placeholder="Date"
          v-model="movie.release_date"
        />
      </div>
      <button type="submit" class="btn btn-primary submitButton">Submit</button>
      <!-- @click=createMovie() -->
    </form>
  </div>

  <!-- d-flex justify-content-center" -->
</template>

<style scoped src= "../assets/css/addPage.css">

</style>
<script>
export default {
  name: "Add",
  data() {
    return {
      movie: {
        name: "",
        director: "",
        genere: "",
        rating: "",
        release_date: "",
      },
      movies: [],
    };
  },

  async created() {
    var response = await fetch("http://127.0.0.1:8000/api/movies/");
    this.movies = await response.json();
  },

  methods: {
    async createMovie() {
      var movieName = document.forms["Form"]["movieName"].value;
      var directorName = document.forms["Form"]["directorName"].value;
      var genere = document.forms["Form"]["genere"].value;
      var rating = document.forms["Form"]["rating"].value;
      var date = document.forms["Form"]["date"].value;

      if (
        (movieName == null || movieName == "",
        directorName == null || directorName == "",
        genere == null || genere == "",
        rating == null || rating == "",
        date == null || date == "")
      ) {
        alert("Please Fill All Required Field");
        return false;
      } else {
        var response = await fetch("http://127.0.0.1:8000/api/movies/", {
          method: "post",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.movie),
        });

        this.movies.push(await response.json());

        console.log("hello");
        alert("Movie Details has been added succesfully!!");
        document.getElementById("movieName").value = "";
        document.getElementById("directorName").value = "";
        document.getElementById("genere").value = "";
        document.getElementById("rating").value = "";
        document.getElementById("date").value = "";
      }
    },
  },
};
</script>
