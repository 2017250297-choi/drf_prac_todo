

async function handleSignin() {
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const password2 = document.getElementById("password2").value
    const name = document.getElementById("name").value
    const age = document.getElementById("age").value
    const gender = document.getElementById("gender").value
    const introduction = document.getElementById("introduction").value

    const request_body = {
        "email": email,
        "password": password,
        "password2": password2,
        "name": name,
        "age": parseInt(age),
        "gender": gender,
        "introduction": introduction
    }
    let headerdata = { "content-type": "application/json" }
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }

    const response = await fetch("http://127.0.0.1:8000/user/", {
        headers: headerdata,
        method: "POST",
        body: JSON.stringify(request_body)
    })
    const result = await response.json()
    console.log(result)
}
async function handleUserDel() {
    let headerdata = {}
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }

    const response = await fetch("http://127.0.0.1:8000/user/", {
        headers: headerdata,
        method: "DELETE",
    })
    const result = await response.json()
    console.log(result)
    localStorage.removeItem('payload')
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
}