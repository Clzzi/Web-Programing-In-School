<template>
  <div class="Todo">
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
  .Todo {
    display: inline-block;
    width: 600px;
    height: 600px;
    min-width: 600px;
    min-height: 600px;
    background-color: #bac8ff;
    border-radius: 5px;
    box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px;
  }
</style>