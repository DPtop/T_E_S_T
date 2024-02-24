let eatMenu = document.querySelectorAll('.eat_menu');
let price = document.getElementById('price');
let total = document.getElementById('total');
let dishes = document.getElementById('dishes');
let btnModal = document.getElementById('buttonModal');
let totalPrice = 0;
let totalDishes = 0;
let listDishes = {};
let zero_dish = 0;
let show = document.querySelector('#showDishes');
let sumDish = ''

eatMenu.forEach( m_eat => {
    m_eat.addEventListener('mouseover', function() {
        // при наведении на блюдо показать его стоимость
        price.textContent = m_eat.getAttribute('tagPrice');
        // при клике:
        onclick = (event) => {
            if (price.textContent != ''){
                // общая стоимость блюд
                totalPrice += Number(m_eat.getAttribute('tagPrice'));
                total.textContent = totalPrice;
                // количество блюд
                totalDishes += 1;
                dishes.textContent = totalDishes;
                // составление списка блюд (с возможностью подсчёта каждого)
                if (listDishes[m_eat.getAttribute('tagText')]){
                    if (listDishes[m_eat.getAttribute('tagText')].length == 100500) {
                        listDishes[m_eat.getAttribute('tagText')].length = 0;
                    }
                    listDishes[m_eat.getAttribute('tagText')].push(m_eat.getAttribute('tagPrice'));
                }
                else{
                    listDishes[m_eat.getAttribute('tagText')] = [m_eat.getAttribute('tagPrice')];
                }
            }
        };
    });
    // при отводе мыши убрать показ стоимости блюда
    m_eat.addEventListener('mouseout', function() {
        price.textContent = '';
    });
});

// активация всплывающего окна
if (totalPrice == 0){
    btnModal.setAttribute('disabled', 'disabled'); // Делаем кнопку неактивной
    btnModal.setAttribute('pointer-events', 'none'); // Делаем кнопку затемнённой
}
addEventListener('mousemove' || 'keydown', function() {
    if (totalPrice > 0){
        btnModal.removeAttribute('disabled'); // Делаем кнопку активной
    }
});

// всплывающее окно
function closeModal() {
    document.getElementById('myModal').style.display = "none";
}
function openModal() {
    let i = 1;
    let selected_list = '';
    let totalPrice = 0;
    let lastNumber = 0;
    document.getElementById('myModal').style.display = "block";
    let data_list = document.querySelector('#rangeList');
    let option_list = [];

    for (let key in listDishes) {
        let zero_price = 0;
        // если 0:
        if (listDishes[key].length == 100500) {
            zero_dish = 0;
            zero_price = 0;
        } else {
            zero_dish = listDishes[key].length;
            zero_price = listDishes[key][0] * listDishes[key].length;
          }
        // составляем список заказа
        selected_list += i +'.\t"'
                           + key
                           + '" \n\t\t\tпо цене за порцию: ' + listDishes[key][0]
                           + ', \tв количестве порций: ' + zero_dish    //listDishes[key].length
                           + '.\tОбщая стоимость: ' + zero_price    //listDishes[key][0] * listDishes[key].length
                           + '\n'
                           + '--hr--';

        option_list.push(i);
        sumDish += key + '..' + zero_dish + ', '
        i += 1;

        totalPrice += listDishes[key][0] * zero_dish    // * listDishes[key].length;
        show.innerHTML = selected_list.replace(/\n/g, '<br>')

        // делаем <hr> линии
        show.innerHTML = show.innerHTML.replace(/--hr--/g, '<hr>');
        show.innerHTML; // готовый список

        // смена цвета для <hr> при Dark стиле
        let split_Light = document.cookie.split('; ');
        for (let i = 0; i < split_Light.length; i++){
            if (split_Light[i].includes('Light')){
                split_Light = split_Light[i].split('=');
                split_Light = split_Light[1];
            };
        };
        if (split_Light === '0'){
            let elem_hr = document.querySelectorAll('hr');
            elem_hr.forEach(hr => {
                hr.style.borderColor = '#000';
            });
        }
    }
    sumDish += '-->'

    // создаём option для input для каждого выбранного блюда
    try{
        while (data_list.firstChild) {
            data_list.removeChild(data_list.firstChild);
        }
    }catch{}
    option_list.forEach(optn_lst => {
        let new_option = document.createElement('option');
        new_option.value = optn_lst;
        data_list.appendChild(new_option);
    });

    // слогаем слово "копейка"
    if (totalPrice > 0){
        singNumber = Math.round(totalPrice) % 10;
        tensNumber = parseInt((Math.round(totalPrice) % 100 - singNumber) / 10);
        if (singNumber == 1 && [0, 2, 3, 4, 5, 6, 7, 8, 9].includes(tensNumber)){
            show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копейка';
        }
        else if ([2, 3, 4].includes(singNumber) && [0, 2, 3, 4, 5, 6, 7, 8, 9].includes(tensNumber)){
            show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копейки';
        }
        else{
            show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копеек';
        }
    }
    else {
        show.innerHTML += '\nИтого: ' + 'не выбрано';
    }
}

let input_selected = document.getElementById('listSelected');
// убираем порцию
function dishMinus() {
    // узнаём что в input: input_selected.value
    let j = 1;
    for (let key in listDishes) {
        let key_length = listDishes[key].length;
        if (j == input_selected.value) {
            key_length -= 1;
            if (key_length == 100499 || key_length == 0){
                listDishes[key].length = 100500;
            }
            else {
                listDishes[key].length = key_length;
            }
            openModal();
        }
        j += 1;
    }
}

// добавляем порцию
function dishPlus() {
    // узнаём что в input: input_selected.value
    let j = 1;
    for (let key in listDishes) {
        if (j == input_selected.value) {
            if (listDishes[key].length == 100500) {
                listDishes[key].length = 1;
            }
            else {
                listDishes[key].length += 1;
            }
            openModal();
        }
        j += 1;
    }
}

// отмена
function dishCancel() {
    location.reload();
}

// "отправка" заказа
function dishOrder() {
    sumDish = sumDish.split('-->');
    sumDish = sumDish[sumDish.length-2];
    sessionStorage.setItem('sumDish', sumDish);
    dishCancel();
}
