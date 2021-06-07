<template>
  <div>
    <header class="AppNav">
      <Nav />
    </header>
    <main class="container">
      <router-view/>
    </main>
  </div>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap");
* {
  font-family: "Nanum Gothic", sans-serif;
}
.app {
  width: 100vw;
  height: 100vh;
}
</style>

<script>
import Nav from "./components/Nav.vue";
export default {
  components: {
    Nav,
  },
};
</script>