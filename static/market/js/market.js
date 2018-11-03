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
}