import Thing from './Thing.js'
import Services from './Services.js'
const SERVICE_THINGS = 'SERVICE_THINGS';

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
        Services.getServiceUrl(SERVICE_THINGS)
         .then(service_url => {
            var url = service_url +  '/things';

        axios.get(url, {withCredentials: true})
            .then(response => {
                console.log(response)
                this.things = response.data.things
            })
            .catch(error => {
                console.log(error);
            });
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