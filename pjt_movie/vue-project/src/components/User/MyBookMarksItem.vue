<script setup>
import { defineEmits } from 'vue';
import { ref, watch } from 'vue'
import { useContentStore } from '@/stores/contents';

const BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/'
const getPosterUrl = (posterPath, imageSize) => {
  if (posterPath) {
    return `${BASE_IMAGE_URL}${imageSize}${posterPath}`
  }
}

const getBackDrop = (backDropPath, imageSize) => {
  if (backDropPath) {
    return `${BASE_IMAGE_URL}${imageSize}${backDropPath}`
  }
}

// import { useUserStore } from '@/stores/users';
// import { onMounted } from 'vue'
// import { RouterLink, RouterView } from 'vue-router';

// const userStore = useUserStore()
// const userDB = userStore.userInfo

const contentStore = useContentStore()
const emit = defineEmits()
const props = defineProps({
  bookmark_item : Object
})

// 북마크 추가/취소 버튼 클릭
const toggleBookmark = async (movie) => {
  await contentStore.addToBookmark(movie);
  emit('bookmark-changed');  // 부모에게 북마크 변경 알리기
};

const formatDate = (dateString) => {
  const date = new Date(dateString)
  return format(date, 'yyyy년 MM월 dd일', { locale: ko }) // 한국 날짜 형식으로 변환
}

</script>


<template>
  <div>
    <div v-if="bookmark_item">
      <!-- <p>bookmark : {{ userDB.bookmark }}</p> -->
        <!-- <pre>
          {{ bookmark_item }}
        </pre> -->
        <div class="movie-poster">
          <RouterLink :to="{ name: 'MovieDetailView', params:{ id: bookmark_item.tmdb_id }}">
            <img :src="getPosterUrl(bookmark_item.poster_url, 'w300')" alt="Movie Poster" class="movie-poster">
          </RouterLink>
        </div>

        <!-- {{ bookmark_item }} -->
        <div>
          <h2>{{ bookmark_item.title }}</h2>
          <br></br>
          <p>tagline : {{ bookmark_item.tagline }}</p>
          <p>overview : {{ bookmark_item.overview }}</p>
          <p>genre : {{ bookmark_item.genre }}</p>  
          <p>runtime : {{ bookmark_item.runtime }}</p>
          <p>status : {{ bookmark_item.status }}</p>
          <p>vote_avg : {{ bookmark_item.vote_avg }}</p>
          <p>vote_count : {{ bookmark_item.vote_count }}</p>
        </div>
      <div>
        <button @click="toggleBookmark(bookmark_item)">
          {{ contentStore.isBookmarked(bookmark_item.tmdb_id) ? '북마크 취소' : '북마크 추가' }}
        </button>
      </div>
    
    </div>
    <hr>
  </div>
</template>


<style scoped>
.movie-poster {
  flex-shrink: 1; 
  width: 200px;
  height: 300px;
  border-radius: 10px;
}
</style>
