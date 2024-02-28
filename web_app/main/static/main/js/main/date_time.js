var timeNode = document.getElementById('time-node');
var dateNode = document.getElementById('date-node');

function getCurrentTimeString() {
    return new Date().toTimeString().replace(/ .*/, '');
}

setInterval(
    () => timeNode.innerHTML = getCurrentTimeString(),
                  1000
);


function getCurrentDateString() {
    return new Date().toDateString();
}

setInterval(
    () => dateNode.innerHTML = getCurrentDateString(),
                  1000
);