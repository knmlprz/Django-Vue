<template>
    <v-container class="fill-height">
        <v-responsive class="align-center text-center fill-height">
            <v-card>
                <div class="py-14" />
                <h1 class="text-h2 font-weight-bold">Zaloguj</h1>
                <div class="py-14" />
                <v-col>
                    <v-form>
                        <v-text-field
                            clearable
                            label="E-mail"
                            v-model="email"
                            ></v-text-field>
                        <v-text-field
                            clearable
                            label="Hasło"
                            type="password"
                            v-model="password"></v-text-field>
                        <v-btn 
                            
                            variant="tonal"
                            @click="handleLoginButtonClick()">Zaloguj</v-btn>
                    </v-form>
                </v-col>
            </v-card>
        </v-responsive>
    </v-container>

</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';
import { login } from '@/api/auth'
const email = ref<string>('');
const password = ref<string>('');
const handleLoginButtonClick = () => {
    login(email.value, password.value)
}
</script>