<template>
  <header class="header">
    <span class="header-Title">My ToDo</span>
    <div class="header-Date">{{ date }}</div>
  </header>
</template>

<script>
  export default {
    data() {
      return {
        date: ""
      }
    },
    created() {
      const now = new Date();
      const month = now.getMonth() + 1;
      const date = now.getDate();
      const weekList = new Array("Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
      const week = weekList[now.getDay()];
      this.date = `${month}-${date} ${week}`;
    }
  }
</script>
