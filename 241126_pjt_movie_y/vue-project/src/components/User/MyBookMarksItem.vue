<script setup>
import { defineEmits } from 'vue';
import { ref, watch } from 'vue'
import { useContentStore } from '@/stores/contents';

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
</script>


<template>
  <div>
    <div v-if="bookmark_item">
      <!-- <p>bookmark : {{ userDB.bookmark }}</p> -->
      <p>
        <!-- <pre>
          {{ bookmark_item }}
        </pre> -->
        {{ bookmark_item }}
        {{ bookmark_item.title }}
      </p>

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

</style>
