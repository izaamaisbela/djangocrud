async function deletar(id){

    var csrf = document.querySelector("[name=csrfmiddlewaretoken]").value

    const resposta = await apiFetch (`/api/user/${id}`, 'DELETE', null, {'X-CSRFToken': csrf})

    if (resposta.status == 200){
        var linhaUsuario = document.getElementById(`usuarios-${id}`)
        linhaUsuario.remove()
    }
}