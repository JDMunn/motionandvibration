<template data-app>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm10 md10>
      <v-progress-linear v-if="loading" indeterminate color="primary" background-color="secondary"></v-progress-linear>
      <v-card hover v-else v-for="(submission, index) in submissions" :key="index">
        <v-card-media height="33%" v-text="submission.link"></v-card-media>
        <v-card-title>
          <h4>{{ submission.title }}</h4>
          <p>{{ submission.description }}</p>
          <p>artist: {{ submission.name }}</p>
        </v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn primary>vote</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
  export default {
    data () {
      return {
        loading: true,
        submissions: []
      }
    },
    methods: {
      loadSubmissions: function () {
        this.axios.get('http://localhost:8082/submissions')
          .then(response => {
            this.submissions = response.data
            this.loading = false
          })
      }
    },
    mounted: function () {
      this.loadSubmissions()
    }
  }
</script>