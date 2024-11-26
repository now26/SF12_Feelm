<script setup>
import { ref, computed, onMounted } from 'vue';  // Vue 3에서 Composition API를 사용하려면 ref와 computed를 import

import MyBookMarks from '@/components/User/MyBookMarks.vue';
import MyContents from '@/components/User/MyContents.vue';

// `tabs`는 탭 목록을 배열로 정의
const tabs = ['BookMarks', 'MyContents']

// 로컬스토리지에서 저장된 탭 상태를 가져오기. 없으면 기본값 'MyInfo'
const savedTab = localStorage.getItem('currentTab')
// 현재 선택된 탭을 `ref`로 정의 (초기값은 'BookMarks')
const currentTab = ref(savedTab || 'BookMarks')

// 탭을 클릭할 때 선택된 탭을 설정하는 함수
const setCurrentTab = (tab) => {
    currentTab.value = tab
    // 탭 상태를 localStorage에 저장
    localStorage.setItem('currentTab', tab)
}

// 현재 탭에 맞는 컴포넌트를 반환하는 계산된 속성 (computed)

const currentTabComponent = computed(() => {
    if (currentTab.value === 'BookMarks') return MyBookMarks
    if (currentTab.value === 'MyContents') return MyContents
})


</script>



<template>
  <div class="page-container">
    <!-- 탭 -->
    <div class="tabs">
        <div
            v-for="(tab, index) in tabs"
            :key="index"
            class="tab"
            @click="setCurrentTab(tab)"
            :class="{ active: currentTab === tab }"
        >
            {{ tab }}
        </div>
    </div>

    <div class="tab-content">
        <component :is="currentTabComponent" />
    </div>

  </div>
</template>



<style scoped>
.tabs {
    display: flex;
    gap: 10px;
    cursor: pointer;
    margin-top: 20px;
    margin-bottom: 25px;
    justify-content: center;
}

.tab {
    padding: 5px 10px;
    margin-right: 20px;
    font-size: 1.1rem;
    border-radius: 12px;
}

.tab:hover {
    background-color: #333;
}

.tab.active {
  background-color: #FFF7D6;
  color: #1C2644;
}

</style>