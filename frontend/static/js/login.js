async function parse_payload(token) {
    const base64Url = token.access.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return jsonPayload
}
async function handlelogin() {
    const email = document.getElementById("email")
    const password = document.getElementById("password")

    const response = await fetch("http://127.0.0.1:8000/user/token/", {
        headers: {
            "content-type": "application/json",
        },
        method: "POST",
        body: JSON.stringify({
            "email": email.value,
            "password": password.value
        })
    })
    const response_json = await response.json()
    const jsonPayload = await parse_payload(response_json)
    localStorage.setItem("payload", jsonPayload);
    localStorage.setItem("refresh", response_json.refresh);
    localStorage.setItem("access", response_json.access);

}


async function refresh() {

    const response = await fetch("http://127.0.0.1:8000/users/refresh/", {

        method: "POST",
        body: JSON.stringify({
            "refresh": localStorage.getItem("refresh")
        })
    })
    const response_json = await response.json()
    console.log(response_json.access)
    const jsonPayload = await parse_payload(response_json)
    console.log(jsonPayload)
    localStorage.setItem("payload", jsonPayload);
    localStorage.setItem("access", response_json.access);
}

async function handlelogout() {

    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    localStorage.removeItem("payload")

}