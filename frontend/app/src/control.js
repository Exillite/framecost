import cookie from "@/cookie"

export default {
    check_auth(page) {
        const token = cookie.getCookie('token');
        if (!token) {
            page.$router.push({ name: 'Login' });
        }
    },
}