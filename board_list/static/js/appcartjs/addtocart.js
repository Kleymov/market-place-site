class Cart {
    constructor(product_data) {
        this.product_data = product_data;
    }
    show() {
        console.log(this.product_data);
    }
}


window.onload = function() {
    $('#toCart').click(function(event){
        event.preventDefault();
        
        let productId = String($(this).attr('product-id'));
        let productData = {};
        productData[productId] = 1;
        
        $.ajax({
            data: JSON.stringify(productData), 
            type: 'POST',
            url: '/add-to-cart/',
            headers: {
                'X-CSRFToken': document.cookie.match(/csrftoken=(.+?)(;|$)/)[1], 
            }, 
            success: function (response) {
                $('#addToCart').css('display', 'none');
                $('#goToCart').css('display', 'block');
            }
        });
    });
}