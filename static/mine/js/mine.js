$(function () {
    $('.mine').width(innerWidth)
    var c_value = $.cookie('token')
    if (c_value){
        $('.quit').show()
    }else {
        $('.quit').hide()
    }

})