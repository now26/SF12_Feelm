<script setup>
import { useCounterStore } from '@/stores/counter';
const useStore = useCounterStore()

import axios from 'axios';
import { onMounted, ref } from 'vue'

import { useRoute } from 'vue-router';
const route = useRoute()

// const articledetail = ref([])
const articledetail = ref(null)

// Article Detail View가 마운트되기 전에 DRF로 단일 게시글 조회를 요청 후 응답데이터를 저장
onMounted(() => {
  // 토큰 전달 test
  // console.log("토큰: ", useStore.token)

  // const token = localStorage.getItem('access_token');
  // console.log("로컬 스토리지에서 읽은 토큰:", token);

  axios({
    method: 'get',
    url: `${useStore.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
        // 토큰 전달
        // Authorization: `Token ${token.value}` 
        // Authorization: `Bearer ${useStore.token.value}` 
        Authorization: `Bearer ${useStore.token}` 
    }
  })
  .then((res) => {
    articledetail.value = res.data
    // console.log(res.data)
  })
  .catch((err) => {console.log(err)})
})


</script>


<template>
  <div>
    <h1>Detail</h1>
    <div v-if="articledetail !== null">
      <p>게시글 번호 : {{ articledetail.id }}</p>
      <p>제목 : {{ articledetail.title }}</p>
      <p>내용 : {{ articledetail.content }}</p>
      <p>작성일 : {{ articledetail.created_at }}</p>
      <p>수정일 : {{ articledetail.updated_at }}</p>
    </div>

  </div>
</template>


<style scoped>

</style>
