<template>
  <div class="intro">
    <Introduce />
  </div>
</template>

<script>
import Introduce from "@/components/Introduce.vue";

export default {
  name: "Intro",
  components: {
    Introduce,
  },
};
</script>

<style lang="scss">
.intro {
  width: 100vw;
  height: 100vh;
  min-width: 1920px;
  max-width: 1920px;
}

</style>