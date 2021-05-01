<template>
  <div id="navigation">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="/">Movie App</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div
        class="collapse navbar-collapse my-2 my-lg-0"
        id="navbarSupportedContent"
      >
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a
              class="navbar-brand"
              href="/addPage.vue"
              
            >
              <router-link to="addPage">Add Movie</router-link></a
            >
          </li>
        </ul>
      </div>
    </nav>
  </div>

  <!-- <li class="nav-item active">
            <a class="navbar-brand" href="/">Home</a>
          </li> -->
</template>

<script>
export default {};
</script>