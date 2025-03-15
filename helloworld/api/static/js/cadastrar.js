async function enviarFormulario(evento){

    evento.preventDefault()

    var nome = document.getElementById("nome").value
    var senha = document.getElementById("senha").value
    var csrf = document.querySelector("[name=csrfmiddlewaretoken]").value
    
    const url = window.location.pathname
    const valor = url.split('/')
    const id = valor[valor.length - 1]
    let resposta;

    if(id){

      resposta = await apiFetch(`/api/user/${id}`, 'PUT', {username: nome, password: senha}, {'X-CSRFToken': csrf})

    }else{

      resposta = await apiFetch('/api/user', 'POST', {nome: nome, senha: senha}, {'X-CSRFToken': csrf})

    }
    
    if(resposta){
      window.location.href = '/home'
    }
      
}

document.getElementById("usuarioForm").addEventListener("submit", enviarFormulario) 