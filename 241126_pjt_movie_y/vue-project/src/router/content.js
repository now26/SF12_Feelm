import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyContentView from '@/views/MyContent/MyContentView.vue'

const contentRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/contents',
      name: 'MyContentView',
      component: MyContentView
    },
  ],
})

// contentRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default contentRouter
