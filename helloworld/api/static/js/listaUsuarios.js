async function deletar(id){
    const resposta = await fetch (`/api/usuarios/${id}`, {
        method: 'DELETE'
    })

    if (resposta.ok){
        var linhaUsuario = document.getElementById(`usuarios-${id}`)
        linhaUsuario.remove()
    }
}