import CurrentUserInfo from './components/CurrentUserInfo.js'
import Services from './components/Services.js'
const SERVICE_LOGIN = 'SERVICE_LOGIN';

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
        Services.getServiceUrl(SERVICE_LOGIN)
         .then(service_url => {
            var url = service_url +  '/current-user';
            axios.get(url, {withCredentials: true}
            )
                .then(response => {
                    this.user = response.data;
                    this.logged_in = true;
                    this.logged_in_as_admin = this.user["is_admin"] > 0
                })
                .catch(error => {
                    console.log(error);
                });
         })
         .catch(error => {
                console.log(error);
         });
        }
      });

admin_app.mount('#admin-app')