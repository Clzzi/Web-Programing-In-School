<template>
  <div>
    <header class="AppNav">
      <Nav />
    </header>
    <main class="container">
      <router-view />
    </main>
  </div>
</template>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap");
* {
  font-family: "Nanum Gothic", sans-serif;
  box-sizing: border-box;
}
.app {
  width: 100vw;
  height: 100vh;
  min-width: 1440px;
}
.container {
  display: block;
  min-width: 1920px;
  max-width: 100vw;
  width: 100%;
  justify-content: center;
  text-align: center;
  align-items: center;
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