import CurrentUserInfo from './components/CurrentUserInfo.js'

var admin_app = Vue.createApp({
      components: {
        CurrentUserInfo
      },
      data() {
          return  {
            user: {},
            logged_in: false,
            logged_in_as_admin: false
          }
      },
      mounted () {
        axios.get('/user/current')
            .then(response => {
                console.log(response)
                this.user = response.data
                this.logged_in = true;
                this.logged_in_as_admin = this.user["is_admin"]
            })
            .catch(error => {
                console.log(error);
            });
        }
      });

admin_app.mount('#admin-app')