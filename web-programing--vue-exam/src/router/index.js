import Vue from 'vue'
import VueRouter from 'vue-router'
import Intro from '../views/Intro.vue'
import Todo from '../views/Todo.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Todo',
    component: Todo
  },
  {
    path: '/intro',
    name: 'Intro',
    component: Intro
  }
]

const router = new VueRouter({
  routes
})

export default router
