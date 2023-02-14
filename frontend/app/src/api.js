import Axios from 'axios';
import cookie from '@/cookie'

const api_url = 'http://127.0.0.1/api/v1';

export default {
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

    async test() {
        return Axios.post("http://localhost:8000/api", {}, {
            params: {
                token: cookie.getCookie('token'),
            }
        });
    }

}