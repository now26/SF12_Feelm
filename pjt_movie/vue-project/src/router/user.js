import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyPageView from '@/views/User/MyPageView.vue'
import UserInfoView from '@/views/User/UserInfoView.vue'
import UserInfo from '@/components/User/UserInfo.vue'

import ReviewView from '@/views/User/ReviewView.vue'
import ReviewDetailView from '@/views/User/ReviewDetailView.vue'
import ReviewList from '@/components/User/ReviewList.vue'
import ReviewCreateView from '@/views/User/ReviewCreateView.vue'

import DiaryCreateView from '@/views/User/DiaryCreateView.vue'
import DiaryDetailView from '@/views/User/DiaryDetailView.vue'

import BookmarkView from '@/views/User/BookmarkView.vue'

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
    },
    {
      path: '/mypage/diary',
      name: 'DiaryCreateView',
      component: DiaryCreateView
    },
    {
      path: '/mypage/diary',
      name: 'DiaryDetailView',
      component: DiaryDetailView
    },
    {
      path: '/movies/bookmark',
      name: 'BookmarkView',
      component: BookmarkView
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
