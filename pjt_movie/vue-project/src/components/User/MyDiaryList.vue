<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue';
import { useContentStore } from '@/stores/contents'

import MyDiaryListItems from '@/components/User/MyDiaryListItems.vue';

const contentStore = useContentStore()
const diaryDB = contentStore.diary_db

const userDiary = ref([...diaryDB])

onMounted(() => {
    contentStore.getDiaryList()
    if(contentStore.diary_db){
        userDiary.value = contentStore.diary_db
    }
})

// 삭제된 다이어리를 처리하는 함수
const handleDeleteDiary = (diary_id) => {
  // 삭제된 diary_id를 제외한 새로운 배열로 갱신
  userDiary.value = userDiary.value.filter(diary => diary.id !== diary_id);
  contentStore.diary_db = userDiary.value
  // 서버에서 해당 다이어리 삭제 API 호출
  contentStore.deleteDiary(diary_id)
  .then(() => {
    contentStore.diary_db = userDiary.value
  })
  .catch((err) => {
      console.error("Error deleting diary:", err)
  })
}

</script>


<template>
    <!-- {{ userDiary }} -->
  <div v-if="userDiary && userDiary.length > 0">
    <MyDiaryListItems
      v-for="diary in userDiary"
      :key="diary.id"
      :diary="diary"
      @deleteDiary="handleDeleteDiary"
    />
  </div>
  <div v-else>
    <p>아직 작성된 일기가 없습니다.</p>
  </div>
</template>


<style scoped>

</style>
