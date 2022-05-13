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
         console.log(service_url)
            var url = service_url +  '/current-user';
            console.log(url);
            axios.get(url, {withCredentials: true}
            )
                .then(response => {
                    console.log(response);
                    console.log(response.data);
                    console.log(response.data.id);
                    console.log(response.data.firstname);
                    this.user = response.data;
                    this.logged_in = true;
                    console.log(this.user);
                    console.log(this.user['is_admin']);
                    console.log(this.user.is_admin);
                    console.log(response.data.is_admin);
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