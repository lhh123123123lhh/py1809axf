$(function () {
    // 设置隐藏滚动条
    $('.market').width(innerWidth)
    //　保存下标
    typeIndex = $.cookie('typeIndex')
    if (typeIndex) {
        $('.type-slider .list1').eq(typeIndex).addClass('active')
    } else {
        $('.type-slider .list1').eq(0).addClass('active')
    }
    $('.list1').click(function () {
        // $(this).addClass('active')
        $.cookie('typeIndex', $(this).index(), {exprires: 3, path: '/'})
    })
    // 顶部导航
    alltypesBt = false
    $('#alltypesBt').click(function () {
        alltypesBt = !alltypesBt
        if (alltypesBt) {
            sortBt = false
            $('.bounce-view.type-view').show()
            $('#alltypesBt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
            $('.bounce-view.sort-view').hide()
            $('#sortBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        } else {
            $('.bounce-view.type-view').hide()
            $('#alltypesBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        }

    })
    sortBt = false
    $('#sortBt').click(function () {
        sortBt = !sortBt
        if (sortBt) {
            alltypesBt = false
            $('.bounce-view.sort-view').show()
            $('#sortBt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
            $('.bounce-view.type-view').hide()
            $('#alltypesBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        } else {
            $('.bounce-view.sort-view').hide()
            $('#sortBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        }
    })
    $('.bounce-view').click(function () {
        alltypesBt = false
        $('.bounce-view.type-view').hide()
        $('#alltypesBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')

        sortBt = false
        $('.bounce-view.sort-view').hide()
        $('#sortBt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    })


    $('.bt-wrapper .glyphicon-minus').hide()
    $('.bt-wrapper .num').hide()

    $('.bt-wrapper .num').each(function () {
        var num = $(this).html()
        if (num) {   // 有数据，即有添加购物车
            $(this).show()
            $(this).prev().show()
        }
    })
    // 加操作
    $('.bt-wrapper .glyphicon-plus').click(function () {
        // console.log('我被点了')
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)
        $.get('/addToCart/', {'goodsid': goodsid}, function (response) {
            console.log(response)
            if (response.status == -1) {
                window.open('/login/', target = "_self")
            } else if (response.status == 1) {
                $that.prev().html(response.number)
            }

        })
    })
    $('.bt-wrapper .glyphicon-minus').click(function () {
        // 商品ID
        var goodsid = $(this).attr('goodsid')
        var $that = $(this)
        // 发起ajax请求
        $.get('/subToCart/', {'goodsid': goodsid}, function (response) {
            console.log(response)
            if (response.status == 1) {  // 操作成功
                var number = response.number
                if (number > 0) {   // 显示，改变个数
                    $that.next().html(number)
                } else {   // 隐藏减号和个数
                    $that.next().hide()
                    $that.hide()
                }
            }
        })
    })
})