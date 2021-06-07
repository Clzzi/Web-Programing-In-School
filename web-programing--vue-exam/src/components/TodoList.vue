<template>
  <ul class="TodoList">
    <li
      v-for="todo in getFilteredTodos"
      :key="todo.id"
      class="TodoList-TodoItem"
    >
      <input
        type="checkbox"
        v-model="todo.completed"
        class="TodoList-TodoItem-Check"
      />
      <div class="TodoList-TodoItem-EditContainer">
        <div
          @dblclick="setSelectedTodo(todo)"
          class="TodoList-TodoItem-EditContainer-Content"
        >
          {{ todo.text }}
        </div>
        <input
          type="text"
          @keyup="updateEditTodo"
          v-show="selectedTodo && todo.id === selectedTodo.id"
          class="TodoList-TodoItem-EditContainer-EditInput"
          autofocus
        />
      </div>
      <button
        type="button"
        @click="removeTodo(todo.id)"
        class="TodoList-TodoItem-DelBtn"
      >
        delete
      </button>
    </li>
  </ul>
</template>

<script>
import { mapGetters, mapActions, mapState } from "vuex";
export default {
  name: "TodoList",
  methods: {
    updateEditTodo(event) {
      if (event.code === "Enter") {
        this.editTodo(event.currentTarget.value);
      }
    },
    ...mapActions(["setSelectedTodo", "editTodo", "removeTodo"]),
  },
  computed: {
    ...mapGetters(["getFilteredTodos"]),
    ...mapState(["selectedTodo"]),
  },
};
</script>

<style lang="scss">
.TodoList {
  list-style: none;
  max-height: 420px;
  overflow-y: scroll;
  overflow-x: hidden;
  padding: 0px 10px 10px 10px;
  &-TodoItem {
    display: inline-flex;
    width: 100%;
    min-width: 100%;
    border: none;
    border-radius: 5px;
    background-color: #748ffc;
    margin-bottom: 10px;
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
    text-align: center;
    align-items: center;
    padding: 0px 8px 0px 8px;
    min-height: 65px;
    &-Check {
      float: left;
      width: 24px;
      height: 24px;
      cursor: pointer;
      display: inline;
    }
    &-EditContainer {
      &-Content {
        display: inline-block;
        font-size: 1.25rem;
        font-weight: 700;
        color: white;
        min-width: 480px;
        max-width: 480px;
        word-break: break-all;
      }
      &-EditInput {
        width: 70%;
        height: 30px;
        outline: none;
        margin-top: 10px;
      }
    }
    &-DelBtn {
      float: right;
      transition: 0.3s;
      height: 30px;
      border: none;
      padding: 0px 5px 0px 5px;
      border-radius: 5px;
      background-color: #748ffc;
      border: 2px solid white;
      color: white;
      outline: none;
      cursor: pointer;
      margin-right: 5px;
    }
    &-DelBtn:hover{
      background-color: #4c6ef5;
    }
  }
}
</style>