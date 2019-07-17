$(document).ready(function(){
    const switchers = [...document.querySelectorAll('.switcher')]

    switchers.forEach(item => {
        item.addEventListener('click', function() {
            switchers.forEach(item => item.parentElement.classList.remove('is-active'))
            this.parentElement.classList.add('is-active')
        })
    })

    $("#loginButtonMenu").click(function(){
        $("#loginForms").show();
    })

    $("#signupButtonMenu").click(function(){
        $("#loginForms").show();
    })

})

function readCSRF(element){
    return $(element).find("[name='csrfmiddlewaretoken']").val();
}
