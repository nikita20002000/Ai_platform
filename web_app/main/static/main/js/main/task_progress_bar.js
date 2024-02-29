const bar = document.getElementById('progress-bar')
const value = document.getElementById('progress-val')


var task_list = bar.textContent.split(' ')
var remain = task_list[0]
var all = task_list[1]

var percent = (remain / all) * 100

bar.style.cssText += `width: ${percent}%;`;
value.textContent = `${percent}%`