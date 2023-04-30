async function parse_payload(token) {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(atob(base64).split('').map(function (c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));
    return jsonPayload
}

async function refresh() {
    const refresh_token = localStorage.getItem("refresh")
    if (refresh_token == null) {
        return null
    }
    console.log(JSON.stringify({
        "refresh": refresh_token
    }))
    const response = await fetch("http://127.0.0.1:8000/user/refresh/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            "refresh": refresh_token
        })
    })
    if (response.status == 401) {
        return null
    }
    const response_json = await response.json()
    console.log(response_json)
    const jsonPayload = await parse_payload(response_json.access)
    localStorage.setItem("payload", jsonPayload);
    localStorage.setItem("access", response_json.access);
    return "Bearer " + localStorage.getItem("access")
}
async function get_access_token() {
    const token = localStorage.getItem('access')
    if (token == null) {

        return null
    }
    else {
        const bearer = "Bearer " + token
        const response = await fetch("http://127.0.0.1:8000/user/token/verify/", {
            method: "GET",
            headers: { "authorization": bearer }
        })
        if (response.status == 200) {
            return 'Bearer ' + token
        }
        else {
            return await refresh()
        }


    }
}