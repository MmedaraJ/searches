function submit(){
    $.ajax({
        method: $('#fetch_form').attr('method'),
        url: $('#fetch_form').attr('action'),
        data: $('#fetch_form').serialize(),
        success: function(response){
            $('#placeholder').html(response)
            return false;
        }
    });
    return false;
}

$(document).ready(function(){
    $('input[name=records]').keyup(function(){
        submit();
    })
})