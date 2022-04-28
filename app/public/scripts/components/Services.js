export default {
    getServiceUrl(service) {
        var url;
        axios.get('/services/' + service)
            .then(response => {
                url = response.data.service_url;
            })
            .catch(error => {
                console.log(error);
            });
        return url;
    }
}
