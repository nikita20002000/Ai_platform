const hello_text = document.getElementById('hello_text')
var date = new Date();

hello_list = [
    'Доброе утро,',
    'Добрый день,',
    'Добрый вечер,',
    'Доброй ночи,'
];

function make_hello(date) {
    var time = (date.getHours());

    if ( time > 5 && time < 12) {
        return 0
    };
    if (time >= 12 && time < 17) {
        return 1;
    };
    if (time >= 5 && time < 24) {
        return 2;
    } else {
        return 3
    }
}

hello_text.textContent = hello_list[make_hello(date)]
