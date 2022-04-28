export default {
    data(){
        return {
            message: '',
            firstname: '',
            lastname: '',
            username: '',
            password: '',
            hasError: false,
            isSuccess: false,
            isFailed: false
        }
    },
    methods: {
        postRegistration: function(event) {
            axios.post('/register', {
                firstname: this.firstname,
                lastname: this.lastname,
                username: this.username,
                password: this.password
            })
            .then(response => {
                if (response.data.registration_success) {
                    this.isSuccess = true;
                    this.isFailed = false;
                    this.hasError = false;
                    this.firstname = '*******'
                    this.lastname = '*******'
                    this.username = '*******'
                    this.password = '***********'
                    this.message = 'Registration success! Please, <a href="/login">log in</a>.'
                } else {
                    this.isFailed = true;
                    this.isSuccess = false;
                    this.hasError = false;
                    this.password = ''
                    this.message = 'Registration failed! ' + response.data.error_msg
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
      template:`<h1>&lt;Register&gt;</h1>
            <form @submit.prevent="postRegistration" id="registrationform">
                <fieldset v-bind:disabled="isSuccess">
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="row">First name:</div>
                            <div class="row"><input v-model="firstname" type="text" autocomplete="firstname"/></div>
                        </div>
                    </div>
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="row">Last name:</div>
                            <div class="row"><input v-model="lastname" type="text" autocomplete="lastname"/></div>
                        </div>
                    </div>
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
                            <div class="row"><input value="Register" type="submit"/></div>
                        </div>
                    </div>
                    <div class="row justify-content-evenly">
                        <div class="col-sm-4">
                            <div class="alert" v-if="message" v-bind:class="messageClass" v-html="message"></div>
                            <div v-if="!isSuccess">Already a member? Please <router-link to="/">log in</router-link></div>
                        </div>
                    </div>
                </fieldset>
            </form>`
}