import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

import MovieTmdbView from '@/views/Movie_tmdb/MovieTmdbView.vue'
import MoviePopularDetailView from '@/views/Movie_tmdb/MoviePopularDetailView.vue'

const movieRouter = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/movies',
      name: 'MovieView',
      component: MovieView
    },
    {
      path: '/movies/:id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/movies/tmdb',
      name: 'MovieTmdbView',
      component: MovieTmdbView
    },
    {
      path: '/movies/tmdb/popular',
      name: 'MoviePopularDetailView',
      component: MoviePopularDetailView
    },
  ],
})

// movieRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default movieRouter
