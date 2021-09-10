$(document).ready(function(){
    function load_data(query){
        $.ajax({
            url:"/ajaxlivesearch",
            method:"POST",
            data:{query:query},
            success:function(data){
                $('#result').html(data);
            }
        });
    }
    $('#search_text').keyup(function(){
        var search = $(this).val();
        if(search != ""){
            load_data(search);
        }else{
            load_data();
        }
    });
});
