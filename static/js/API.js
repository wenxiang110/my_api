$(".API-new").click(function () {
    $(".home-show").removeClass("hide");
    $(".API-modal").removeClass("hide");
    $(".API-add-title").text("新增接口");


})
$(".api-button").eq(1).click(function () {
    $(".home-show").addClass("hide");
    $(".API-modal").addClass("hide");
    $("#API-add")[0].reset();

})
$(".api-button").eq(0).click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        URL: "/API/",
        data:$("#API-add").serialize(),
        success: function (data) {
            var ecode=data["ecode"]
            var message=data["message"]
            console.log(data['ecode'])
            if (ecode==0){
                $('.API-alert').removeClass('hide');
                $('.API-alert').text(message);
                setTimeout(function(){
                    $('.API-alert').addClass('hide');
                    window.location.reload();
                },3000)

            }
            else {
                $('.API-alert').removeClass('hide');
                $('.API-alert').text(message);
                setTimeout(function(){
                    $('.API-alert').addClass('hide');
                },3000)
            }

        }
    })

})
$('.API-edit').click(function(){
    $(".home-show").removeClass("hide");
    $(".API-modal").removeClass("hide");
    $(".API-add-title").text("编辑接口")
    $("select[name='project_name']").val($(this).parent().parent().children().eq(1).attr("project-id"));
    $("input[name='API_name']").val($(this).parent().parent().children().eq(2).text());
    $("input[name='API_url']").val($(this).parent().parent().children().eq(3).text());
    $("textarea[name='API_remark']").val($(this).parent().parent().children().eq(5).text());
    $("select[name='API_way']").val($(this).parent().attr('type-id'));
    $("textarea[name='API_para']").val($(this).parent().parent().children().eq(4).text());
    $("input[name='API-id']").val($(this).parent().parent().attr('API-id'));
})
$('.API-delete').click(function () {
    $.ajax({
        type: "delete",
        dataType: "json",
        url:"/API/",
        data:
            {
                "API_id":$(this).parent().parent().attr('API-id')
            },
        success:function (data) {
           window.location.reload()

        }
    })

})
$('.API_do').click(function(){
    $(".home-show").removeClass("hide");
    $(".API-para").removeClass("hide");
    var Interface_id=$(this).parent().parent().attr('Interface-id');
    $(".btn-default").click(function () {
        var API_token=$("input[name='API-token']").val();
        $.ajax({
            type:"POST",
            dataType:"json",
            url:"/report/",
            data:{
                "Interface_id":Interface_id,
                "API_token":API_token
            },
            success:function (data) {
                var data=JSON.stringify(data)
                $("textarea[name='test_result']").val(data);
            }

        })

    })
})
$('.btn-primary').click(function () {
    $(".home-show").addClass("hide");
    $(".API-para").addClass("hide");
    $("input[name='API-token']").val("");
})
