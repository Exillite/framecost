import Axios from 'axios';
import cookie from '@/cookie'

const api_url = 'http://127.0.0.1/api/v1';

export default {
    async test() {
        return Axios.post("http://localhost:8000/api", {}, {
            params: {
                token: cookie.getCookie('token'),
            }
        });
    },

    async register(name, surname, login, email, password) {
        return Axios.post(api_url + '/register', {
            name: name,
            surname: surname,
            login: login,
            email: email,
            password: password,
        });
    },

    async login(email, password) {
        return Axios.post(api_url + '/login', {
            email: email,
            password: password
        });
    },

    async create_shop(title) {
        return Axios.post(api_url + "/shop", {
            title: title,
        }, {
            params: {
                token: cookie.getCookie('token'),
                user_id: cookie.getCookie('user_id'),
            }
        })
    },

    async get_shop(shop_slug) {
        return Axios.get(api_url + `/shop/${shop_slug}`, {
            params: {
                token: cookie.getCookie('token'),
                user_id: cookie.getCookie('user_id'),
            },
        })
    },

    async get_all_users_shops() {
        return Axios.get(api_url + "/user/shops", {
            params: {
                token: cookie.getCookie('token'),
                user_id: cookie.getCookie('user_id'),
            }
        })
    },
}