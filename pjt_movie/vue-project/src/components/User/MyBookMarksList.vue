<script setup>
import { ref, watch } from 'vue'
import { onMounted } from 'vue'

import { useUserStore } from '@/stores/users';
import { useContentStore } from '@/stores/contents';
import { RouterLink, RouterView } from 'vue-router';

import MyBookMarksItem from '@/components/User/MyBookMarksItem.vue';

const contentStore = useContentStore()
// const bookmarkList_local = ref([...contentStore.bookmarkList])
const bookmarkList = ref(contentStore.bookmarkList)

// console.log(bookmarkList)

const isbookmarks = ref([])

// bookmarkList가 변경될 때마다 UI를 업데이트하도록 watch 설정
watch(() => contentStore.bookmarkList, (newList) => {
  bookmarkList.value = newList;
});

// 자식 컴포넌트에서 북마크 변경 이벤트 처리
const handleBookmarkChanged = () => {
  // 북마크 변경 시 목록 갱신
  bookmarkList.value = [...contentStore.bookmarkList];
};

// onMounted(() => {
//   const bookmarkList = ref([contentStore.bookmarkList])
// })

</script>


<template>
  <div>
    <div>
      <div v-if="bookmarkList.length > 0">
        <MyBookMarksItem
          v-for="bookmark in bookmarkList.length"
          :key="bookmark.tmdb_id"
          :bookmark_item="bookmark"
          @bookmark-changed="handleBookmarkChanged"
        />
      </div>
      <div v-else>
        북마크가 비어있습니다.
      </div>

    </div>
  </div>
</template>


<style scoped>

</style>
