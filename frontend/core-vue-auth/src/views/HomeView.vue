<template>
  <main>
    <h3>{{ auth ? message : 'You are not logged in' }}</h3>
  </main>
</template>

<script  lang="ts">
 import { onMounted, ref, computed } from "vue";
    import axios from 'axios';
    import { useStore } from "vuex";
    export default {
        name: "HomeView",
        setup(){
        const message = ref('You are not logged in') 
        const store = useStore()
        const auth = computed(() => store.state.auth)
        onMounted(async () => {
          try {
            const {data} =  await axios.get('user')
            console.log(data.first_name);
            message.value =  `Hi! ${data.first_name }, ${data.last_name}` 
            await store.dispatch('setAuth', true)
          } catch (e) {
            await store.dispatch('setAuth', false)
          }
          
        })
        
        return ({
          message,
          auth
        })
      }
    }
</script>

<style scoped>

</style>