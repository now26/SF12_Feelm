import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyPageView from '@/views/User/MyPageView.vue'
import UserInfoView from '@/views/User/UserInfoView.vue'
import UserInfo from '@/components/User/UserInfo.vue'

import ReviewView from '@/views/User/ReviewView.vue'
import ReviewDetailView from '@/views/User/ReviewDetailView.vue'
import ReviewList from '@/components/User/ReviewList.vue'
import ReviewCreateView from '@/views/Review/ReviewCreateView.vue'


import TabsView from '@/views/TabsView.vue'


const userRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView,
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
    {
      path: '/review/create',
      name: 'ReviewCreateView',
      component: ReviewCreateView
    }

  ],
})

userRouter.beforeEach((to, from, next) => {
  if (from.name === 'MyPageView') {
    // currentTab 값을 null로 설정 (이 방식은 기본적으로 삭제된 것처럼 동작)
    localStorage.setItem('currentTab', null);
    console.log('currentTab 값을 null로 설정');
  }
  next();
});

export default userRouter
