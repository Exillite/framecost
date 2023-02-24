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

                <h1>{{ product.title }}</h1>
                <h3>{{ product.category }}</h3>
                <h3>{{ product.price }}₽</h3>

                <v-tabs fixed-tabs
                v-model="activeTab">
                    <v-tab :value="1">
                    Товары
                    </v-tab>

                    <v-tab :value="2">
                    Параметры
                    </v-tab>

                </v-tabs>


                <v-window v-model="activeTab">
                    <v-window-item :value="1">
                                                
                        <div style="margin-top: 10px;">
                            <v-btn variant="outlined" block
                            color="blue-grey"
                            @click="newItemDialog = true">
                                Добавить
                            </v-btn>
                        </div>
                        
                        <div v-for="item in items" :key="item.id">
                            <v-card
                                class="mx-auto"
                                variant="outlined"
                            >
                                <v-card-item>
                                <div>
                                    <div v-if="item.params.cnt == 0">
                                        <div class="text-h6 mb-1" >
                                            {{ product.title }}
                                        </div>
                                        <div class="text-caption">
                                            Параметры отсутствуют
                                        </div>
                                    </div>
                                    <div v-if="item.params.cnt == 1">
                                        <div class="text-h6 mb-1" >
                                            {{ product.title }}
                                        </div>
                                        <div class="text-caption">
                                            {{ item.params.a }}
                                        </div>
                                    </div>
                                    <div v-if="item.params.cnt == 2">
                                        <div class="text-h6 mb-1" >
                                            {{ product.title }}
                                        </div>
                                        <div class="text-caption">
                                            {{ item.params.a }} × {{ item.params.b }}
                                        </div>
                                    </div>
                                </div>
                                </v-card-item>
                                
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn variant="outlined"
                                    @click="openItemEdit(item)">
                                        Редактировать
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>

                    </v-window-item>

                    <v-window-item :value="2">
                        <v-form style="margin-top: 10px;">
                            <v-text-field
                                label="Название"
                                v-model="ep_title"
                                required
                                default=""
                                variant="outlined"
                            ></v-text-field>

                            <v-text-field
                                label="Категория"
                                v-model="ep_category"
                                required
                                default=""
                                variant="outlined"
                            ></v-text-field>

                            <v-text-field
                                label="Цена"
                                v-model="ep_price"
                                required
                                type="number"
                                min="0.01"
                                default=""
                                step="0.01"
                                variant="outlined"
                            ></v-text-field>


                            <v-btn type="submit" 
                            block
                            variant="outlined"
                            color="success"
                            @click="edit_product()"
                            style="margin-bottom: 10px;"
                            >Обновить</v-btn>

                            <v-btn 
                            block
                            variant="outlined"
                            color="error"
                            @click="delete_product()"
                            >Удалить</v-btn>
                            
                        </v-form>
                    </v-window-item>
                </v-window>
            </v-container>
        </v-main>
    </v-app>

    <v-dialog
        v-model="newItemDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <v-select
                    v-model="ni_count_params"
                    :items="[
                        { title: 'Параметры не требуются', value: 0 },
                        { title: 'Один параметр', value: 1 },
                        { title: 'Два параметра', value: 2 },
                    ]"
                    :rules="[v => !(v==null) || 'Выберите один из пунктов']"
                    label="Количество параметров"
                    required
                    variant="outlined"
                ></v-select>


                <v-text-field
                    v-if="ni_count_params >= 1"

                    label="параметр №1"
                    v-model="ni_a"
                    required
                    type="number"
                    min="0.01"
                    default=""
                    step="0.01"
                    variant="outlined"
                ></v-text-field>


                <v-text-field
                    v-if="ni_count_params == 2"

                    label="параметр №2"
                    v-model="ni_b"
                    required
                    type="number"
                    min="0.01"
                    default=""
                    step="0.01"
                    variant="outlined"
                ></v-text-field>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                @click="newItemDialog = false"
                variant="outlined"
                color="error"
            >
                Отмена
            </v-btn>
                
            <v-btn
                @click="create_item()"
                variant="outlined"
                color="success"
            >
                Добавить
            </v-btn>

        </v-card-actions>
    </v-card>
    </v-dialog>


    <v-dialog
        v-model="editItemDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <v-select
                    v-model="ei_count_params"
                    :items="[
                        { title: 'Параметры не требуются', value: 0 },
                        { title: 'Один параметр', value: 1 },
                        { title: 'Два параметра', value: 2 },
                    ]"
                    :rules="[v => !(v==null) || 'Выберите один из пунктов']"
                    label="Количество параметров"
                    required
                    variant="outlined"
                ></v-select>


                <v-text-field
                    v-if="ei_count_params >= 1"

                    label="параметр №1"
                    v-model="ei_a"
                    required
                    type="number"
                    min="0.01"
                    default=""
                    step="0.01"
                    variant="outlined"
                ></v-text-field>


                <v-text-field
                    v-if="ei_count_params == 2"

                    label="параметр №2"
                    v-model="ei_b"
                    required
                    type="number"
                    min="0.01"
                    default=""
                    step="0.01"
                    variant="outlined"
                ></v-text-field>
            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-btn
                @click="delete_item()"
                variant="outlined"
                color="error"
            >
                Удалить
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn
                @click="editItemDialog = false"
                variant="outlined"
                color="error"
            >
                Отмена
            </v-btn>
                
            <v-btn
                @click="edit_item()"
                variant="outlined"
                color="success"
            >
                Редактировать
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
                product: {},
                items: [],

                ep_title: null,
                ep_category: null,
                ep_price: null,

                activeTab: 1,

                newItemDialog: false,
                editItemDialog: false,

                ni_count_params: null,
                ni_a: null,
                ni_b: null,

                ei_id: null,
                ei_count_params: null,
                ei_a: null,
                ei_b: null,

            }
        },

        methods: {
            create_item() {

                if (this.ni_count_params == null) {
                    return;
                }
                if (this.ni_count_params >= 1 && !this.ni_a) {
                    return;
                }
                if (this.ni_count_params == 2 && !this.ni_b) {
                    return;
                }


                const ni_params = {cnt: this.ni_count_params};
                if (this.ni_count_params >= 1) {
                    ni_params.a = parseFloat(this.ni_a);
                }
                if (this.ni_count_params == 2) {
                    ni_params.b = parseFloat(this.ni_b);
                }

                api.create_item(this.product.id, JSON.stringify(ni_params)).then((r) => {
                    console.log(r.data);
                    
                    api.get_products_items(this.$route.params.slug).then((r) => {
                        this.items = r.data.items;
                    });
                });

                this.ni_count_params = null;
                this.ni_a = null;
                this.ni_b = null;

                this.newItemDialog = false;
            },

            edit_item() {
                if (this.ei_count_params == null) {
                    return;
                }
                if (this.ei_count_params >= 1 && !this.ei_a) {
                    return;
                }
                if (this.ei_count_params == 2 && !this.ei_b) {
                    return;
                }

                const ei_params = {cnt: this.ei_count_params};
                if (this.ei_count_params >= 1) {
                    ei_params.a = parseFloat(this.ei_a);
                }
                if (this.ei_count_params == 2) {
                    ei_params.b = parseFloat(this.ei_b);
                }

                api.update_item(this.ei_id, JSON.stringify(ei_params)).then((r) => {
                    api.get_products_items(this.$route.params.slug).then((r) => {
                        this.items = r.data.items;
                    });
                })

                this.editItemDialog = false;
            },

            delete_item() {
                api.delete_item(this.ei_id).then((r) => {
                    api.get_products_items(this.$route.params.slug).then((r) => {
                        this.items = r.data.items;
                    });
                });

                this.editItemDialog = false;
            },

            openItemEdit(item) {
                this.ei_id = item.id;
                this.ei_count_params = item.params.cnt;
                this.ei_a = item.params.a;
                this.ei_b = item.params.b;

                this.editItemDialog = true;
            },

            edit_product() {
                api.update_product(this.product.slug, this.ep_title, this.ep_category, this.ep_price);
            },

            delete_product() {
                api.delete_product(this.product.slug);
                this.$router.push({name: 'Shop', params: {'slug': this.product.shop.slug }});
            },

        },

        mounted() {
            api.get_product(this.$route.params.slug).then((r) => {
                this.product = r.data.product;

                api.get_products_items(this.$route.params.slug).then((r) => {
                    this.items = r.data.items;
                });

                this.ep_title = this.product.title;
                this.ep_category = this.product.category;
                this.ep_price = this.product.price;
                
            });
        },
    }
</script>

<style>
    .v-card {
        margin-top: 10px;
    }
</style>