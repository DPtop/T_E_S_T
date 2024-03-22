let sumDishOrder = sessionStorage.getItem('sumDish');
let priceDishOrder = sessionStorage.getItem('totalPrice');

console.log('priceDishOrder', priceDishOrder);

function sumOrder(){
    // Отображаем кнопку buttonClearOrder
    let btnClear = document.getElementById('buttonClearOrder');
    btnClear.style.visibility = 'visible';

    // Создаем элемент <div> с id 'orderDIV'
    let divElement = document.getElementById('orderDIV');


    if (sumDishOrder == null) {
        // Создаем элемент <img> и задаем ему атрибуты
        let imgElement = document.createElement('img');
        imgElement.src = '/static/image/null.jpeg';

        // Добавляем созданные элементы внутрь элемента <div>
        divElement.appendChild(imgElement);
        divElement.appendChild(paragraphElement);

        // Добавляем элемент <div> на страницу
        document.body.appendChild(divElement);
    }
    else {
        let buttonSumOrder = document.getElementById('buttonSumOrder');
        sumDishOrder = sumDishOrder.split(', ');

        for (let i = 0; i < sumDishOrder.length; i++){
            let ordImg = sumDishOrder[i].split('..');
            if (ordImg != ''){
                ordImg0 = ordImg[0].toLowerCase();
                ordImg0 = ordImg0.replace(/\s/g, "");
                ordImg1 = ordImg[1];

                // Создаем элемент <p> с текстом "1234"
                let paragraphElement = document.createElement('p');
                paragraphElement.textContent = 'в количестве порций: ' + ordImg1;

                // Создаем элемент <img> и задаем ему атрибуты
                let imgElement = document.createElement('img');
                imgElement.src = '/static/image/'+ordImg0.toLowerCase()+'.jpeg';

                // Добавляем созданные элементы внутрь элемента <div>
                divElement.appendChild(imgElement);
                divElement.appendChild(paragraphElement);

                // Добавляем элемент <div> на страницу
                document.body.appendChild(divElement);
            }
        };
        // Создаем элемент с общеё ценой заказа
        let priceElement = document.createElement('p');
        priceElement.textContent = 'на сумму: ' + priceDishOrder;
        divElement.appendChild(priceElement);
        document.body.appendChild(divElement);
    }
}

function dishClear(){
    // Очистить sumDish
    sessionStorage.setItem('sumDish', null);
    sessionStorage.setItem('totalPrice', null);
    location.reload();
}