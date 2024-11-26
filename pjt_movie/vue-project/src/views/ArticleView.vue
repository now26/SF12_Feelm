<script setup>
import { useCounterStore } from '@/stores/counter.js'
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import ArticleList from '@/components/ArticleList.vue';

const useStore = useCounterStore()


onMounted(()=>{
  useStore.getArticles()
  // console.log(useStore.tests)
})
</script>


<template>
  <header>
    <h1>Articles</h1>
  </header>
  
  <div id="page">

    <div>
      <nav>
        <RouterLink :to="{name: 'ArticleCreateView'}" class="createBtn">Create</RouterLink>
      </nav>
    </div>
    
    <div class="note">
      <div class="background">
        <div id="pageD">
          <ArticleList/>
        </div>
      </div>
    </div>
    
  </div>
</template>


<style scoped>
header {
  display: flex;
  justify-content: center;
}

h1 {
  font-weight: bold;
  font-size: 2.5rem;
  padding-bottom: 20px;
}

.createBtn{
  font-size: 1.5rem;
  color: aliceblue;
  text-decoration-line: none;
  display: flex;
  justify-content: flex-end;
  padding-bottom: 20px;
  padding-right: 15%;
}

.note {
  display: flex;
  justify-content: center;
}

.background {
  background-color: rgb(215, 240, 250);
  min-height: 100dvh;
  padding-top: 40px;
  width: 80%;
  justify-content: center;
}

#pageD {
  display: grid;
  grid-template-columns: 70%;
  justify-content: center;
}


</style>
