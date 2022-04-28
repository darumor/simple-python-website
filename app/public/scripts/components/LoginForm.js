import Services from './Services.js'
const SERVICE_LOGIN = 'SERVICE_LOGIN'

export default {
    data(){
        return {
            message: '',
            username: '',
            password: '',
            hasError: false,
            isSuccess: false,
            isFailed: false
        }
    },
    methods: {
        postLogin: function(event) {
            const url = Services.getServiceUrl(SERVICE_LOGIN);
            axios.post(url, {
                username: this.username,
                password: this.password
            })
            .then(response => {
                if (response.data.login_success) {
                    this.isSuccess = true;
                    this.isFailed = false;
                    this.hasError = false;
                    this.username = '*******'
                    this.password = '***********'
                    this.message = 'Login success! Please proceed to the <a href="/restricted">RESTRICTED AREA</a> or <a href="/admin">ADMIN AREA</a>.'
                } else {
                    this.isFailed = true;
                    this.isSuccess = false;
                    this.hasError = false;
                    this.username = ''
                    this.password = ''
                    this.message = 'Login failed! Access denied.'
                }
            })
            .catch(error => {
                this.message = error;
                this.hasError = true;
                this.isFailed = false;
                this.isSuccess = false;
                console.log(error);
            });
        }
      },
      computed: {
          messageClass: function () {
            return {
              'alert-success': this.isSuccess,
              'alert-warning': this.hasError,
              'alert-danger': this.isFailed
            }
          }
      },
      template:`<h1>&lt;Login&gt;</h1>
            <form @submit.prevent="postLogin" id="loginform">
                <fieldset v-bind:disabled="isSuccess">
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="row">Username:</div>
                            <div class="row"><input v-model="username" type="text" autocomplete="username"/></div>
                        </div>
                    </div>
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="row">Password:</div>
                            <div class="row"><input v-model="password" type="password" autocomplete="current-password"/>
                            </div>
                        </div>
                    </div>
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="row"><input value="Login" type="submit"/></div>
                        </div>
                    </div>
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="alert"  v-if="message" v-bind:class="messageClass" v-html="message"></div>
                            <div v-if="!isSuccess">Not a member yet? Register <router-link to="/registration-form">here</router-link></div>
                        </div>
                    </div>
                </fieldset>
            </form>`
}