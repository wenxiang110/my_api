$(".set_add").click(function () {
    $(".home-show").removeClass("hide");
    $(".interface-modal").removeClass("hide");
    $(".form-header h4").text("新增集合")
})
$(".form-foot .btn").eq(1).click(function () {
    $(".home-show").addClass("hide");
    $(".interface-modal").addClass("hide");
    $("#set_form")[0].reset();
})
$(".form-foot .btn").eq(0).click(function () {
    $.ajax({
        type: "post",
        url: "/Interface_set/",
        dataType: "JSON",
        data: $('#set_form').serialize(),
        success: function (data) {
            window.location.href="/Interface_set/"

        }
    })
})
$(".edit-icon").click(function () {
    $(".home-show").removeClass("hide");
    $(".interface-modal").removeClass("hide");
    $(".form-header h4").text("编辑集合")
    var reslut_id=$(this).parent().attr("reslut_id")
    $.ajax({
        type: "put",
        dataType: "json",
        url: "/Interface_set/",
        data: {
            id:reslut_id,
        },
        success: function (data) {
            var name=data["name"];
            var mark=data["mark"];
            $("input[name='set_name']").val(name);
            $("input[name='set_mark']").val(mark);
            $("input[name='set_id']").val(reslut_id);

        }
    })
})
$(".delete-icon").click(function (data) {

    $.ajax({
        type: "delete",
        dataType: "json",
        url: "/Interface_set/",
        data:{
            id:$(this).parent().attr("reslut_id"),

        },
        success: function (data) {
            window.location.reload()

        }
    })

})
$(".set_all").click(function () {
            $("input[name='set_inter']").each(function () {
                if($(this).prop('checked')){
                    $(this).prop('checked',false);
                }
                else {
                    $(this).prop('checked',true)
                }

            })

})