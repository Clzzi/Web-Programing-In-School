<template>
  <div class="todo">
    <TodoTitle />
    <TodoHeader />
    <TodoInput />
    <TodoList />
  </div>
</template>

<script>
import TodoInput from "@/components/TodoInput";
import TodoList from "@/components/TodoList";
import TodoHeader from "@/components/TodoHeader";
import TodoTitle from "@/components/TodoTitle";
export default {
  name: "Todo",
  components: {
    TodoInput,
    TodoList,
    TodoHeader,
    TodoTitle,
  },
};
</script>

<style lang="scss">

</style>