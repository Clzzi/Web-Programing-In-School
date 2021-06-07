<template>
  <div class="todo">
    <h1>Todo App</h1>
    <TodoInput />
    <TodoList />
    <TodoFooter />
  </div>
</template>

<script>
import TodoInput from "@/components/TodoInput";
import TodoList from "@/components/TodoList";
import TodoFooter from "@/components/TodoFooter";
export default {
  name: "Todo",
  components: {
    TodoInput,
    TodoList,
    TodoFooter,
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