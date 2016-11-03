
var log = function () {
    console.log(arguments)
};
alert('input password');
$(document).ready(function(){
    //给按钮绑定 click 事件
    $('#id-button-add-blog').on('click', function(){
        var blog = $('#id-input-blog').val();
        var form = {
            blog: blog
        };
        var requrest = {
            url: '/add',
            type: 'post',
            data: form,
            success: function () {
                log('success', arguments)
            },
            error: function () {
                log('error', arguments)
            }
        };
        $.ajax(requrest)
    })
});
