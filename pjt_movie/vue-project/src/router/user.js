import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyPageView from '@/views/User/MyPageView.vue'
import UserInfoView from '@/views/User/UserInfoView.vue'
import UserInfo from '@/components/User/UserInfo.vue'

import ReviewView from '@/views/User/ReviewView.vue'
import ReviewDetailView from '@/views/User/ReviewDetailView.vue'
import ReviewList from '@/components/User/ReviewList.vue'


const userRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/mypage/myinfo',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/review',
      name: 'ReviewList',
      component: ReviewList
    },
    // {
    //   path: '/review',
    //   name: 'ReviewView',
    //   component: ReviewView
    // },
    {
      path: '/review/:id',
      name: 'ReviewDetailView',
      component: ReviewDetailView
    },

  ],
})

// userRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default userRouter
