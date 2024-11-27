<script setup>
defineProps({
  review:Object
})

</script>


<template>
  <div>
    <ul>
      <li>
        <p>Movie : {{ review.movie }}</p>
        <p>Contents : {{ review.content }}</p>
        <p>Ratings : {{ review.rating }}</p>
      </li>
    </ul>
    <hr>
  </div>
</template>


<style scoped>

</style>
