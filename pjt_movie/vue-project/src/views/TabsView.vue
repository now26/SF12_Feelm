<!-- div 식 -->

<template>
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
</template>

<script>
import { ref, computed } from 'vue';  // Vue 3에서 Composition API를 사용하려면 ref와 computed를 import

// 각 탭에 해당하는 컴포넌트를 import 해야 합니다.
import Tab1Component from '@/components/User/UserInfo.vue';
import Tab2Component from '@/components/User/UserInfo.vue';
import Tab3Component from '@/components/User/UserInfo.vue';

export default {
  setup() {
    // `tabs`는 탭 목록을 배열로 정의
    const tabs = ['Tab1', 'Tab2', 'Tab3'];

    // 현재 선택된 탭을 `ref`로 정의 (초기값은 'Tab1')
    const currentTab = ref('Tab1');

    // 탭을 클릭할 때 선택된 탭을 설정하는 함수
    const setCurrentTab = (tab) => {
      currentTab.value = tab;
    };

    // 현재 탭에 맞는 컴포넌트를 반환하는 계산된 속성 (computed)
    const currentTabComponent = computed(() => {
      if (currentTab.value === 'Tab1') return Tab1Component;
      if (currentTab.value === 'Tab2') return Tab2Component;
      if (currentTab.value === 'Tab3') return Tab3Component;
    });

    // setup 함수 내에서 반환된 변수와 함수를 template에서 사용할 수 있게 반환
    return {
      tabs,
      currentTab,
      setCurrentTab,
      currentTabComponent,
    };
  },
};
</script>

<style scoped>
.tabs {
  display: flex;
  gap: 10px;
  cursor: pointer;
}

.tab {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.tab.active {
  background-color: #4CAF50;
  color: white;
}
</style>





<!-- ======================================= -->
<!-- button 식 -->
<!-- <template>
    <div class="page-container"> -->
      <!-- 탭 -->
      <!-- <div class="tabs">
        <button 
          v-for="(tab, index) in tabs" 
          :key="index" 
          @click="currentTab = tab"
          :class="{ active: currentTab === tab }"
        >
          {{ tab }}
        </button>
      </div> -->
  
      <!-- 탭에 따른 내용 표시 -->
      <!-- <div class="tab-content"> -->
        <!-- <component :is="currentTabComponent" />
      </div>
    </div>
  </template> -->
  
  <!-- <script>
  import UserInfo from '@/components/User/UserInfo.vue';
  import ReviewList from '@/components/User/ReviewList.vue'; -->

  <!-- // import Tab1 from './Tab1.vue'
  // import Tab2 from './Tab2.vue'
  // import Tab3 from './Tab3.vue'
  
  export default {
    data() {
      return {
        tabs: ['UserInfo', 'ReviewList', 'ReviewList'],  // 탭 이름
        currentTab: 'UserInfo',  // 기본적으로 선택된 탭
      }
    },
    computed: {
      currentTabComponent() {
        // 현재 탭에 맞는 컴포넌트를 반환
        if (this.currentTab === 'UserInfo') {
          return UserInfo
        } else if (this.currentTab === 'ReviewList') {
          return ReviewList
        } else if (this.currentTab === 'ReviewList') {
          return ReviewList
        }
      }
    },
    components: {
      UserInfo,
      ReviewList,
      ReviewList
    }
  }
  </script>
  
  <style scoped>
  .tabs {
    display: flex;
    gap: 10px;
  }
  button.active {
    background-color: #4CAF50;
    color: white;
  }
  </style> -->
  