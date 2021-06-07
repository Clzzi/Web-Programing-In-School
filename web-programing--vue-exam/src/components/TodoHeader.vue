<template>
  <div class="TodoHeader">
    <select
      name="all"
      @change="onChange(onChange($event))"
      class="TodoHeader-SelectBox"
    >
      <option value="all">All</option>
      <option value="active">Active</option>
      <option value="done">Done</option>
    </select>
    <button type="button" @click="clearAll" class="TodoHeader-ClearAll">
      Clear All
    </button>
    <button
      type="button"
      @click="removeCompletedTodo"
      v-show="completedCount"
      class="TodoHeader-ClearDone"
    >
      Clear Done
    </button>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "TodoFooter",
  methods: {
    ...mapActions(["updateVisibility", "removeCompletedTodo", "clearAll"]),
    onChange(e) {
      this.updateVisibility(e.target.value);
    },
  },
  computed: {
    ...mapGetters(["completedCount"]),
  },
};
</script>

<style lang="scss">
.TodoHeader {
  padding: 0px 6px 0px 6px;
  display: inline-block;
  width: 100%;
  height: 30px;
  text-align: start;
  vertical-align: middle;
  margin-bottom: 15px;
  &-SelectBox {
    float: left;
    width: 100px;
    text-align-last: center;
    text-align: center;
    -ms-text-align-last: center;
    -moz-text-align-last: center;
    outline: none;
  }
  &-ClearDone {
    transition: 0.3s;
    float: right;
    height: 100%;
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
  &-ClearDone:hover {
    background-color: #4c6ef5;
  }
  &-ClearAll {
    transition: 0.3s;
    float: right;
    height: 100%;
    border: none;
    padding: 0px 5px 0px 5px;
    border-radius: 5px;
    background-color: #748ffc;
    border: 2px solid white;
    color: white;
    outline: none;
    cursor: pointer;
  }
  &-ClearAll:hover {
    background-color: #4c6ef5;
  }
}
</style>