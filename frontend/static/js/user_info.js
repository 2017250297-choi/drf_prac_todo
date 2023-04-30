window.onload = () => {
    console.log('loaded')
}

async function edit_info(id) {
    const current_password = document.getElementById("current_password").value
    const request_body = {
        "current_password": current_password,
    }
    const key_ = ["password", "password2", "name", "age", "gender", "introduction"]
    key_.forEach((e) => {
        const e_value = document.getElementById(e).value
        if (e_value != '') {
            request_body[e] = e_value
        }

    });
    console.log(request_body)
    let headerdata = { "content-type": "application/json" }
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }

    const response = await fetch("http://127.0.0.1:8000/user/" + id + '/', {
        headers: headerdata,
        method: "PUT",
        body: JSON.stringify(request_body)
    })
    const response_json = await response.json()
    console.log(response_json)
}


async function load_info() {
    var id = document.getElementById("user_id").value
    let headerdata = {}
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }
    const response = await fetch("http://127.0.0.1:8000/user/" + id + '/', {
        headers: headerdata,
        method: "GET",
        redirect: 'manual'
    })
    const response_json = await response.json()
    let container = document.getElementById("userinfo")
    const key_ = ["email", "name", "age", "gender", "introduction", "last_login"]
    var temp_html = ``
    key_.forEach((e) => {
        const e_value = response_json.user[e]
        if (e_value != undefined) {
            temp_html += `${e}: ${e_value}<br>`
        }
    });
    container.innerHTML = temp_html
    let todo_list = document.getElementById("users_todo")
    todo_list.innerHTML = ``
    const todolists = response_json.users_todolist

    todolists.forEach((element) => {
        var element_ = document.createElement('div')
        element_.innerHTML = `
        <p>${element.title}<br>author: ${element.user}<br>updated: ${element.updated_at}
        <br>complete: ${element.is_complete}
        <br>when: ${element.completion_at}</p>
        <input type="text" id="${element.id}" placeholder="edit title">
        <button onclick="handleTodoPut('${element.id}')">edit</button>
        <button onclick="handleTodoComplete('${element.id}')">toggle complete</button>
        <button onclick="handleTodoDelete('${element.id}')">delete</button>
        `

        todo_list.appendChild(element_)


    });
    var edit_container = document.getElementById('edit')
    edit_container.innerHTML = `<input type="password" name="current_password" placeholder="current_passwrod" id="current_password">
    <input type="password" name="password" id="password" placeholder="password">
    <input type="password" name="password2" id="password2" placeholder="rewrite password">
    <input type="text" name="name" placeholder="name" id="name">
    <input type="number" name="age" placeholder="age" id="age">
    <select name="gender" id="gender">
        <option value="">--select gender--</option>
        <option value="M">Male</option>
        <option value="F">Female</option>
    </select>
    <textarea name="introduction" id="introduction" cols="30" rows="10" placeholder="introduction"></textarea>
    <button onclick="edit_info(${id})">수정</button>`

}