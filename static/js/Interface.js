$(".Interface-new").click(function(){
    $(".home-show").removeClass("hide");
    $(".Interface-modal").removeClass("hide");
     $(".interface-title").text("新增用例");


})
$(".interface-b ").click(function(){
    $(".home-show").addClass("hide");
    $(".Interface-modal").addClass("hide");
    $("#Interface")[0].reset();
})
$(".interface-a").click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/Interface/",
        data: $("#Interface").serialize(),
        success: function (data) {
            var ecode=data["ecode"];
            var message=data["message"];

            if (ecode===1){
                    $(".interface-alert").removeClass("hide");
                    $(".interface-alert").text(message);
                    setTimeout(function () {
                       $(".interface-alert").addClass("hide");

                    },2000)
            }
            else{
                window.location.href="/Interface/";
            }
        }

    })

})
$(".interface-edit").click(function () {
    $(".home-show").removeClass("hide");
    $(".Interface-modal").removeClass("hide");
    $(".interface-title").text("编辑用例");
    var interface_id=$(this).parent().parent().attr("Interface-id")
    $.ajax({
        type: "put",
        url:"/Interface/",
        dataType: "json",
        data: {
            "interface_id":interface_id
        },
        success:function (data) {
            var result=data["interface_result"];
            var remark=data["interface_remark"];
            var name=data["interface_name"];
            var API_id=data["API_id"];
            $("input[name='Interface_name']").val(name);
            $("textarea[name='Interface_remark']").val(remark);
            $("textarea[name='Interface_result']").val(result);
            $(".select-common").val(API_id);
            $("input[name='interface_id']").val(interface_id);


            }


    })

})
$(".interface-delete").click(function () {
    $.ajax({
        type: "delete",
        dataType:"json",
        url:"/Interface/",
        data:{
            "Interface_id":$(this).parent().parent().attr("Interface-id")
},
        success:function (data) {
            var ecode=data["ecode"];
            if (ecode===0){
                alert("删除成功")
            }
            else {
                alert("删除失败")
            }
        }
    })
})