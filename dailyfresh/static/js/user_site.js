$(function () {
    var error_phone = false;

    $('#phone').blur(function () {
        check_phone();
        
    });

    function check_phone() {
        var len = $('#phone').val().length;
        console.log("你执行了吗");
        var re = /^\d+$/;
        if(len == 11 && re.test($('#phone').val())) {
            console.log("正常的手机号");
            $('#phone').next().hide();
            error_phone = false;
        }
        else {
            console.log("错误的手机号");
            alert('你的手机格式不正确,只能是11位数字');

            error_phone = true;
        }

    }
    $('#form').submit(function () {
        check_phone();
        if(error_phone == false){
            return true
        }
        else {
            return false;
        }


    });


})