function searchApi(){
     var items = document.getElementById('items')
items.innerHTML = `searching...`
                var words = document.getElementById("searchitem").value
                if (words === "" || words === " "){
                alert("please enter item")
                }else{
            var url = window.location.origin +"/search/";



            const data = {q:words}
            const http = new XMLHttpRequest();
                http.open('POST', url);
                http.setRequestHeader('Content-type', 'application/json');
                // http.setRequestHeader('Authentication','id_token');
                http.send(JSON.stringify(data)); // Make sure to stringify
                http.onload = function() {
                state = true;
                var resp = http.responseText;
                var json_resp = JSON.parse(resp);
                // You can now use the response for what you want
                if(json_resp['success']){
                    // look for id of element that will hold the results and append to it
                    // objects received from calling api

                    if (json_resp['objects'].length > 0){
                    items.innerHTML = ""
                    for (var i=0;i<json_resp['objects'].length;i++){
                        var obj = json_resp['objects'][i]
                    items.innerHTML += `<div class="col-lg-4 col-md-12 mb-4">
<div class="card card-ecommerce" style="width:19rem; height:420px">
    <div class="view overlay">
        <img src="image" height="300px" width="350px" class="img-fluid">
        <a href="`+obj['url']+`">
            <div class="mask rgba-white-slight"></div>
        </a>
    </div>
    <div class="card-body">

        <h5 class="card-title mb-1"><strong><a href="url" class="dark-grey-text">`+obj['title']+`</a></strong>
        </h5>
        <span class="badge badge-pill mb-2">New</span>
        <!-- Rating -->
        <ul class="rating">
            <li><i class="fas fa-star blue-text"></i></li>
            <li><i class="fas fa-star blue-text"></i></li>
            <li><i class="fas fa-star blue-text"></i></li>
            <li><i class="fas fa-star blue-text"></i></li>
            <li><i class="fas fa-star blue-text"></i></li>
        </ul>
        <div class="card-footer pb-0">
            <div class="row mb-0">
                    <span class="float-left"><strong>GHC `+obj['price']+`</strong></span>
                <span class="float-right">
                        <a class="" data-toggle="tooltip" data-placement="top"
                           title="Add to Cart"><i class="fas fa-shopping-cart ml-3"></i></a>
                        </span>
            </div>
        </div>

    </div>
</div>
</div>v`
                    }
                    }else{
                    items.innerHTML = "No items founds"
                    }

                }

                console.log(json_resp)
                }
                }
            }