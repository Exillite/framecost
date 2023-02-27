<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title @click="$router.push({ name: 'Main' })">ЛОГО</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon @click="log_out()">
                <v-icon>mdi-export</v-icon>
            </v-btn>
        </v-app-bar>
        <v-main>
            <v-container>
                <div class="align-center flex-column">
                    <ul id="shos-list">
                        <div v-for="shop in shops" :key="shop.id">
                            <v-card class="auto" variant="outlined">
                                <v-card-item>
                                    <div>
                                        <div class="text-overline mb-1">
                                            Магазин
                                        </div>
                                        <div class="text-h6 mb-1">
                                            {{ shop.title }}
                                        </div>
                                        <div class="text-caption">{{ shop.owner.name }} {{ shop.owner.surname }}</div>
                                    </div>
                                </v-card-item>

                                <v-card-actions>
                                    <v-btn variant="outlined"
                                        @click="$router.push({ name: 'Shop', params: { 'slug': shop.slug } })">
                                        Открыть
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>
                    </ul>
                    <v-btn style="float: right;" @click="newShopDialog = true">Создать магазин</v-btn>

                </div>

            </v-container>
        </v-main>
    </v-app>

    <v-dialog v-model="newShopDialog" width="1000px" persistent>
        <v-card>
            <v-card-text>
                <v-form>
                    <v-text-field label="Название" v-model="ns_title" required></v-text-field>

                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="newShopDialog = false" variant="outlined" color="error">
                    Отмена
                </v-btn>

                <v-btn @click="create_shop()" variant="outlined" color="success">
                    Создать
                </v-btn>

            </v-card-actions>
        </v-card>
    </v-dialog>
</template>



<script>

import api from '@/api'
import control from '@/control';

export default {
    data() {
        return {
            newShopDialog: false,

            ns_title: null,

            shops: [],
            // shops: [
            //     {
            //         id: "234789234",
            //         title: 'Mokos',
            //         owner: 'Peta Petrov',
            //     },
            // ],
        }
    },

    methods: {
        log_out() {
            control.log_out();
            this.$router.push({ name: 'Login' });
        },

        create_shop() {
            api.create_shop(this.ns_title).then((r) => {
                api.get_all_users_shops().then((response) => {
                    if (response.data.status == 200) {
                        this.shops = response.data.shops;
                    }
                }).catch((error) => {
                    console.log(error);
                })
            });

            this.newShopDialog = false;
        },
    },

    mounted() {

        if (!control.check_auth()) {
            this.$router.push({ name: 'Login' });
        }

        api.get_all_users_shops().then((response) => {
            if (response.data.status == 200) {
                this.shops = response.data.shops;
            }
        }).catch((error) => {
            console.log(error);
        })
    }
}
</script>

<style>
.v-card {
    margin-bottom: 10px;
}
</style>