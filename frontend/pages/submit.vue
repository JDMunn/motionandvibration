<template>
  <v-container>
    <v-layout column justify-center align-center>
      <v-flex xs12 sm10 md10>
        <v-stepper v-model="submission.step">
          <v-stepper-header>
            <v-stepper-step step="1" :complete="submission.step > 1">select a category</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="2" :complete="submission.step > 2">select a focus</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="3">describe your project</v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="3">upload</v-stepper-step>
          </v-stepper-header>
          <v-stepper-content step="1">
            <v-select
              :items="['motion', 'vibration']"
              v-model="submission.category"
              label="category"
              single-line
              bottom
            ></v-select>
            <v-btn primary @click.stop="submission.step = 2">Continue</v-btn>
            <v-btn flat nuxt to="/">Cancel</v-btn>
          </v-stepper-content>
          <v-stepper-content v-if="submission.category === 'motion'" step="2">
            motino
            <v-btn primary @click.stop="submission.step = 3">Continue</v-btn>
            <v-btn flat @click.stop="submission.step = 1">Cancel</v-btn>
          </v-stepper-content>
          <v-stepper-content v-else step="2">
            vibration
            <v-btn primary @click.stop="submission.step = 3">Continue</v-btn>
            <v-btn flat @click.stop="submission.step = 1">Cancel</v-btn>
          </v-stepper-content>
          <v-stepper-content step="3">
            <v-btn primary @click.stop="submission.step = 1">Continue</v-btn>
            <v-btn flat @click.stop="submission.step = 2">Cancel</v-btn>
          </v-stepper-content>
        </v-stepper>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        submission: {
          step: 0,
          category: null
        }
      }
    }
  }
</script>
