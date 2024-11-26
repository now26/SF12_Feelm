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
  const api_key = '87246d75e1ce26e1392a087b3d1d88c5'
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


  return {
    bookmarkList,
    addToBookmark,
    isBookmarked
  }

}, { persist: true })