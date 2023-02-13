import Main from '@/pages/Main.vue'
import { createWebHistory, createRouter } from 'vue-router'


const routes = [{
        path: '/',
        name: 'Main',
        component: Main,
    },
    {
        path: '/login',
        name: 'Login',
        component: () =>
            import ('@/pages/Login.vue'),
    },
]

const router = new createRouter({
    history: createWebHistory(),
    routes
})

export default router