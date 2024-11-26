<script setup>
import { useUserStore } from '@/stores/users';
import { useContentStore } from '@/stores/contents';
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';

import MyDiaryList from '@/components/User/MyDiaryList.vue';

const userStore = useUserStore()
const userDB = userStore.userInfo

const contentStore = useContentStore()
const diaryDB = contentStore.diary_db


</script>


<template>
  <div>
    <header>
      <h1>
        Diary
      </h1>
    </header>

    <MyDiaryList />
  </div>
</template>


<style scoped>

</style>
