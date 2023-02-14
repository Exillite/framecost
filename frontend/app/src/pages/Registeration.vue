<template>
    <v-app>
        <v-app-bar app>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
            <v-toolbar-title>ЛОГО</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn 
            text
            @click="$router.push({name: 'Login'})"
            >Войти</v-btn>
        </v-app-bar>
      <v-main>
        <v-container>
            <v-alert
                v-if="error"
                type="error"
                dismissible
            >
                <v-alert-title>Ошибка</v-alert-title>
                <v-alert-description>Неверный логин или пароль</v-alert-description>
            </v-alert>
            <h2>Регистрация</h2>
            <form @submit.prevent="submit">
            <v-text-field
                v-model="name"
                label="Имя"
                type="text"
                required
                :rules="nameRules"
                autocomplete="given-name"
            ></v-text-field>
            <v-text-field
                v-model="surname"
                label="Фамилия"
                type="text"
                required
                :rules="surnameRules"
                autocomplete="family-name"
            ></v-text-field>
            <v-text-field
                v-model="login"
                label="Логин"
                type="text"
                required
                :rules="loginRules"
                autocomplete="nickname"
            ></v-text-field>
            <v-text-field
                v-model="email"
                label="E-mail"
                type="email"
                required
                :rules="emailRules"
                autocomplete="email"
            ></v-text-field>
            <v-text-field
                v-model="password"
                label="Пароль"
                type="password"
                required
                :rules="passwordRules"
                autocomplete="current-password"
            ></v-text-field>
            <v-text-field
                v-model="repit_password"
                label="Повторите пароль"
                type="password"
                required
                :rules="repit_passwordRules"
                autocomplete="current-password"
            ></v-text-field>
            <v-btn type="submit" color="primary">Войти</v-btn>
        </form>
        </v-container>

      </v-main>
      
    </v-app>
  </template>

<script>
    import api from '@/api'
    import cookie from '@/cookie'

    export default {
        data() {
            return {
                name: '',
                surname: '',
                login: '',
                email: '',
                password: '',
                repit_password: '',
                error: false,

                nameRules: [
                    v => !!v || 'Введите имя',
                    v => (v && v.length < 3) || 'Имя должно быть более длинным',
                ],
                surnameRules: [
                    v => !!v || 'Введите фамилию',
                    v => (v && v.length < 3) || 'Фамилия должна быть более длинной',
                ],
                loginRules: [
                    v => !!v || 'Введите логин',
                    v => (v && v.length < 3) || 'Логин должен быть более длинным',
                ],
                emailRules: [
                    v => !!v || 'Введите E-mail',
                    v => /.+@.+\..+/.test(v) || 'E-mail должен быть валидным',
                ],
                passwordRules: [
                    v => !!v || 'Введите пароль',
                    v => (v && v.length < 6) || 'Пароль должен быть более длинным',
                ],
                repit_passwordRules: [
                    v => !!v || 'Введите пароль',
                    v => (v && v.length < 6) || 'Пароль должен быть более длинным',
                    v => (v && v === this.password) || 'Пароли не совпадают',
                ],
            }
        },
        methods: {
            submit() {
                api.register(this.name, this.surname, this.login, this.email, this.password)
                    .then(response => {
                        if (response.status === 200) {
                            this.$router.push({name: 'Home'})
                        } else {
                            this.error = true
                        }
                    })
                    .catch(error => {
                        console.log(error)
                        this.error = true
                    })
            }
        }
    }
</script>

<style>
</style>
