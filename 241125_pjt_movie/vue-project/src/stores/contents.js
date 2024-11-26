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


  return {

  }

}, { persist: true })