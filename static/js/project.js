$('.button[value="确定"]').click(function () {
    $.ajax({
        type: "post",
        url:  "/project/",
        dataType:"json",
        data: $('#project-add').serialize(),
        success: function (data) {
            var ecode=data['ecode']
            if (ecode==0){
                window.location.href='/project/'

            }
            else{
                window.location.reload()
            }

        }

    })

})
$('.button[value="取消"]').click(function () {
    $(".home-show").addClass('hide');
    $(".home-modal").addClass("hide")

})

$(".project-new").click(function () {
    $(".form-title").text('新增项目');
    $(".home-show").removeClass('hide');
    $(".home-modal").removeClass("hide");

})
$("#project-q").click(function () {
    var keyword=$('.project-header input[name="query_project"]')[0].value;
    if (keyword){
        if(keyword==='#'){
            window.location.href='/project/';
        }
        else {
            window.location.href='?projectname='+keyword;
        }
    }
    else {
        window.location.href='/project/';
    }

})


$('.table-button').click(function () {
    $.ajax({
        type: 'put',
        url: '/project/',
        dataType: 'JSON',
        data: {
                'p-id': $(this).parent().parent().attr('project-id'),
                'project_type':$(this).parent().attr('p-id'),
        },
        success:function(data){
            if (data){window.location.reload();}
            else{
                window.location.reload();
            }


        }
    })

})
$('.table-delete').click(function () {
    $.ajax({
        type: "delete",
        url: "/project/",
        dataType: "JSON",
        data:{
            "id": $(this).parent().parent().attr("project-id")
        },
        success:function (data) {
            if (data){
                window.location.reload();
            }
            else {
                window.location.reload();
            }

        }
    })

})
$('.table-edit').click(function () {
    $(".home-show").removeClass('hide');
    $(".home-modal").removeClass("hide");
    $(".form-title").text('编辑项目');
    $("input[name='projectname']").val($(this).parent().parent().children().eq(1).text());
    $("input[name='projectver']").val($(this).parent().parent().children().eq(2).text());
    $("input[name='projecturl']").val($(this).parent().parent().children().eq(3).text());
    $("textarea[name='projectremark']").val($(this).parent().parent().children().eq(4).text());
    $("select[name='projecttype']").val($(this).parent().attr('p-id'));
    $("input[name='project-id']").val($(this).parent().parent().attr('project-id'))


})