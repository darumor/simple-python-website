import CurrentUserInfo from './components/CurrentUserInfo.js'
import Services from './components/Services.js'
const SERVICE_LOGIN = 'SERVICE_LOGIN';

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
        Services.getServiceUrl(SERVICE_LOGIN)
         .then(service_url => {
            var url = service_url +  '/current-user';
            axios.get(url, {withCredentials: true}
            )
            .then(response => {
                this.user = response.data
                this.logged_in = true;
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

restricted_app.mount('#restricted-app')