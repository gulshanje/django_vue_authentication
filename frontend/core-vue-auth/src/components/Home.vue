<template>
    <div>
        <h1>Hello Home Page</h1>
        <h3>{{ message }}</h3>
    </div>
</template>

<script>
import { onMounted, ref } from "vue";
import axios from 'axios';
    export default {
        name:'HomePage',
        setup(){
          const message = ref('You are not logged in') 
          onMounted(async () => {
            const {data} =  await axios.get('user')
            message.value = `Hi! ${data.first_name }, ${data.last_name}` 
          })
          
          return ({
            message
          })
        }
    }
</script>

<style scoped>

</style>