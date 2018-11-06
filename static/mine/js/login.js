$(function () {
    $('.login').width(innerWidth)

    $('#subButton').on('click', function () {
        console.log('登录')

        temp1 = checkingAccount()
        temp2 = checkingPassword()
        if (temp1 && temp2) {
            $('.login form').submit()
        }
    })

    function checkingAccount() {
        // 数字、字母
        var reg = /^(\w){8,12}$/
        var accountInput = $('#account input')
        if (reg.test(accountInput.val())) {  // 符合
            $('#account i').html('')
            $('#account b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            return true
        } else {    // 不符合
            $('#account i').html('账号格式错误').addClass('err')
            $('#account b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return false
        }
    }

    function checkingPassword() {
        // 数字
        var reg = /^(\w){6,12}$/
        var passwordInput = $('#password input')
        if (reg.test(passwordInput.val())) {  // 符合
            $('#password i').html('')
            $('#password b').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            return true
        } else {    // 不符合
            $('#password i').html('密码格式错误').addClass('err')
            $('#password b').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return false
        }
    }
})
