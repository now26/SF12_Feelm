<script setup>
import { onMounted, ref } from 'vue'

import { useContentStore } from '@/stores/contents';
const contentStore = useContentStore()
contentStore.getDiaryList()

const diaryList = ref([])

onMounted(() => {
  if(contentStore.getDiaryList()) {
    diaryList.value = contentStore.diary_db
  }
})

console.log(diaryList.value)


</script>


<template>
  <div>
    <h1>Diary View</h1>
    {{  }}
  </div>
</template>


<style scoped>

</style>
