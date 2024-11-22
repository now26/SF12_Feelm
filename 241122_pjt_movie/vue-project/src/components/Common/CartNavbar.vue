<script setup>
import { RouterLink } from 'vue-router';
</script>


<template>
  <nav class="navCart">
    <RouterLink :to="{ name: 'CartHomeView' }">CartHome</RouterLink> | 
    <RouterLink :to="{ name: 'CartView'}">Cart</RouterLink>
  </nav>

</template>


<style scoped>

</style>
