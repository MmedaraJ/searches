function submit(){
    $.ajax({
        method: $('#filter_form').attr('method'),
        url: $('#filter_form').attr('action'),
        data: $('#filter_form').serialize(),
        success: function(response){
            $('#placeholder').html(response)
        }
    });
    return false;
}

$(document).ready(function(){
    $('input[name=name]').keyup(function(){
        submit();
    })
    $('input[name=gender]').change(function(){
        submit();
    })
    $('input[name=sport]').change(function(){
        submit();
    })
})