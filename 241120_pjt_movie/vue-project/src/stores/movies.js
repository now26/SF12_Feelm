import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

import { useCounterStore } from './counter'


export const useMovieStore = defineStore('movies', () => {
  const useStore = useCounterStore()
  const router = useRouter()

  const DB_BASE_URL = 'http://127.0.0.1:8000'
  const token = useStore.token

  const TMDB_BASE_URL = 'https://api.themoviedb.org/'
  const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY
  const api_key = '87246d75e1ce26e1392a087b3d1d88c5'
  const TMDB_TOKEN = import.meta.env.VITE_TMDB_TOKEN
  // console.log(import.meta.env.VITE_TMDB_TOKEN)

  const movies_db = ref([])


  // TMDB - movie_popular
  const movie_popular = ref([]) // 인기 영화 목록
  const currentPage = ref(1) // 현재 페이지 번호
  const totalPages = ref(0) // 전체 페이지 수


  const getMovies = function() {
    // 토큰 전달 test
    // console.log("토큰: ", token)

    axios({
      method: 'get',
      url: `${DB_BASE_URL}/api/v1/movies/`,
      headers: {
        // 토큰 전달
        Authorization: `Bearer ${token}`
      }
    })
    .then((res) => {
      movies_db.value = res.data
      // console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const getMoviePopular = async function(pageNum = 1) {
    try {
      // 비동기 요청을 기다림
      const response = await axios({
        method: 'get',
        url: `${TMDB_BASE_URL}/3/discover/movie`,
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${TMDB_TOKEN}`,
        },
        params: {
          include_adult: false,
          include_video: false,
          language: 'en-US',
          page: pageNum,
          sort_by: 'popularity.desc',
        }
      });
  
      // 응답 받은 데이터를 상태에 반영
      movie_popular.value = response.data.results;
      currentPage.value = pageNum;
      totalPages.value = response.data.total_pages;
    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };
  


  return {
    DB_BASE_URL,
    movies_db,
    movie_popular,
    currentPage,
    totalPages,
    getMovies,
    getMoviePopular
  }

}, { persist: true })