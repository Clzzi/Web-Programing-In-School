<template>
  <div class="nav">
    <div class="nav-Logo">Vue Exam</div>
    <div class="nav-Content">
      <router-link to="/">ToDoList</router-link> | 
      <router-link to="/intro">IntroDuce</router-link>
    </div>
    <router-view />
  </div>
</template>

<style lang="scss">
/* .nav {
  width: 100vw;
  height: 60px;
  display: flex;
  text-align: center;
  align-items: center;
  vertical-align: middle;
  border-bottom: 1px solid black;
  &-Logo {
    display: flex;
    flex-wrap: 1;
    font-size: 2rem;
    font-weight: bold;
    color: #0080ff;
    margin-right: 30px;
    height: 100%;
    line-height: 60px;
    margin-left: 30px;
  }
  &-Content {
    height: 100%;
    line-height: 60px;
    margin-left: 35%;
    :nth-child(1) {
      padding-right: 30px;
    }
    & > a {
      font-size: 1.25rem;
      text-decoration: none;
      color: #1ec0ff;
      &.router-link-exact-active {
        color: #0080ff;
      }
    }
  }
} */
</style>
