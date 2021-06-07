<template>
  <div class="todo">
    <h1>Todo App</h1>
    <TodoHeader />
    <TodoInput />
    <TodoList />
  </div>
</template>

<script>
import TodoInput from "@/components/TodoInput";
import TodoList from "@/components/TodoList";
import TodoHeader from "@/components/TodoHeader";
export default {
  name: "Todo",
  components: {
    TodoInput,
    TodoList,
    TodoHeader,
  },
};
</script>

<style lang="scss">
.todo {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>