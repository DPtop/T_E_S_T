let sumDishOrder = sessionStorage.getItem('sumDish');

function sumOrder(){
    let buttonSumOrder = document.getElementById('buttonSumOrder');
    sumDishOrder = sumDishOrder.split(', ');
    for (let i = 0; i < sumDishOrder.length; i++){
        let ordImg = sumDishOrder[i].split('..');
        if (ordImg != ''){
            ordImg0 = ordImg[0].toLowerCase();
            ordImg0 = ordImg0.replace(/\s/g, "");
            ordImg1 = ordImg[1];

            // Создаем элементы
            const divElement = document.createElement('div');
            const imgElement = document.createElement('img');
            const pElement = document.createElement('p');

            // Устанавливаем текст для элемента <p>
            pElement.textContent = 'в количестве порций: ' + ordImg1;

            // Устанавливаем атрибуты для элемента <img>
            imgElement.setAttribute('src', '/static/image/'+ordImg0.toLowerCase()+'.jpeg');
//            imgElement.setAttribute('alt', 'Текстовое описание изображения');

            // Добавляем элементы <img> и <p> внутрь элемента <div>
            divElement.appendChild(imgElement);
            divElement.appendChild(pElement);

            // Добавляем текстовое содержимое для элемента <div>
//            divElement.textContent += ' Дополнительный текст';

            // Добавляем элемент <div> в DOM
            document.body.appendChild(divElement);
        }
    };
    sessionStorage.setItem('sumDish', null);
}