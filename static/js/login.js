$('#login').click(function () {
    var pwd=$.md5($('#login-form')[0].password.value);
    $.ajax({
        type: 'post',
        url: '/login/',
        data:{
            username: $('#login-form')[0].username.value,
            password: pwd
        },
        success: function (data) {
            var ecode_message=JSON.parse(data);
            var ecode=ecode_message['ecode']
            if (ecode==0){
                window.location.href='/project/'
            }
            else {
               $(".login-alert").removeClass("hide");
                $(".login-alert").text(ecode_message['message'])
                setTimeout(function(){
                    $(".login-alert").addClass("hide");
                },3000)
            }

        }
    })

})