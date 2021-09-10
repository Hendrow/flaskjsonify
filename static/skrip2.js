$(document).ready(function(){
    load_data();
    function load_data(hasil){
        $.ajax({
            url: '/ajaxlivesearch',
            method: 'POST',
            data: {hasil:hasil},
            success: function(data){
                $("#result").html(data);
                $('#result').append(data.htmlresponse);
            }
        })
    }

    $('#search_text').keyup(function(){
       var cari = $(this).val();
       if (cari!=""){
           load_data(cari)
       }else{
           load_data()
       }

    })
})