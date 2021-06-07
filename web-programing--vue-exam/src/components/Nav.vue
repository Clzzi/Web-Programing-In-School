<template>
  <div class="nav">
    <div class="nav-Logo">Vue Exam</div>
    <div class="nav-Content">
      <router-link to="/" active-class="active" exact>ToDoList</router-link>
      <router-link to="/intro" active-class="active" exact
        >IntroDuce</router-link
      >
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.nav {
  width: 100%;
  min-width: 1440px;
  height: 73px;
  display: inline-block;
  padding: 0px 30px 0px 30px;
  align-items: center;
  justify-content: center;
  line-height: 65px;
  background-color: #a5d8ff;
  margin-bottom: 30px;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px;
  &-Logo {
    font-size: 2rem;
    font-weight: 700;
    color: #0080ff;
    height: 100%;
    display: inline-block;
    margin-right: 30px;
  }
  &-Content {
    display: inline-block;
    font-size: 1.25rem;
    font-weight: 700;
    & > a {
      transition: 0.2s;
      display: inline-block;
      height: 100%;
      text-decoration: none;
      margin-right: 15px;
      color: #1ec0ff;
    }
    & > a:hover {
      color: #0080ff;
    }
    .router-link-exact-active {
      color: #0080ff;
      border-bottom: 3px solid #0080ff;
    }
  }
}
</style>