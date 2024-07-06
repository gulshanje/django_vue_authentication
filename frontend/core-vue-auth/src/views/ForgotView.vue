<template>
  <main class="form-signin w-100 m-auto">
   <form  @submit.prevent="submit">
    <!-- <img class="mb-4" src="../src/assets/logo.png" alt="" width="72" height="57"> -->
     <div v-if="notify.cls" :class="`alert alert-${notify.cls}`" role="alert">
        {{ notify.message }}
     </div>
    <h1 class="h3 mb-3 fw-normal">Recover Password</h1>

    <div class="form-floating">
      <input  v-model="email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email address</label>
    </div>


   
    <button class="btn btn-primary w-100 py-2 mt-3" type="submit">Submit</button>
    <p class="mt-5 mb-3 text-body-secondary">&copy; 2017–2024</p>
  </form>
</main>
</template>

<script lang="ts">

import { ref, reactive } from 'vue';
import axios from 'axios';
// import { useRouter } from 'vue-router';
export default {
    name: 'ForgotView',
    setup () {
        const email = ref('') 
        const notify = reactive({cls: '', message: ''})
        const submit = async () => {
            try {
                console.log('testing');
                await axios.post('forgot', {
                email: email.value
                });
                notify.cls="success"
                notify.message="Email was sent"
           
            } catch (e) {
                notify.cls="danger"
                notify.message="Email doesn't exist"
            }
        }
           
          return {
            email, submit, notify
          }
        
    }
}
</script>

<style scoped>

</style>