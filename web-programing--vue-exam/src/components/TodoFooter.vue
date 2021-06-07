<template>
  <div>
    <select name="all" @change="onChange(onChange($event))">
      <option value="all">All</option>
      <option value="active">Active</option>
      <option value="done">Done</option>
    </select>
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
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TodoFooter",
  methods: {
    ...mapActions(["updateVisibility", "removeCompletedTodo"]),
    onChange(e) {
      this.updateVisibility(e.target.value);
    },
  },
  computed: {
    ...mapGetters(["completedCount"]),
  },
};
</script>

<style></style>