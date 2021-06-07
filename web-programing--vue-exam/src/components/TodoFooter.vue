<template>
  <div>
    <button type="button" @click="updateVisibility('all')">All</button>
    <button type="button" @click="updateVisibility('active')">Active</button>
    <button type="button" @click="updateVisibility('completed')">
      Completed
    </button>
    <button
      type="button"
      @click="removeCompletedTodo"
      v-show="completedCount > 0"
    >
      Clear completed
    </button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'TodoFooter',
  methods: {
    ...mapActions(['updateVisibility', 'removeCompletedTodo'])
  },
  computed: {
    ...mapGetters(['completedCount'])
  }
}
</script>

<style></style>