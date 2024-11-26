<script setup>
import { ref, watch } from 'vue'
import { useContentStore } from '@/stores/contents';
import MyBookMarksItem from '@/components/User/MyBookMarksItem.vue';

// import { onMounted } from 'vue'
// import { useUserStore } from '@/stores/users';
// import { RouterLink, RouterView } from 'vue-router';


const contentStore = useContentStore()
const bookmarkList = ref(contentStore.bookmarkList)
// const bookmarkList_local = ref([...contentStore.bookmarkList])

// const isbookmarks = ref([])
// console.log(bookmarkList)

// bookmarkList가 변경될 때마다 UI를 업데이트하도록 watch 설정
watch(() => contentStore.bookmarkList, (newList) => {
  bookmarkList.value = newList;
});

// 자식 컴포넌트에서 북마크 변경 이벤트 처리
const handleBookmarkChanged = () => {
  // 북마크 변경 시 목록 갱신
  bookmarkList.value = [...contentStore.bookmarkList]
}

// onMounted(() => {
//   const bookmarkList = ref([contentStore.bookmarkList])
// })

</script>


<template>
  <!-- <div id="page"> -->
  <div>
    <div>
      <div v-if="bookmarkList.length > 0">
        <MyBookMarksItem
          v-for="bookmark in bookmarkList"
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
