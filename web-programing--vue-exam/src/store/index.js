import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    todos: [],
    visibility: "all",
    selectedTodo: null,
  },
  mutations: {
    ADD_TODO(state, todo) {
      state.todos.push(todo);
    },
    REMOVE_TODO(state, id) {
      state.todos = state.todos.filter((todo) => todo.id !== id);
    },
    EDIT_TODO(state, text) {
      state.selectedTodo.text = text;
      const findIndex = state.todos.findIndex(
        (todo) => todo.id === state.selectedTodo.id
      );
      state.todos.splice(findIndex, 1, state.selectedTodo);
      state.selectedTodo = null;
    },
    REMOVE_COMPLETED_TODO(state) {
      state.todos = state.todos.filter((todo) => !todo.completed);
    },
    UPDATE_VISIBILITY(state, visibility) {
      state.visibility = visibility;
    },
    SET_EDIT_TODO(state, todo) {
      state.selectedTodo = todo;
    },
  },
  actions: {
    createTodo({ commit }, text) {
      commit("ADD_TODO", {
        id: `todo-${Date.now()}`,
        text,
        completed: false,
      });
    },
    removeTodo({ commit }, id) {
      commit("REMOVE_TODO", id);
    },
    editTodo({ commit }, text) {
      commit("EDIT_TODO", text);
    },
    removeCompletedTodo({ commit }) {
      commit("REMOVE_COMPLETED_TODO");
    },
    updateVisibility({ commit }, visibility) {
      commit("UPDATE_VISIBILITY", visibility);
    },
    setSelectedTodo({ commit }, todo) {
      commit("SET_EDIT_TODO", todo);
    },
  },
  getters: {
    getFilteredTodos(state) {
      const { visibility } = state;
      if (visibility === "active") {
        return state.todos.filter((todo) => !todo.completed);
      } else if (visibility === "done") {
        return state.todos.filter((todo) => todo.completed);
      } else {
        return state.todos;
      }
    },
    completedCount(state) {
      return state.todos.filter((todo) => todo.completed).length;
    },
  },
});
