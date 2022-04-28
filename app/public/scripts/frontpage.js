import ThingList from './components/ThingList.js'

var frontpage_app = Vue.createApp({
      components: {
        ThingList
      }
      });

frontpage_app.mount('#front-page-app')