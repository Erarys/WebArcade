const RANDOM_QUOTE_API_URL = 'https://api.quotable.io/random'
const quoteDisplayElement = document.getElementById('quoteDisplay')
const quoteInputElement = document.getElementById('quoteInput')
const timerElement = document.getElementById('timer')
const workElement = document.getElementById('work')


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

quoteInputElement.addEventListener('input', () => {
    const arrayQuote = quoteDisplayElement.querySelectorAll('span')
    const arrayValue = quoteInputElement.value.split('')

    let correct = true
    arrayQuote.forEach((characterSpan, index) => {
        const character = arrayValue[index]
        if (character == null) {
            characterSpan.classList.remove('correct')
            characterSpan.classList.remove('incorrect')
            correct = false
        } else if (character === characterSpan.innerText) {
            characterSpan.classList.add('correct')
            characterSpan.classList.remove('incorrect')
        } else {
            characterSpan.classList.remove('correct')
            characterSpan.classList.add('incorrect')
            correct = false
        }
    })
    if (correct) {
        let speed = (text.length * 60) / parseInt(timer.textContent)
        workElement.innerText = "Ваша скорость " + speed + " " + text.length + " " + timer.textContent
        const data = {
            "speed": speed,
        }
        querySomething()
    }
})

function querySomething(){
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/keyboard/",
        headers: {
            "Content-Type": "application/json",
            "HTTP_GROUP_NAME": "groups_name",
        },
        data: {
            "check_this": $('#this_field').val(),
            "csrfmiddlewaretoken": getCookie("csrftoken"),
        },
        success: function(data){
            console.log("success");
            console.log(data);
        },
        failure: function(data){
            console.log("failure");
            console.log(data);
        },
    });
    alert('marcusShep function ran.')
}

function getRandomQuote() {
    return fetch(RANDOM_QUOTE_API_URL)
        .then(response => response.json())
        .then(data => data.content)
}

let text;

async function getNextQuote() {
    const quote = await getRandomQuote()
    text = quote
    quoteDisplayElement.innerHTML = ''
    quote.split('').forEach(character => {
        const characterSpan = document.createElement('span')
        // characterSpan.classList.add('correct')
        characterSpan.innerText = character
        quoteDisplayElement.appendChild(characterSpan)
    })
    quoteInputElement.value = null

    startTimer()
}

let startTime, timeFinish

function startTimer() {
    timerElement.innerText = 0;
    startTime = new Date()
    setInterval(() => {
        timer.innerText = getTimerTime()
    }, 1000)
}

function getTimerTime() {
    return Math.floor((new Date() - startTime) / 1000)
}

getNextQuote()
