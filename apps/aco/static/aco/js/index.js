$(document).ready(function(){
    $('#fetch_form').submit(function(){
        $.post(
            $(this).attr('action'),
            $(this).serialize(),
            function(res){
                console.log('The response object');
                console.log(res);
                var html_string = "";
                if(res.results.length !== 0){
                    $('#placeholder').html("")
                    for (var i=0; i<res.results.length; i++){
                        $('#placeholder').append("<video controls src='" + res.results[i].previewUrl + "'></video>");
                    }
                }
                else{
                    $('#placeholder').html("Not found");
                }
            },
            'json'
        );
        return false;
    });
});