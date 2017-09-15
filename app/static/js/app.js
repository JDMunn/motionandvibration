var app = new Vue({
    el: '#app',
    data: function() {
        return {
            alertFileUploaded: false,
            file: {
                name: null
            },
            rules: {
                required: (value) => !!value || 'required'
            }
        }
    },
    methods: {

    },
    mounted: function () {

    },
    computed: {

    }
});

