<template>
  <div class="todo">
    <TodoHeader />
    <TodoTitle />
    <TodoInput />
    <TodoController />
    <TodoList />
    <TodoFooter />
  </div>
</template>

<script>
import TodoHeader from "../components/TodoHeader";
import TodoTitle from "../components/TodoTitle";
import TodoInput from "../components/TodoInput";
import TodoList from "../components/TodoList";
import TodoController from "../components/TodoController";
import TodoFooter from "../components/TodoFooter";

export default {
  name: "ToDoList",
  components: {
    TodoHeader,
    TodoTitle,
    TodoInput,
    TodoController,
    TodoList,
    TodoFooter,
  },
};
</script>
