<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm10 md10>
      <v-card hover>
        <v-card-media height="300px" src="/a_1.jpg"></v-card-media>
        <v-card-title class="headline">
          the national music and film festival of the Amarean Isles
        </v-card-title>
        <v-card-text>
          <h6>theme: Sky Islands</h6>
          <p>media will be judged by the inhabitants and artists of the Amarean Isles</p>
          <p>submissions open: 10/11/17</p>
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
                  :error="this.errors.category.length === 0 ? false : true"
                  :error-messages="this.errors.category"
                  @input="validate([{field: 'category', errorMessage: 'please select a category'}], 1)"
                  v-model="submission.category"
                  label="category"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="validate([{field: 'category', errorMessage: 'please select a category'}], 2)">continue</v-btn>
                <v-btn flat @click.stop="submission.started = false">cancel</v-btn>
              </v-stepper-content>
              <v-stepper-content v-if="submission.category === 'motion'" step="2">
                <v-select
                  :items="['documentary', 'live action', 'animation', 'experimental']"
                  :error="this.errors.focus.length === 0 ? false : true"
                  :error-messages="this.errors.focus"
                  @input="validate([{field: 'focus', errorMessage: 'please select a focus'}], 2)"
                  v-model="submission.focus"
                  label="focus"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="validate([{field: 'focus', errorMessage: 'please select a focus'}], 3)">continue</v-btn>
                <v-btn flat @click.stop="submission.step = 1">back</v-btn>
              </v-stepper-content>
              <v-stepper-content v-else step="2">
                <v-select
                  :items="['acoustic', 'electronic']"
                  :error="this.errors.focus.length === 0 ? false : true"
                  :error-messages="this.errors.focus"
                  @input="validate([{field: 'focus', errorMessage: 'please select a focus'}], 2)"
                  v-model="submission.focus"
                  label="focus"
                  single-line
                  bottom
                ></v-select>
                <v-btn secondary @click.stop="validate([{field: 'focus', errorMessage: 'please select a focus'}], 3)">continue</v-btn>
                <v-btn flat @click.stop="submission.step = 1">back</v-btn>
              </v-stepper-content>
              <v-stepper-content step="3">
                <v-text-field
                  name="submission-title"
                  v-model="submission.title"
                  label="project title"
                  :error="this.errors.title.length === 0 ? false : true"
                  :error-messages="this.errors.title"
                  @input="validate([{field: 'title', errorMessage: 'please add a title for your submission'}], 3)"
                ></v-text-field>
                <v-text-field
                  name="submission-description"
                  v-model="submission.description"
                  label="project description"
                  multi-line
                  :error="this.errors.description.length === 0 ? false : true"
                  :error-messages="this.errors.description"
                  @input="validate([{field: 'description', errorMessage: 'please add a description of your project'}], 3)"
                ></v-text-field>
                <v-text-field
                  name="submission-name"
                  v-model="submission.name"
                  label="your name"
                  :error="this.errors.name.length === 0 ? false : true"
                  :error-messages="this.errors.name"
                  @input="validate([{field: 'name', errorMessage: 'please provide your name, it will be displayed alongside your submission'}], 3)"
                ></v-text-field>
                <v-text-field
                  name="submission-email"
                  v-model="submission.email"
                  label="your email"
                  :error="this.errors.email.length === 0 ? false : true"
                  :error-messages="this.errors.email"
                  @input="validate([{field: 'email', errorMessage: 'please provide your email, it will only be used to contact you if you win'}], 3)"
                ></v-text-field>
                <v-btn secondary @click.stop="validate([{field: 'title', errorMessage: 'please add a title for your submission'}, {field: 'description', errorMessage: 'please add a description of your project'}, {field: 'name', errorMessage: 'please provide your name, it will be displayed alongside your submission'}, {field: 'email', errorMessage: 'please provide your email, it will only be used to contact you if you win'}], 4)">continue</v-btn>
                <v-btn flat @click.stop="submission.step = 2">back</v-btn>
              </v-stepper-content>
              <v-stepper-content step="4">
                <dropzone v-if="directUploadsEnabled" id="submission-file"
                  :url="uploadUrl"
                  v-on:vdropzone-success="submission.canFinish = true; submission.link = `http://motionandvibration.com/api/uploads/${submission.title.replace(/ /g,'_')}`">
                  <!-- Optional parameters if any! -->
                  <input type="hidden" name="token" value="xxx">
                </dropzone>
                <br v-if="directUploadsEnabled">
                <p v-if="directUploadsEnabled" class="text-xs-center"><i>or</i></p>
                <v-text-field
                  name="submission-link"
                  v-model="submission.link"
                  label="link to your project (soundcloud, youtube, vimeo, etc.)"
                  :error="this.errors.link.length === 0 ? false : true"
                  :error-messages="this.errors.link"
                  @input="validate([{field: 'link', errorMessage: 'please add a link to your project'}], 4)"
                ></v-text-field>
                <v-btn info @click.stop="validate([{field: 'link', errorMessage: 'please either directly upload your project by dragging in a file above or add a link where it can be accessed'}], 5)">submit</v-btn>
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
          <v-btn v-if="viewSubmissionsEnabled" class="mb-3" primary block flat nuxt to="/submissions">view submissions</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
      <v-container>
        <blockquote>
          As your nerves project into your astral body, find your throat in your ears, grow your garden through the eye of an evergreen spine, each blink a sacral kiss to your creativity.
        </blockquote>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
        viewSubmissionsEnabled: false,
        directUploadsEnabled: false,
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
          email: null,
          link: null
        },
        errors: {
          category: [],
          focus: [],
          title: [],
          description: [],
          name: [],
          email: [],
          link: []
        }
      }
    },
    computed: {
      uploadUrl: function () {
        if (this.submission.title) {
          return `/api/uploads/${this.submission.title.replace(/ /g, '_')}`
        } else {
          return '/api/uploads/if_you_see_this_something_went_wrong'
        }
      }
    },
    methods: {
      submit: function () {
        let app = this
        this.axios.post('http://motionandvibration.com/api/submissions', app.submission)
          .then(response => {
            console.log(response)
            app.submission.started = false
            app.submission.finished = true
          })
          .catch(e => {
            app.submission.started = false
            app.submission.finished = true
          })
      },
      validate: function (fields, nextStep) {
        var hasErrors = false
        fields.forEach(function (field) {
          if (this.submission[field.field] !== null && this.submission[field.field] !== '') {
            this.errors[field.field] = []
          } else {
            hasErrors = true
            if (!this.errors[field.field].length) {
              this.errors[field.field].push(field.errorMessage)
            }
          }
        }, this)
        if (!hasErrors) {
          if (nextStep > 4) {
            this.submit(this.submission)
          } else {
            this.submission.step = nextStep
          }
        }
      }
    }
  }
</script>