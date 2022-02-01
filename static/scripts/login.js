var login_app = new Vue({
      el: '#login-app',
      data: {
        message: '',
        username: '',
        password: '',
        hasError: false,
        isSuccess: false,
        isFailed: false
      },
      methods: {
        postLogin: function(event) {
            axios.post('/login', {
                username: this.username,
                password: this.password
            })
            .then(response => {
                if (response.data.login_success) {
                    this.isSuccess = true;
                    this.isFailed = false;
                    this.hasError = false;
                    this.message = '<p>Login success!</p><p>Please proceed to the <a href="/restricted">RESTRICTED AREA</a>.</p>'
                } else {
                    this.isFailed = true;
                    this.isSuccess = false;
                    this.hasError = false;
                    this.message = '<p>Login failed! Access denied.</p>'
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
      }
    });

