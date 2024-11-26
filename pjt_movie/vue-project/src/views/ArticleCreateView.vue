<script setup>
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import { ref } from 'vue'
import axios from 'axios'

import { useRouter } from 'vue-router';
const router = useRouter()


const title = ref([])
const content = ref([])

// DRF로 게시글 생성 요청을 보내는 함수
const createArticle = () => {
  axios({
    method: 'post',
    url: `${useStore.API_URL}/api/v1/articles/`,
    // axios로 post 전달할 때, data 속성에 담아서 전달
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      // 토큰 전달, 중앙저장소가 아니기 때문에 useStore를 써야 한다.
      Authorization: `Bearer ${useStore.token}` 
    }
  })
  .then((res) => {
    console.log(res)
    router.push({name: 'ArticleView'})
  })
  .catch((err) => console.log(err))
}

</script>


<template>
  <div>
    <h1>Create</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">Title : </label>
        <input type="text" id="title" v-model.trim="title">
      </div>
      
      <div>
        <label for="content">Content : </label>
        <textarea id="content" v-model.trim="content"></textarea>
      </div>
      
      <div>
        <button type="submit">submit</button>
      </div>
    </form>
  </div>
</template>


<style scoped>

</style>
