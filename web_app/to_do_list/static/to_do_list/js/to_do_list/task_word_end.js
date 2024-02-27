const count = Number(document.getElementById("count_tasks").textContent)
const text = document.getElementById("correct_word")

var nouns_list = [
    'незавершенная задача',
    'незавершенных задачи',
    'незавершенных задач'
]


function getNoun(number) {
    number = Math.abs(number) % 100;
    var num = number % 10;

    if (number > 10 && number < 20) {
        return 2;
    }
    if (num >= 5 && num < 10){
        return 2;
    }
    if (num > 1 && num < 5) {
        return 1;
    }
    if (num == 1) {
        return 0;
    }
}


text.textContent = nouns_list[getNoun(count)]

