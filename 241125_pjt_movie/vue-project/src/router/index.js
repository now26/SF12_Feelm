import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import MyPageView from '@/views/User/MyPageView.vue'

import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'


// cart.js 라우터를 불러오기.
import cartRouter from '@/router/cart'

// movie.js 라우터를 불러오기.
import movieRouter from '@/router/movie'

// user.js 라우터를 불러오기.
import userRouter from '@/router/user'

// content.js 라우터를 불러오기.
import contentRouter from '@/router/content'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/articles/create',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },

    // cart.js 라우터를 추가
    ...cartRouter.options.routes, 
    
    // movie.js 라우터를 추가
    ...movieRouter.options.routes,

    // user.js 라우터를 추가
    ...userRouter.options.routes,

    // content.js 라우터를 추가
    ...contentRouter.options.routes,
  ],
})

router.beforeEach((to, from) => {
  const useStore = useCounterStore()

  if (window.isLoggingOut){
    window.isLoggingOut = false
    return true
  }

  if (to.name === 'ArticleView' && !useStore.isLogin){
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }

  if ((to.name === 'SignUpView' || to.name ==='LogInView') && (useStore.isLogin)){
    window.alert('이미 로그인 되어있습니다.')
    // return { name: 'HomeView' }
    return { name: from.name } // 현재 페이지 잔류
  }

  return true
})

export default router
