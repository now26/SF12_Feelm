import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MyContentView from '@/views/MyContent/MyContentView.vue'
import RecommendView from '@/components/Content/RecommendView.vue'
import RcContentDetailView from '@/views/MyContent/RcContentDetailView.vue'
import RcUserDetailView from '@/views/MyContent/RcUserDetailView.vue'

import RcDetail2 from '@/views/MyContent/RcDetail2.vue'

const contentRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/contents',
      name: 'MyContentView',
      component: MyContentView
    },
    {
      path: '/movie/recommend',
      name: 'RecommendView',
      component: RecommendView
    },
    {
      path: '/movie/recommend/bookmark-based',
      name: 'RcContentDetailView',
      component: RcContentDetailView
    },
    {
      path: '/movie/recommend/user-based',
      name: 'RcUserDetailView',
      component: RcUserDetailView
    },
    {
      path: '/movie/recommend/content-based2',
      name: 'RcDetail2',
      component: RcDetail2
    },
  ],
})

// contentRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default contentRouter
