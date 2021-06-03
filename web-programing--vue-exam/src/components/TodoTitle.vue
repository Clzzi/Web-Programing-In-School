<template>
  <div class="TodoTitle">
    <span class="TodoTitle-message"> {{ msg }} </span>
    <span class="TodoTitle-Task">
      You have
      <span class="TodoTitle-Task-Number"> {{ totalTask }} </span>
      tasks today!
    </span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "Just Do It",
      totalTask: 5,
    };
  },
};
</script>
