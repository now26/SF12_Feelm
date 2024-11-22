import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyPageView from '@/views/User/MyPageView.vue'

import ReviewDetailView from '@/views/User/ReviewDetailView.vue'

const userRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/review-list',
      name: 'ReviewDetailView',
      component: ReviewDetailView
    },

  ],
})

// userRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default userRouter
