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

    const response = await fetch("http://127.0.0.1:8000/user/", {
        headers: {
            "content-type": "application/json",
        },
        method: "POST",
        body: JSON.stringify(request_body)
    })


}