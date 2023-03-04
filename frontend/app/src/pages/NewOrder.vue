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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина багета №2"
                        v-model="baget2_width"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина багета №2"
                        v-model="baget2_width"
                        required
                        type="number"
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота багета"
                        v-model="baget_height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота"
                        v-model="height"
                        required
                        type="number"
                        min="0.01"
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
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Высота багета"
                        v-model="baget_height"
                        required
                        type="number"
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                    <v-text-field
                        label="Ширина паспарту"
                        v-model="paspartu_width"
                        required
                        type="number"
                        min="0.01"
                        default=""
                        step="0.01"
                        variant="outlined"
                    ></v-text-field>

                </div>

                <v-divider></v-divider>

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
                template_id: null,

                width: null,
                height: null,
                is_horisontal: true,
                baget_width: null,
                paspartu_width: null,
                baget1_width: null,
                baget2_width:null,
                baget_height: null,

            }
        },

        methods: {
            calculate() {
                const data = {};
                const templ_type = "";

                if (this.template_id == 0) {
                    templ_type = ""; // TODO sttfr
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget_width = this.baget_width;
                }
                if (this.template_id == 1) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = this.baget_width;
                    data.paspartu_width = this.paspartu_width;
                }
                if (this.template_id == 2) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget_width = this.baget_width;
                }
                if (this.template_id == 3) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget1_width = this.baget1_width;
                    data.baget2_width = this.baget2_width;
                }
                if (this.template_id == 4) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget_width = this.baget_width;
                }
                if (this.template_id == 5) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;
                    
                    data.baget1_width = this.baget1_width;
                    data.baget2_width = this.baget2_width;
                    data.paspartu_width = this.paspartu_width;
                }
                if (this.template_id == 6) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = this.baget_width;
                    data.paspartu_width = this.paspartu_width;
                }
                if (this.template_id == 7) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = this.baget_width;
                    data.paspartu_width = this.paspartu_width;
                }
                if (this.template_id == 8) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = this.baget_width;
                    data.paspartu_width = this.paspartu_width;
                }
                if (this.template_id == 8) {
                    data.width = this.width;
                    data.height = this.height;
                    data.is_horisontal = this.is_horisontal;

                    data.baget_width = this.baget_width;
                    data.paspartu_width = this.paspartu_width;
                    data.paspartu_width = this.paspartu_width;
                }

                api.get_tmplate_prices()
            }
        },
    }
</script>

<style>

</style>