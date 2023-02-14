<template>
    <v-app>
        <v-app-bar app>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
            <v-toolbar-title>ЛОГО</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn 
            @click="$router.push({name: 'Registeration'})"
            text>Зарегистрироваться</v-btn>
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
            <h2>Вход</h2>
            <form @submit.prevent="submit">
            <v-text-field
                v-model="email"
                label="E-mail"
                type="email"
                required
                autocomplete="email"
            ></v-text-field>
            <v-text-field
                v-model="password"
                label="Пароль"
                type="password"
                required
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
                email: '',
                password: '',
                error: false,
            }
        },
        methods: {
            submit() {
                api.login(this.email, this.password).then((response) => {
                    // console.log(response);
                    if (response.data.status == 200) {
                        const st = JSON.stringify(response.data.tocken)

                        // set cookie token on month
                        cookie.setCookie('token', st, {'max-age': 2592000});
                        this.$router.push({name: 'Main'});

                    } else {
                        this.error = true;
                    }
                }).catch((error) => {
                    this.error = true;
                    console.log(error);
                })
            }
        }
    }
</script>

<style>
</style>
