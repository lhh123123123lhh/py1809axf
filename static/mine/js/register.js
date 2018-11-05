$(function () {
    $('.register').width(innerWidth)

    // 账号验证
    $('#account input').blur(function () {
        if ($(this).val() == '') return

        var reg = /^(\w){8,12}$/
        var flag = reg.test($(this).val())
        console.log(flag)
        if (flag) {
            $.get('/checkaccount/', {'account': $(this).val()}, function (data) {
                if (data['status'] == 1) {

                    $('#account b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                } else {
                    console.log(data)
                    $('#account b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                }
            })
        } else {
            $('#account b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    // 密码验证
    $('#password input').blur(function () {
        if ($(this).val() == '') return
        var pattern = /^(\w){6,12}$/
        var flag = pattern.test($(this).val())
        if (flag) {
            $('#password b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#password b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    // 密码确认
    $('#password1 input').blur(function () {
        if ($(this).val() == '') return

        if ($(this).val() == $('#password input').val()) {
            $('#password1 b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#password1 b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    // 用户名验证
    $('#user input').blur(function () {
        if ($(this).val() != '') {
            $('#user b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#user b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    // 手机号验证
    $('#tel input').blur(function () {
        if ($(this).val() == '') return
        var pattern = /^1(3|4|5|7|8)\d{9}$/
        var flag = pattern.test($(this).val())
        if (flag) {
            $('#tel b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#tel b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
    // 地址验证
    $('#address input').blur(function () {
        if ($(this).val() != '') {
            $('#address b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {
            $('#address b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })
})