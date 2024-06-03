data = JSON.stringify({
    headline: "Testing",
    tag: "Testing",
    background_image: "Testing",
    content: "Testing",
    user: 1
})

let csrftoken = getCookie('csrftoken');
let response = fetch("http://127.0.0.1:8000/json/", {
    method: 'POST',
    body: data,
    headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        "X-CSRFToken": csrftoken
    },
})


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}