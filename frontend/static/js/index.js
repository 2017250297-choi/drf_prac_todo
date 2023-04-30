window.onload = () => {
    console.log("LOADED!")
    get_todolist()

}
async function get_todolist() {
    const response = await fetch("http://127.0.0.1:8000/todolist", {
    })
    const todolists = await response.json()
    var container = document.getElementById("list")
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
        container.appendChild(element_)


    });

}
async function handleTodoPut(id) {
    const title = document.getElementById(id).value
    const request_body = {
        "title": title,
    }
    let headerdata = { "content-type": "application/json" }
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }
    console.log(headerdata)
    const response = await fetch("http://127.0.0.1:8000/todolist/" + id + "/", {
        headers: headerdata,
        method: "PUT",
        body: JSON.stringify(request_body)
    })
    respose_json = await response.json()
    location.href = ""
}
async function handleTodoComplete(id) {
    let headerdata = {}
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }
    const response = await fetch("http://127.0.0.1:8000/todolist/complete/" + id + "/", {
        headers: headerdata,
        method: "PUT",
    })
    location.href = ""
}
async function handleTodoDelete(id) {
    let headerdata = {}
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }
    const response = await fetch("http://127.0.0.1:8000/todolist/" + id + "/", {
        headers: headerdata,
        method: "DELETE",
    })
    location.href = ""
}
async function handleTodo() {
    const title = document.getElementById("title").value

    const request_body = {
        "title": title,
    }
    let headerdata = { "content-type": "application/json" }
    const access_token = await get_access_token()
    if (access_token != null) {
        headerdata['authorization'] = access_token
    }
    console.log(headerdata)
    const response = await fetch("http://127.0.0.1:8000/todolist/", {
        headers: headerdata,
        method: "POST",
        body: JSON.stringify(request_body)
    })
    respose_json = await response.json()
    console.log(respose_json)
}