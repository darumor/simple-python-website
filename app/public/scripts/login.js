import LoginForm from './components/LoginForm.js'
import RegistrationForm from './components/RegistrationForm.js'

const routes = [
  { path: '/', component: LoginForm },
  { path: '/registration-form', component: RegistrationForm },
];

const router = VueRouter.createRouter({
  history: VueRouter.createWebHashHistory(),
  routes,
});

var login_app = Vue.createApp();
login_app.use(router)
login_app.mount('#login-app')
