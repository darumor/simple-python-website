import CurrentUserInfo from './components/CurrentUserInfo.js'

var restricted_app = Vue.createApp({
      components: {
        CurrentUserInfo
      },
      data() {
          return {
            user: {},
            logged_in: false
          }
      },
      mounted () {
        axios.get('/user/current')
            .then(response => {
                console.log(response)
                this.user = response.data
                this.logged_in = true;
            })
            .catch(error => {
                console.log(error);
            });
        }
      });

restricted_app.mount('#restricted-app')