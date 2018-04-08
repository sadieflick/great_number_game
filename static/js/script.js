$(document).ready(function(){

    if ($('h2').html() == "") {
        $('#answerBox').hide();
    }

    $('#get_guess').submit(function() {
        $('#answerBox').show();
    });

    if ($('h2').text().indexOf('was the number!') > -1) {
        $('#answerBox').css('background-color', "green");
        $('#answerBox').append("<button id='start'>start over<button>")
        $(document).on("click", "#start", function(){
            location.reload();
        });
        $('#get_guess').hide();
        
    }
    // $(document).on("submit", "#get_guess", function(event) {
    //     if ($('h2').text().indexOf('was the number!') > -1) {
    //         $('#answerBox').css('background-color', "green");
    //         console.log("Should turn green")
    //     }
    
    // });
    
    var htmlString = $('h2').html();
    // if (htmlString == "<%session['randomNum']%>" + " was the number!"){
    //     $('#get_guess').css('background-color', "green");
    // }
    console.log("Returning html string:", htmlString);
});