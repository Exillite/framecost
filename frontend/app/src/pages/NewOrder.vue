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
                <h1>Новый заказ</h1>

                
                <v-select
                    v-model="template_id"
                    :items="[
                        { title: 'Без паспарту', value: 0 },
                        { title: 'С паспарту', value: 1 },
                        { title: 'Рама с кантом', value: 2 },
                        { title: 'Двойная рама', value: 3 },
                        { title: 'Рама + натяжка на подрамником', value: 4 },
                        { title: 'Двойная рама с паспарту', value: 5 },
                        { title: 'Рама с кантом и одинарным паспарту', value: 6 },
                        { title: 'Рама с кантом и двойным паспарту', value: 7 },
                        { title: 'Объемное оформление. Рамочка', value: 8 },
                        { title: 'Объемное оформление. Рамочка с паспарту', value: 9 },
                    ]"
                    :rules="[v => !(v==null) || 'Выберите один из пунктов']"
                    label="Количество параметров"
                    required
                    variant="outlined"
                ></v-select>

                <v-divider></v-divider>

                <div v-if="template_id == 0">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 1">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 2">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 3">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета №1"
                        v-model="baget1_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина багета №2"
                        v-model="baget2_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 4">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 5">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета №1"
                        v-model="baget1_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина багета №2"
                        v-model="baget2_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 6">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 7">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 8">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота багета"
                        v-model="baget_height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <div v-if="template_id == 9">
                    <v-text-field
                        label="Ширина"
                        v-model="width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-checkbox 
                        label="Горизантально"
                        v-model="is_horisontal"
                    ></v-checkbox>

                    <v-text-field
                        label="Ширина багета"
                        v-model="baget_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота багета"
                        v-model="baget_height"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.000000001"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <v-btn
                    v-if="template_id != null"

                    @click="calculate()"
                    variant="outlined"
                    color="success"
                >
                    Расчитать параметры
                </v-btn>

                <v-divider></v-divider>

                <div v-for="item in items">
                    <h3>{{ item.title }} - {{ item.value }}</h3>
                    <v-autocomplete
                        v-model="item.product"
                        :items="products"
                        item-title="title"
                        label="Продукт"
                        :clearable="true"
                        @update:model-value="selectProduct(item)"
                    ></v-autocomplete>

                    <v-select
                        v-if="item.product"

                        label="Выбор товара"
                        :items="item.items"
                        item-title="txt"
                        item-value="id"
                        v-model="item.item"
                    ></v-select>
                </div>

                <br>

                <v-btn
                    v-if="items.length > 0"

                    @click="get_order_price()"
                    variant="outlined"
                    color="success"
                >
                    Расчитать стоимость
                </v-btn>

                <h2 v-if="order_price">{{ order_price }}₽</h2>
                <br>
                <v-btn
                    v-if="items.length > 0"

                    @click="create_order()"
                    variant="outlined"
                    color="success"
                >
                    Создать заказ
                </v-btn>


            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    import api from '@/api'
    import control from '@/control';

    export default {
        data() {
            return {
                shop: {},

                template_id: null,

                products: [],

                items: [],

                params: {},

                width: null,
                height: null,
                is_horisontal: true,
                baget_width: null,
                paspartu_width: null,
                baget1_width: null,
                baget2_width:null,
                baget_height: null,

                order_price: null,
            }
        },

        methods: {
            calculate() {
                const data = {};
                let templ_type = "";

                if (this.template_id == 0) {
                    templ_type = "WithOut_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget_width = parseFloat(this.baget_width);
                }
                if (this.template_id == 1) {
                    templ_type = "With_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                    data.paspartu_width = parseFloat(this.paspartu_width);
                }
                if (this.template_id == 2) {
                    templ_type = "Rama_With_Cant";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                }
                if (this.template_id == 3) {
                    templ_type = "Double_Rama";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget1_width = parseFloat(this.baget1_width);
                    data.baget2_width = parseFloat(this.baget2_width);
                }
                if (this.template_id == 4) {
                    templ_type = "Rama_With_Natazka_Na_Podramnik";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget_width = parseFloat(this.baget_width);
                }
                if (this.template_id == 5) {
                    templ_type = "Double_Rama_With_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget1_width = parseFloat(this.baget1_width);
                    data.baget2_width = parseFloat(this.baget2_width);
                    data.paspartu_width = parseFloat(this.paspartu_width);
                }
                if (this.template_id == 6) {
                    templ_type = "Rama_With_Cant_And_Single_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                    data.paspartu_width = parseFloat(this.paspartu_width);
                }
                if (this.template_id == 7) {
                    templ_type = "Rama_With_Cant_And_Double_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                    data.paspartu_width = parseFloat(this.paspartu_width);
                }
                if (this.template_id == 8) {
                    templ_type = "Volume_Dezigne";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                    data.baget_height = parseFloat(this.baget_height);
                }
                if (this.template_id == 9) {
                    templ_type = "Volume_Dezigne_With_Paspartu";
                    data.width = parseFloat(this.width);
                    data.height = parseFloat(this.height);
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = parseFloat(this.baget_width);
                    data.baget_height = parseFloat(this.baget_height);
                    data.paspartu_width = parseFloat(this.paspartu_width);
                }
                api.get_tmplate_prices(templ_type, JSON.stringify(data)).then((r) => {
                    this.params = r.data.data;

                    for (var key in this.params) {
                        const item = {};
                        item.title = key;
                        item.value = this.params[key];
                        item.product = null;
                        item.items = [];
                        item.item = null;
                        this.items.push(item);
                    }
                });
            },

            selectProduct(el) {
                // console.log(this.products);
                // console.log(el);
                var itms;
                for (var prod in this.products) {
                    if (this.products[prod].title === el.product) {
                        itms = this.products[prod].items;
                        break;       
                    }
                }
                console.log(itms);
                for (var item in this.items) {
                    if (this.items[item].product == el.product) {
                        this.items[item].item = null;
                        this.items[item].items = itms;
                        break;
                    }
                }
            },

            get_order_price() {
                const data = {}
                data.cnt = 0;
                data.items = [];
                
                this.items.forEach(function(el) {
                    if (el.item != null){
                        data.cnt += 1;

                        const itm = {};
                        itm.item_id = el.item;
                        itm.cnt = 1;
                        itm.a = el.value;

                        data.items.push(itm);
                    }
                });

                api.order_price(this.shop.id, JSON.stringify(data)).then((r) => {
                    this.order_price = r.data.price;
                });
            },

            create_order() {
                const data = {}
                data.cnt = 0;
                data.items = [];
                
                this.items.forEach(function(el) {
                    if (el.item != null){
                        data.cnt += 1;

                        const itm = {};
                        itm.item_id = el.item;
                        itm.cnt = 1;
                        itm.a = el.value;

                        data.items.push(itm);
                    }
                });


                api.create_order(this.shop.id, JSON.stringify(data)).then((r) => {
                    this.$router.push({name: 'Shop', params: {'slug': this.shop.slug }});
                });
            },
        },

        mounted() {
            api.get_shops_products(this.$route.params.slug).then((r) => {
                this.products = r.data.products;

                this.products.forEach(function(el) {
                    api.get_products_items(el.slug).then((r) => {
                        el.items = r.data.items;
                        el.items.forEach(function(ell) {
                            if (ell.params.cnt == 0) {
                                ell.txt = "Нет параметров";
                            }
                            if (ell.params.cnt == 1) {
                                ell.txt = `${el.title} - ${ell.params.a}`
                            }
                            if (ell.params.cnt == 2) {
                                ell.txt = `${ell.params.a} x ${ell.params.b}`
                            }
                        })
                    });
                });
            });

            api.get_shop(this.$route.params.slug).then((r) => {
                this.shop = r.data.shop;
            });
        },
    }
</script>

<style>

</style>