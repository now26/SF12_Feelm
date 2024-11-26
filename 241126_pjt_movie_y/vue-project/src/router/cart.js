import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import CartHomeView from '@/views/Cart/CartHomeView.vue'
import CartView from '@/views/Cart/CartView.vue'
import CartDetailView from '@/views/Cart/CartDetailView.vue'

const cartRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/cart/home',
      name: 'CartHomeView',
      component: CartHomeView
    },
    {
      path: '/cart',
      name: 'CartView',
      component: CartView
    },
    {
      path: '/cart/:product_id',
      name: 'CartDetailView',
      component: CartDetailView
    },
  ],
})

// cartRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default cartRouter
