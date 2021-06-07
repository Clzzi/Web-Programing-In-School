<template>
  <div>
    <ul>
      <li v-for="todo in getFilteredTodos" :key="todo.id">
        <input type="checkbox" v-model="todo.completed" />
        <span @dblclick="setSelectedTodo(todo)">{{ todo.text }}</span>
        <button type="button" @click="removeTodo(todo.id)">delete</button>
        <input
          type="text"
          @keyup="updateEditTodo"
          v-show="selectedTodo && todo.id === selectedTodo.id"
        />
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapState } from 'vuex'
export default {
  name: 'TodoList',
  methods: {
    updateEditTodo(event) {
      if (event.code === 'Enter') {
        this.editTodo(event.currentTarget.value)
      }
    },
    ...mapActions(['setSelectedTodo', 'editTodo', 'removeTodo'])
  },
  computed: {
    ...mapGetters(['getFilteredTodos']),
    ...mapState(['selectedTodo'])
  }
}
</script>

<style></style>