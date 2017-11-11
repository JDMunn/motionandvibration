<template>
  <v-app light>
    <v-toolbar fixed>
      <v-spacer></v-spacer>
      <v-toolbar-title v-html="title"></v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <main>
      <v-container fluid class="mb-5">
        <nuxt />
      </v-container>
    </main>
    <v-footer fixed>
      <span><a href="https://facebook.com/amareanline">facebook.com/amareanline</a></span>
      <v-spacer></v-spacer>
      <span>999</span>
      <v-spacer></v-spacer>
      <span><a href="https://instagram.com/amareanline">instagram.com/amareanline</a></span>
    </v-footer>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        clipped: false,
        drawer: true,
        fixed: false,
        items: [
          { to: '/' },
          { to: '/submit', example: 'foo' }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: '<b>motion</b> and <b>vibration</b>'
      }
    }
  }
</script>
