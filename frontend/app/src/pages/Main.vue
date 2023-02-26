<template>
<div class="hi">
    <h1>{{ hi }}</h1>
</div>
</template>

<script>

    import api from '@/api'

    export default {
        data() {
            return {
                hi: 'hi!',
            }
        },
        mounted() {

            $router.push({name: 'Login'});

            api.test().then((response) => {
                console.log(response);
                this.hi = response.data.message;
            })
        },
    }
</script>

<style>

</style>