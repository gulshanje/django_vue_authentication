
import LoginPage from '@/components/Login.vue';
import RegisterPage from '@/components/Register.vue';
import HomePage from '@/components/Home.vue';
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
    {
        name: 'Login',
        component: LoginPage,
        path: '/login'
    },
    {
        name: 'Register',
        component: RegisterPage,
        path: '/register'
    },
    {
        name: 'Home',
        component: HomePage,
        path: '/'
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router