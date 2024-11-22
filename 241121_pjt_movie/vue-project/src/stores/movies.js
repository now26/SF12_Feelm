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

  // TMDB - movie_popular
  const movie_popular = ref([]) // 인기 영화 목록
  const po_currentPage = ref(1) // 현재 페이지 번호
  const po_totalPages = ref(0) // 전체 페이지 수

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
          // language: 'en-US',
          language: 'ko-KR',
          page: pageNum,
          sort_by: 'popularity.desc',
        }
      });
  
      // 응답 받은 데이터를 상태에 반영
      movie_popular.value = response.data.results;
      po_currentPage.value = pageNum;
      po_totalPages.value = response.data.total_pages;
    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };


  // TMDB - movie_now_playing
  const movie_nowPlaying = ref([]) // 현재 상영 영화 목록
  const np_currentPage = ref(1) // 현재 페이지 번호
  const np_totalPages = ref(0) // 전체 페이지 수

  const getMovieNowPlaying = async function(pageNum = 1, startDate = null, endDate = null) {
    try {

      // 오늘 날짜를 기준으로 한 달 전 날짜 계산
      const today = new Date()
      const lastMonth = new Date(today)
      lastMonth.setMonth(today.getMonth() - 1)

      // startDate와 endDate가 전달되지 않으면 기본값으로 설정
      const formattedStartDate = startDate || formatDate(lastMonth) // 한 달 전
      const formattedEndDate = endDate || formatDate(today) // 오늘

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
          // language: 'en-US',
          language: 'ko-KR',
          page: pageNum,
          sort_by: 'popularity.desc',
          with_release_type: '2|3',
          // 'release_date.gte': {min_date},
          // 'release_date.lte': {max_date},
          'release_date.gte': formattedStartDate,
          'release_date.lte': formattedEndDate,
        }
      });
  
      // 응답 받은 데이터를 상태에 반영
      movie_nowPlaying.value = response.data.results;
      np_currentPage.value = pageNum;
      np_totalPages.value = response.data.total_pages;
      // return response.data;

    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };


  // TMDB - movie_upComing
  const movie_upComing = ref([]) // 상영 예정 영화 목록
  const up_currentPage = ref(1) // 현재 페이지 번호
  const up_totalPages = ref(0) // 전체 페이지 수

  const getMovieUpComing = async function(pageNum = 1, startDate = null, endDate = null) {
    try {

      // 오늘 날짜를 기준으로 한 달 전 날짜 계산
      const today = new Date()
      const nearFuture = new Date(today)
      const future = new Date(today)
      nearFuture.setDate(today.getDate() + 7)
      future.setMonth(today.getMonth() + 1)

      // startDate와 endDate가 전달되지 않으면 기본값으로 설정
      const formattedStartDate = startDate || formatDate(nearFuture) // 7일 후
      const formattedEndDate = endDate || formatDate(future) // 한달 후

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
          // language: 'en-US',
          language: 'ko-KR',
          page: pageNum,
          sort_by: 'popularity.desc',
          with_release_type: '2|3',
          'release_date.gte': formattedStartDate,
          'release_date.lte': formattedEndDate,
        }
      });
  
      // 응답 받은 데이터를 상태에 반영
      movie_upComing.value = response.data.results;
      up_currentPage.value = pageNum;
      up_totalPages.value = response.data.total_pages;
      // return response.data;

    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };


  // TMDB - movie_topRated
  const movie_topRated = ref([]) // 별점 높은 영화 목록
  const tr_currentPage = ref(1) // 현재 페이지 번호
  const tr_totalPages = ref(0) // 전체 페이지 수

  const getMovieTopRated = async function(pageNum = 1) {
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
          // language: 'en-US',
          language: 'ko-KR',
          page: pageNum,
          sort_by: 'vote_average.desc',
          without_genres: [99, 10755],
          with_release_type: '2|3',
          'vote_count.gte': 200,
        }
      });
  
      // 응답 받은 데이터를 상태에 반영
      movie_topRated.value = response.data.results;
      tr_currentPage.value = pageNum;
      tr_totalPages.value = response.data.total_pages;
      // return response.data;

    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };
  
  // 날짜를 'YYYY-MM-DD' 형식으로 변환하는 함수
  const formatDate = (date) => {
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
  };


  return {
    DB_BASE_URL,
    movies_db,

    movie_popular,
    po_currentPage,
    po_totalPages,

    movie_nowPlaying,
    np_currentPage,
    np_totalPages,

    movie_upComing,
    up_currentPage,
    up_totalPages,

    movie_topRated,
    tr_currentPage,
    tr_totalPages,

    getMovies,
    getMoviePopular,
    getMovieNowPlaying,
    getMovieUpComing,
    getMovieTopRated
  }

}, { persist: true })