

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
    const jsonPayload = await parse_payload(response_json.access)
    localStorage.setItem("payload", jsonPayload);
    localStorage.setItem("refresh", response_json.refresh);
    localStorage.setItem("access", response_json.access);

}


async function handlelogout() {

    localStorage.removeItem("access")
    localStorage.removeItem("refresh")
    localStorage.removeItem("payload")

}