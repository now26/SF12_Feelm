import { createRouter, createWebHistory } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

import MovieTmdbView from '@/views/Movie_tmdb/MovieTmdbView.vue'
import MoviePopularDetailView from '@/views/Movie_tmdb/MoviePopularDetailView.vue'
import MovieNowPlayingDetailView from '@/views/Movie_tmdb/MovieNowPlayingDetailView.vue'
import MovieTopRatedDetailView from '@/views/Movie_tmdb/MovieTopRatedDetailView.vue'
import MovieUpComingDetailView from '@/views/Movie_tmdb/MovieUpComingDetailView.vue'

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
    {
      path: '/movies/tmdb/now-playing',
      name: 'MovieNowPlayingDetailView',
      component: MovieNowPlayingDetailView
    },
    {
      path: '/movies/tmdb/upcoming-list',
      name: 'MovieUpComingDetailView',
      component: MovieUpComingDetailView
    },
    {
      path: '/movies/tmdb/top-rated-list',
      name: 'MovieTopRatedDetailView',
      component: MovieTopRatedDetailView
    },
  ],
})

// movieRouter.beforeEach((to, from) => {
//   const useStore = useCounterStore()

// })

export default movieRouter
