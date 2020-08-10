var button_list = document.getElementsByClassName('update-cart')

for (var i = 0; i < button_list.length ; i++ ){
    button_list[i].addEventListener('click',function(){
    var orderId = this.dataset.order
    var action = this.dataset.action
    update_quantity(orderId,action)
  })
}

function update_quantity(orderId,action){
  var url = '/store/cart/update_quantity/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
      'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'orderId':orderId, 'action':action})
	})
	.then((response) => {
	   return response.json();
	})
	.then((data) => {
    location.reload()
	});
}
