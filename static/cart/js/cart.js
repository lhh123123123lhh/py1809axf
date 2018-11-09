$(function () {
    $('.cart').width(innerWidth)
    total()

    // 每个按钮单独点击
    $('.confirm-wrapper').click(function () {
        var cartid = $(this).attr('cartid')
        var $that = $(this)
        console.log(cartid)
        $.get('/select/', {'cartid': cartid}, function (response) {
            console.log(response)
            if (response.status == 1) {
                var isselect = response.isselect
                $that.attr('isselect', isselect)
                if (isselect) {
                    $that.find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {
                    $that.find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                }
            }
            total()
        })
    })


    // 全选/取消全选
    $('.bill .all span').click(function () {
        var isselect = $(this).attr('isselect')
        isselect = (isselect == 'false') ? true : false
        $(this).attr('isselect', isselect)
        if (isselect) {
            $(this).removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $(this).removeClass('glyphicon glyphicon-ok').addClass('no')
        }


        $.get('/changeall/', {'isselect': isselect}, function (response) {
            console.log(response)
            if (response.status == 1) {
                // 遍历
                $('.confirm-wrapper').each(function () {
                    $(this).attr('isselect', isselect)
                    if (isselect) {
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                })
            }
            total()
        })
    })

    // 定义方法
    function total() {
        var sum = 0

        // 遍历操作
        $('.goods').each(function () {
            var $confirm = $(this).find('.confirm-wrapper')
            var $content = $(this).find('.content-wrapper')

            if ($confirm.find('.glyphicon-ok').length) {
                var price = $content.find('.price').attr('price')
                var num = $content.find('.num').attr('number')
                sum += price * num
            }
        })

        // 显示
        $('.bill .total b').html(parseInt(sum))
    }

    // 下单
    $('.bill .bill-right').click(function () {
        $.get('/generateorder/', function (response) {
            console.log(response)
            if (response.status == 1) {  // 跳转到订单详情
                window.open('/orderinfo/' + response.identifier +
                    '/', target = '_self')
            }
        })
    })

})

