export default {
  props: {
    user: Object
  },
  template:`<div>
        Welcome {{ user.lastname }}!
  </div>`
}
