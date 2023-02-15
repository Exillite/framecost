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
                <div class="align-center flex-column">
                <ul id="shos-list">
                    <div v-for="shop in shops" :key="shop.id">
                        <v-card
                            class="auto"
                            variant="outlined"
                        >
                            <v-card-item>
                            <div>
                                <div class="text-overline mb-1">
                                Магазин
                                </div>
                                <div class="text-h6 mb-1">
                                {{ shop.title }}
                                </div>
                                <div class="text-caption">{{ shop.owner }}</div>
                            </div>
                            <div class="text--primary">
    
                            </div>
                            </v-card-item>
                            
                            <v-card-actions>
                            <v-btn variant="outlined">
                                Открыть
                            </v-btn>
                            </v-card-actions>
                        </v-card>
                    </div>
                </ul>
                
            </div>

            </v-container>
        </v-main>
    </v-app>
</template>

<script>
    export default {
        data () {
            return {
                shops: [
                    {
                        id: "234789234",
                        title: 'Mokos',
                        owner: 'Peta Petrov',
                        products_cnt: 34,
                        templates_cnt: 8,
                    },
                ],
            }
        },
    }
</script>

<style>
    .v-card {
        margin-bottom: 10px;
    }
</style>