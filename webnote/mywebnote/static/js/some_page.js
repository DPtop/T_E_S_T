let eatMenu = document.querySelectorAll('.eat_menu');
let price = document.getElementById('price');
let total = document.getElementById('total');
let dishes = document.getElementById('dishes');
let btnModal = document.getElementById('buttonModal');
let totalPrice = 0;
let totalDishes = 0;
let listDishes = {};

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
                //
                // составление списка блюд (с возможностью подсчёта каждого)
                if (listDishes[m_eat.getAttribute('tagText')]){
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

// активность всплывающего окна
if (totalPrice == 0){
    btnModal.setAttribute('disabled', 'disabled'); // Делаем кнопку неактивной
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
    let show = document.querySelector('#showDishes');
    let i = 1;
    let selected = '';
    let totalPrice = 0;
    let lastNumber = 0;
    document.getElementById('myModal').style.display = "block";
    for (let key in listDishes) {
        selected += i +'.\t"'
                      + key
                      + '" \n\t\t\tпо цене за порцию: ' + listDishes[key][0]
                      + ', \tв количестве порций: ' + listDishes[key].length
                      + '.\tОбщая стоимость: ' + listDishes[key][0] * listDishes[key].length
                      + '\n'
                      + '--hr--';
        i += 1;
        totalPrice += listDishes[key][0] * listDishes[key].length;
        show.innerHTML = selected.replace(/\n/g, '<br>')

        // делаем <hr> линии
        show.innerHTML = show.innerHTML.replace(/--hr--/g, '<hr>');
        show.innerHTML;

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

    // слогаем слово "копейка"
    lastNumber = Math.round(totalPrice) % 10;
    if (lastNumber == 1){
        show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копейка';
    }
    else if ([2, 3, 4].includes(lastNumber)){
        show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копейки';
    }
    else{
        show.innerHTML += '\nИтого: ' + Math.round(totalPrice) + ' копеек';
    }
}