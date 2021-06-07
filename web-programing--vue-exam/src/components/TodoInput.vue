<template>
  <div>
    <input type="text" v-model="input" @keyup="inputTodo" />
    <button type="button" @click="addTodo">ADD</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'TodoInput',
  data() {
    return { input: '' }
  },
  methods: {
    inputTodo(event) {
      if (event.key === 'Enter') {
        this.addTodo()
      }
    },
    addTodo() {
      if (this.input.trim() === '') return
      this.createTodo(this.input)
      this.input = ''
    },
    ...mapActions(['createTodo'])
  }
}
</script>

<style></style>