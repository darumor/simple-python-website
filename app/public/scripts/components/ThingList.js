import Thing from './Thing.js'

export default {
     components: {
        Thing
      },
      data() {
          return  {
            things: []
          }
      },
      mounted () {
        axios.get('/things')
            .then(response => {
                console.log(response)
                this.things = response.data.things
            })
            .catch(error => {
                console.log(error);
            });
      },
      template:`<div class="row justify-content-evenly">
                    <div class="col-sm-1">
                    </div>
                    <div class="col-sm-3">
                        <h2>All things</h2>
                    </div>
                    <div class="col-sm-4">
                        <Thing v-for="thing in things" :thing="thing"></Thing>
                    </div>
                    <div class="col-sm-4">
                    </div>
                </div>
                `
}