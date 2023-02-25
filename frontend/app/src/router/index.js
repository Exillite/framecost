import Main from '@/pages/Main.vue'
import { createWebHistory, createRouter } from 'vue-router'
import cookie from '@/cookie'


function check_is_login() {
    if (cookie.getCookie('user_id') === undefined) {
        return true;
    }
    return true;
}

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
    {
        path: '/registration',
        name: 'Registration',
        component: () =>
            import ('@/pages/Registration.vue'),
    },
    {
        path: '/shops',
        name: 'Shops',
        component: () =>
            import ('@/pages/Shops.vue'),
    },
    {
        path: '/shop/:slug',
        name: 'Shop',
        component: () =>
            import ('@/pages/Shop.vue'),
    },
    {
        path: '/product/:slug',
        name: 'Product',

        component: () =>
            import ('@/pages/Product.vue'),
    },
    {
        path: '/:pathMatch(.*)*',
        component: () =>
            import ('@/pages/404.vue'),
    }
]

const router = new createRouter({
    history: createWebHistory(),
    routes
})


export default router