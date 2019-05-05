$('.set_header input').eq(0).click(function () {
    $('.home-show').removeClass("hide");
    $('.add_inter').removeClass("hide");

})
$('.set_bottom .btn').eq(1).click(function () {
    $('.home-show').addClass("hide");
    $('.add_inter').addClass("hide");
    $("input[name='set_inter']").prop('checked',false)

})
$('.set_bottom .btn').eq(0).click(function () {
    var list=[];
    var id=window.location.href[String(window.location.href).length-1];
    $("input[name='set_inter']").each(function () {
        if($(this).prop('checked')) {
            list.push($(this).parent().attr('inter_id'));
        }
        else {
            return null;
        }
    })
    console.log(list)
    $.ajax({
        type: 'post',
        dataType:'JSON',
        url: '/set/',
        data:{"id":id,"list":String(list)},
        success: function (data) {
            window.alert(data);

        }
    })
})
$('.set_header input').eq(1).click(function () {
     var id=window.location.href[String(window.location.href).length-1];
     $.ajax({
         type: "post",
         url: "/start/",
         data: {id:id},
         success: function (data) {
             window.location.reload();

         }
     })

})