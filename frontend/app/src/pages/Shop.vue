<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title>ЛОГО</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-btn icon>
                <v-icon>mdi-export</v-icon>
            </v-btn>
        </v-app-bar>
        <v-main>
            <v-container>

                <h1>{{ shop.title }}</h1>


                <v-tabs fixed-tabs
                v-model="activeTab">
                    <v-tab :value="1">
                    Товары
                    </v-tab>

                    <v-tab :value="2">
                    Шаблоны
                    </v-tab>

                    <v-tab :value="3">
                    Заказы
                    </v-tab>

                    <v-tab :value="4">
                    Параметры
                    </v-tab>
                </v-tabs>


                <v-window v-model="activeTab">
                    <v-window-item :value="1">
                                                
                        <div style="margin-top: 10px;">
                            <v-btn variant="outlined" block
                            color="blue-grey"
                            @click="newProductDialog = true">
                                Добавить товар
                            </v-btn>
                        </div>
                        
                        <div v-for="product in products" :key="product.id">
                            <v-card
                                class="mx-auto"
                                variant="outlined"
                            >
                                <v-card-item>
                                <div>
                                    <div class="text-overline mb-1">
                                        {{ product.category }}
                                    </div>
                                    <div class="text-h6 mb-1">
                                    {{ product.title }}
                                    </div>
                                    <div class="text-caption">{{ product.price }}₽</div>
                                </div>
                                </v-card-item>
                                
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn variant="outlined"
                                    @click="$router.push({name: 'Product', params: {'slug': product.slug }})">
                                        Открыть
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>

                    </v-window-item>

                    <v-window-item :value="2">
                    Two
                    </v-window-item>

                    <v-window-item :value="3">
                    Three
                    </v-window-item>

                    <v-window-item :value="4">
                    Threeddd
                    </v-window-item>
                </v-window>
            </v-container>
        </v-main>
    </v-app>

    <v-dialog
        v-model="newProductDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <v-text-field
                label="Название"
                v-model="np_title"
                required
                ></v-text-field>
                <v-text-field
                label="Категория"
                v-model="np_category"
                required
                ></v-text-field>
                <v-text-field
                label="Цена"
                v-model="np_price"
                required
                type="number"
                min="0.01"
                default=""
                step="0.01"
                ></v-text-field>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                @click="newProductDialog = false"
                variant="outlined"
                color="error"
            >
                Отмена
            </v-btn>
                
            <v-btn
                @click="create_product()"
                variant="outlined"
                color="success"
            >
                Добавить
            </v-btn>

        </v-card-actions>
    </v-card>
    </v-dialog>

</template>

<script>
    import api from '@/api'

    export default {
        
        data() {
            return {
                newProductDialog: false,
                shop: {},
                products: [],
                activeTab: 1,
                
                np_title: "",
                np_category: "",
                np_price: null,
            }
        },

        methods: {
            create_product() {
                api.create_product(this.np_title, this.np_category, this.np_price, this.shop.id);

                api.get_shops_products(this.shop.slug).then((response) => {
                    console.log(response.data);
                    this.products = response.data.products;
                });

                this.newProductDialog = false;
            },
        },

        mounted() {
            api.get_shop(this.$route.params.slug).then((response) => {
                this.shop = response.data.shop;
                
                api.get_shops_products(this.shop.slug).then((response) => {
                    console.log(response.data);
                    this.products = response.data.products;
                });
            });
            

        },
    }
</script>

<style>
    .v-card {
        margin-top: 10px;
    }
</style>