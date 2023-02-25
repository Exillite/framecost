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
                                                                    
                        <div style="margin-top: 10px;">
                            <v-btn variant="outlined" block
                            color="blue-grey"
                            @click="newTemplateDialog = true">
                                Добавить шаблон
                            </v-btn>
                        </div>
                        
                        <div v-for="template in templates" :key="template.id">
                            <v-card
                                class="mx-auto"
                                variant="outlined"
                            >
                                <v-card-item>
                                <div>
                                    <div class="text-h6 mb-1">
                                        {{ template.title }}
                                    </div>
                                    <div class="text-caption">
                                        Количество товаров: {{ template.products.length }}
                                    </div>
                                </div>
                                </v-card-item>
                                
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn variant="outlined"
                                    @click="openEditTemplate(template)">
                                        Открыть
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </div>

                    </v-window-item>

                    <v-window-item :value="3">
                        
                    </v-window-item>

                    <v-window-item :value="4" style="margin-top: 10px;">
                        <div v-for="admin in shop.admins" :key="admin.id" style="font-size: large;">
                            {{ admin.name }} {{ admin.surname }}
                        </div>

                        <v-form style="margin-top: 10px;">
                            <v-text-field
                                label="E-mail нового администратора"
                                v-model="es_admin_email"
                                required
                                default=""
                                type="email"
                                variant="outlined"
                            ></v-text-field>

                            <v-btn type="submit"
                                block
                                variant="outlined"
                                color="success"
                                @click="add_admin()"
                                style="margin-bottom: 10px;"
                            >Добавить</v-btn>                           
                        </v-form>
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


    <v-dialog
        v-model="newTemplateDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <v-text-field
                label="Название"
                v-model="nt_title"
                required
                ></v-text-field>

                <v-select
                    v-model="nt_products"
                    :items="products_list"
                    label="Выберете товары"
                    multiple
                    persistent-hint
                ></v-select>

            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                @click="newTemplateDialog = false"
                variant="outlined"
                color="error"
            >
                Отмена
            </v-btn>
                
            <v-btn
                @click="create_template()"
                variant="outlined"
                color="success"
            >
                Добавить
            </v-btn>

        </v-card-actions>
    </v-card>
    </v-dialog>


    <v-dialog
        v-model="editTemplateDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <h3>{{ et_title }}</h3>

                <v-list :items="et_products"></v-list>

            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                @click="delete_template()"
                variant="outlined"
                color="error"
            >
                Удалить
            </v-btn>
                
            <v-btn
                @click="editTemplateDialog = false;"
                variant="outlined"
                color="success"
            >
                ОК
            </v-btn>

        </v-card-actions>
    </v-card>
    </v-dialog>

    <v-dialog
        v-model="editTemplateDialog"
        width="1000px"
        persistent
    >
    <v-card>
        <v-card-text>
            <v-form>
                <h3>{{ et_title }}</h3>

                <v-list :items="et_products"></v-list>

            </v-form>
        </v-card-text>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                @click="delete_template()"
                variant="outlined"
                color="error"
            >
                Удалить
            </v-btn>
                
            <v-btn
                @click="editTemplateDialog = false;"
                variant="outlined"
                color="success"
            >
                ОК
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
                newTemplateDialog: false,
                editTemplateDialog: false,

                shop: {},
                products: [],
                templates: [],
                activeTab: 1,
                
                np_title: "",
                np_category: "",
                np_price: null,

                nt_title: null,
                nt_products: [],

                es_admin_email: null,

                et_id: null,
                et_title: null,
                et_products: [],

                products_list: [],
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

            create_template() {
                const nt_prd = {};
                nt_prd.products = [];
                this.nt_products.forEach(function(el) {
                    nt_prd.products.push({product_id: el})
                });

                api.create_tempalte(this.nt_title, this.shop.id, JSON.stringify(nt_prd)).then((r) => {
                    api.get_shops_templates(this.shop.slug).then((r) => {
                        this.templates = r.data.templates;
                    });
                });


                this.newTemplateDialog = false;
            },

            add_product_to_list(product) {
                this.products_list.push({title: product.title, value: product.id})
            },

            add_edit_product_to_list(product) {
                this.et_products.push({title: product.title, value: product.id})
            },

            openEditTemplate(template) {
                this.et_title = template.title;
                template.products.forEach(element => this.add_edit_product_to_list(element));
                this.et_id = template.id;

                this.editTemplateDialog = true;
            },

            delete_template() {
                api.delete_template(this.et_id).then((response) => {
                    api.get_shops_templates(this.shop.slug).then((r) => {
                        this.templates = r.data.templates;
                    });
                });

                this.editTemplateDialog = false;
            },

            add_admin() {
                api.add_shop_admin(this.es_admin_email, this.shop.slug);
            },
        },

        mounted() {
            api.get_shop(this.$route.params.slug).then((response) => {
                this.shop = response.data.shop;
                
                api.get_shops_products(this.shop.slug).then((response) => {
                    this.products = response.data.products;
                    this.products.forEach(element => this.add_product_to_list(element));
                });

                api.get_shops_templates(this.shop.slug).then((r) => {
                    this.templates = r.data.templates;
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