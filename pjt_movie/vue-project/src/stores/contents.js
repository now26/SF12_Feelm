import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'
import { useRouter } from 'vue-router'

import { useCounterStore } from '@/stores/counter'


export const useContentStore = defineStore('contents', () => {
  const useStore = useCounterStore()
  const router = useRouter()

  const DB_BASE_URL = 'http://127.0.0.1:8000'
  const token = useStore.token

  const TMDB_BASE_URL = 'https://api.themoviedb.org/'
  const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY
  const TMDB_TOKEN = import.meta.env.VITE_TMDB_TOKEN
  // console.log(import.meta.env.VITE_TMDB_TOKEN)

  let bookmarkList = ref([])

  const addToBookmark = async (movie) => {
    const movie_id = movie.tmdb_id

    try {
      const response = await axios({
        method: 'post',
        url: `${DB_BASE_URL}/api/v1/movies/${movie_id}/bookmark/`,
        data: {
          tmdb_id: movie_id,
        },
        headers: {
          Authorization: `Bearer ${useStore.token}`
        }
      })
      // console.log(response.data)
      if (response.data.message === '북마크 성공'){
        bookmarkList.value.push(movie)

      } else if (response.data.message === '북마크 취소 성공'){
        bookmarkList.value = bookmarkList.value.filter(item => item.tmdb_id !== movie_id);
      }

      // Log the updated state for debugging
      console.log('Updated bookmark list:', bookmarkList.value);
      console.log('Updated isBookmarked:', isBookmarked.value);

      // isBookmark.value = 1
      // bookmarkLists.value.push(re)
    } catch (err) {
      console.error('Error:', err)
    }
  }

  // 영화가 북마크에 있는지 확인
  const isBookmarked = (movie_id) => {
    return bookmarkList.value.some(movie => movie.tmdb_id === movie_id)
  }


  const diary_db = ref([])
  const getDiaryList = function() {

    axios({
      method: 'get',
      url: `${DB_BASE_URL}/accounts/mypage/diary/`,
      headers: {
        Authorization: `Bearer ${useStore.token}`
      }
    })
    .then((res) => {
      // console.log(res)
      diary_db.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const rcContentBasedMovies = ref([]) // 인기 영화 목록
  const rcCt_urrentPage = ref(1) // 현재 페이지 번호
  const rcCt_totalPages = ref(0) // 전체 페이지 수

  const getContentBased = async function(tmdb_id) {
    try {
      // 비동기 요청을 기다림
      const response = await axios({
        method: 'get',
        url: `${DB_BASE_URL}/api/v1/movies/${tmdb_id}/`,
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${token}`,
        },
      });
  
      // 응답 받은 데이터를 상태에 반영
      console.log(response.data)
      rcContentBasedMovies.value = response.data.results;
      // rcCt_urrentPage.value = pageNum;
      // rcCt_totalPages.value = response.data.total_pages;
    } catch (err) {
      console.error('Error fetching popular movies:', err);
    }
  };


  const rcUser_BM_BasedMovies = ref([]) // 인기 영화 목록
  const rcUser_RT_BasedMovies = ref([]) // 인기 영화 목록
  const rcUs_urrentPage = ref(1) // 현재 페이지 번호
  const rcUs_totalPages = ref(0) // 전체 페이지 수

  const getUserBased = async function() {
    try {
      // 비동기 요청을 기다림
      const response = await axios({
        method: 'get',
        url: `${DB_BASE_URL}/accounts/mypage/recom/`,
        headers: {
          accept: 'application/json',
          Authorization: `Bearer ${token}`,
        },
      });
  
    // 응답 데이터 로그 확인
    console.log('API 응답:', response.data);

    // bookmark_reccomendations 데이터를 처리
    if (response.data && Array.isArray(response.data.bookmark_reccomendations)) {
      rcUser_BM_BasedMovies.value = response.data.bookmark_reccomendations;
      console.log('북마크 추천:', rcUser_BM_BasedMovies.value);
    } else {
      console.error('bookmark_reccomendations 데이터가 없습니다.');
      rcUser_BM_BasedMovies.value = [];  // 빈 배열로 처리
    }

    // review_recommendations 데이터를 처리
    if (response.data && Array.isArray(response.data.review_recommendations)) {
      rcUser_RT_BasedMovies.value = response.data.review_recommendations;
      console.log('리뷰 추천:', rcUser_RT_BasedMovies.value);
    } else {
      console.error('review_recommendations 데이터가 없습니다.');
      rcUser_RT_BasedMovies.value = [];  // 빈 배열로 처리
    }

  } catch (err) {
    console.error('Error fetching user-based recommendations:', err);
  }
};






  return {
    bookmarkList,

    diary_db,

    rcContentBasedMovies,
    rcCt_urrentPage,
    rcCt_totalPages,

    rcUser_BM_BasedMovies,
    rcUser_RT_BasedMovies,
    rcUs_urrentPage,
    rcUs_totalPages,

    addToBookmark,
    isBookmarked,

    getDiaryList,

    getContentBased,
    getUserBased
  }

}, { persist: true })