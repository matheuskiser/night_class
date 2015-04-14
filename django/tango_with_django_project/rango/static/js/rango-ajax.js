$('#likes').click(function () {
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function (data) {
        $('#like_count').html(data);
        $('#likes').hide();
    });
});

$('#suggestion').keyup(function () {
    var query;
    query = $(this).val();
    $.get('/rango/suggest_category/', {suggestion: query}, function (data) {
        $('#cats').html(data);
    });
});

$('.rango-add').click(function () {
    var catid = $(this).attr("data-catid");
    var cat_page_title = $(this).attr("data-title");
    var cat_page_url = $(this).attr("data-url");
    $(this).hide();
    $.get('/rango/auto_add_page/', {category_id: catid, title: cat_page_title, url: cat_page_url}, function (data) {
        $('#pages').html(data);
        $(this).hide();
    });
});