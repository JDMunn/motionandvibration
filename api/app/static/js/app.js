Vue2Leaflet = require('vue2-leaflet');
Vue.component('v-map', Vue2Leaflet.Map);
Vue.component('v-tilelayer', Vue2Leaflet.TileLayer);
Vue.component('v-marker', Vue2Leaflet.Marker);

var app = new Vue({
    el: '#app',
    data: function() {
        return {
            uploadLink: "https://www.youtube.com/watch?v=PX2PODoDDL0",
            backgroundImage: "/media/v_1.jpg",
            backgroundImage2: "/media/a_2.jpg",
            backgroundImage3: "/media/v_2.jpg",
            anastasiya1: "/media/a_3_flip.jpg",
            anastasiya2: "/media/a_3.jpg",
            submissionStep: 'chooseCategory',
            category: null,
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
        submitCategory: function(category) {
            this.proceedSubmission("chooseSubCategory", category);
        },
        proceedSubmission: function(step, category) {
            this.category = category;
            this.submissionStep = step;
        },
        downloadFromUploadLink: function(step, category) {
//            axios.get('/')
//                .then(response => {
//                    console.log("success")
//                    console.log(response)
//                })
//                .catch(e => {
//                    console.log("fail")
//                    console.log(e)
//                })
        }
    },
    mounted: function () {

    },
    computed: {

    }
});

