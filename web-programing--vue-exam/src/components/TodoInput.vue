<template>
  <div class="TodoInputWrapper">
    <input
      class="TodoInputWrapper-TodoInput"
      type="text"
      v-model="input"
      @keyup="inputTodo"
      autofocus
    />
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "TodoInput",
  data() {
    return { input: "" };
  },
  methods: {
    inputTodo(event) {
      if (event.key === "Enter") {
        this.addTodo();
      }
    },
    addTodo() {
      if (this.input.trim() === "") return;
      this.createTodo(this.input);
      this.input = "";
    },
    ...mapActions(["createTodo"]),
  },
};
</script>

<style lang="scss">
.TodoInputWrapper {
  width: 600px;
  height: 60px;
  padding: 0px 6px 0px 6px;
  margin-bottom: 10px;
  &-TodoInput {
    width: 100%;
    height: 100%;
    outline: none;
    border-radius: 5px;
    border: none;
    padding: 0px 10px 0px 10px;
    font-size: 1.25rem;
  }
}
</style>