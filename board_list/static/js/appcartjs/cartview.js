"use strict";

$('#cart').submit(function(){return false;});

function getResult(){
    let products=document.getElementsByClassName('product'),
        quantity=0, 
        totalPrice=0;


    for(let i=0; i<products.length; i++){
        if(products[i].querySelector('[class="product-check"]').checked){
            quantity += Number(products[i].querySelector('[class="quantity"]').value);
            totalPrice += Number(products[i].querySelector('[class="price"]').textContent) * Number(products[i].querySelector('[class="quantity"]').value);
        }
        // totalPrice += products[i].querySelector('[class="price"]').textContent; // TODO: доделать, чтобы не было  none в выводе 
    }    
    console.log(totalPrice)
    $('#totalQuantity').text(quantity);
    $('#totalPrice').text(totalPrice);
}

// Проверка значений input
// Если следующее значение при уменьшении меньше или равно 0
// То кнопка "минус" блокируется
let inputs = document.getElementsByClassName('quantity');
for(let i=0; i<inputs.length; i++){
    if(Number(inputs[i].value) - 1 <= 0) {
        inputs[i].previousElementSibling.disabled = true;
    }
}

getResult();


$('.minus').click(function() {
    let input = this.nextElementSibling;
    if(Number(input.value) - 1 <= 0) {
        this.disabled = true;
    }else{
        input.value = Number(input.value) - 1;
    }

    if(Number(input.value) - 1 <= 0) {
        this.disabled = true;
    }
    

    let productData = {};
    productData[input.getAttribute('product-id')] = Number(input.value);

    $.ajax({
        method: 'POST', 
        url: '/change-quantity/',
        data: JSON.stringify(productData), 
        headers: {
            'X-CSRFToken': document.cookie.match(/csrftoken=(.+?)(;|$)/)[1], 
        }, 
        success: function() {
            getResult();
        }
    }) 
});

$('.plus').click(function() {
    let input = this.previousElementSibling;
    
    input.value = Number(input.value) + 1;
    if(Number(input.value) > 1) {
        input.previousElementSibling.disabled = false;
    }
    
    let productData = {};
    productData[input.getAttribute('product-id')] = Number(input.value);

    $.ajax({
        method: 'POST', 
        url: '/change-quantity/',
        data: JSON.stringify(productData), 
        headers: {
            'X-CSRFToken': document.cookie.match(/csrftoken=(.+?)(;|$)/)[1], 
        }, 
        success: function() {
            getResult();
        }
    });
    
});

$('.delete-from-cart').click(function(){
    let productId = String($(this).attr('product-id'));
    let productData = {};
    productData[productId] = 1;
    
    $.ajax({
        data: JSON.stringify(productData), 
        type: 'POST',
        url: '/delete-from-cart/',
        headers: {
            'X-CSRFToken': document.cookie.match(/csrftoken=(.+?)(;|$)/)[1], 
        }, 
        success: function (response) {
            console.log(response)
        }
    });

    location.reload(); // Перезагрузка страницы после удаления товара из корзины
});


$("#allCheck").click(function() {
    let inputs = document.getElementsByClassName('product-check');
    for(let i=0; i<inputs.length; i++) {
        if(this.checked == true) {
            inputs[i].checked = true;
        }else{
            inputs[i].checked = false;
        }
    }
    getResult();
});

$(".product-check").on('click', function() {
    let inputs = document.getElementsByClassName('product-check');
    let checkInput = document.getElementById('allCheck');

    for(let i=0; i<inputs.length; i++) {
        if(inputs[i].checked == false) {
            checkInput.checked = false;
            getResult();
            return 0;
        }
    }
    checkInput.checked = true;
    getResult();
});