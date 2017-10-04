<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm10 md10>
      <div>
        <img src="/a_1.jpg" class="mb-2" width=100%/>
      </div>
      <v-card>
        <v-card-title class="headline">
          the national music and film festival of the amarean isles
        </v-card-title>
        <v-card-text>
          <h6>theme: Sky Islands</h6>
          <p>media will be judged by the inhabitants and artists of the amarean isles</p>
          <p>submissions open: 10/11/17</p>
          <p>submissions closed: ??/??/18</p>
          <p>winners announced: ??/??/18</p>
          <hr>
          <v-container v-if="submission.started">
            <h6 class="text-xs-center">submission:</h6>
            <v-stepper secondary v-model="submission.step">
              <v-stepper-header>
                <v-stepper-step step="1" :complete="submission.step > 1">select a category</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="2" :complete="submission.step > 2">select a focus</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="3" :complete="submission.step > 3">describe your project</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="4">upload</v-stepper-step>
              </v-stepper-header>
              <v-stepper-content step="1">
                <v-select
                  :items="['motion', 'vibration']"
                  v-model="submission.category"
                  label="category"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="submission.step = 2">Continue</v-btn>
                <v-btn flat nuxt to="/">Cancel</v-btn>
              </v-stepper-content>
              <v-stepper-content v-if="submission.category === 'motion'" step="2">
                <v-select
                  :items="['documentary', 'live action', 'animation', 'experimental']"
                  v-model="submission.focus"
                  label="focus"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="submission.step = 3">continue</v-btn>
                <v-btn flat @click.stop="submission.started = false">cancel</v-btn>
              </v-stepper-content>
              <v-stepper-content v-else step="2">
                <v-select
                  :items="['acoustic', 'electronic']"
                  v-model="submission.focus"
                  label="focus"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="submission.step = 3">continue</v-btn>
                <v-btn flat @click.stop="submission.step = 1">back</v-btn>
              </v-stepper-content>
              <v-stepper-content step="3">
                <v-text-field
                  name="submission-title"
                  v-model="submission.title"
                  label="project title"
                ></v-text-field>
                <v-text-field
                  name="submission-description"
                  v-model="submission.description"
                  label="project description"
                  multi-line
                ></v-text-field>
                <v-text-field
                  name="submission-name"
                  v-model="submission.name"
                  label="your name"
                ></v-text-field>
                <v-text-field
                  name="submission-email"
                  v-model="submission.email"
                  label="your email"
                ></v-text-field>
                <v-btn secondary @click.stop="submission.step = 4">continue</v-btn>
                <v-btn flat @click.stop="submission.step = 2">back</v-btn>
              </v-stepper-content>
              <v-stepper-content step="4">
                <dropzone id="submission-file"
                  url="/api/submissions"
                  v-on:vdropzone-success="submission.canFinish = true">
                  <!-- Optional parameters if any! -->
                  <input type="hidden" name="token" value="xxx">
                </dropzone>
                <br>
                <p class="text-xs-center"><i>or</i></p>
                <v-text-field
                  name="submission-link"
                  label="link to your project (soundcloud, youtube, vimeo, etc.)"
                ></v-text-field>
                <v-btn secondary @click.stop="submission.canFinish = true">upload</v-btn>
                <v-btn flat @click.stop="submission.step = 3">back</v-btn>
              </v-stepper-content>
            </v-stepper>
          </v-container>
          <v-container v-else-if="submission.finished">
            <p>Thank you for submitting to motion and vibration, {{ submission.name.split('\ ')[0] }}! May luck be on your side.</p>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn v-if="!submission.started && !submission.finished" class="mb-3" info block flat @click.stop="submission.started = true">submit</v-btn>
          <v-btn v-if="submission.canFinish && !submission.finished" class="mb-3" info block @click.stop="submit(submission)">submit</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
      <v-container>
        <blockquote>
          Sail the light through your Kundalini - two pronged serpent tongue, stabbing the meat of the world with your lust for oblivion. The infinite is in your soul my friends!
        </blockquote>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
        submission: {
          started: false,
          canFinish: false,
          finished: false,
          step: 0,
          category: null,
          focus: null,
          title: null,
          description: null,
          name: null,
          email: null
        }
      }
    },
    methods: {
      submit: function () {
        let app = this
        this.axios.post('http://motionandvibration.com/api/submit', app.submission)
          .then(response => {
            console.log(response)
            app.submission.started = false
            app.submission.finished = true
          })
          .catch(e => {
            app.submission.started = false
            app.submission.finished = true
          })
      }
    }
  }
</script>