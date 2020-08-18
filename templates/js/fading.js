/*----------------------------------------------------*/
/* Fading in/out quotes
------------------------------------------------------ */

(window.onload = function() {

    var quotes = $(".quotes");
    var quoteIndex = -1;
    
    function showNextQuote() {
        ++quoteIndex;
        quotes.eq(quoteIndex % quotes.length)
            .fadeIn(1000)
            .delay(2000)
            .fadeOut(1000, showNextQuote);
    }
    
    showNextQuote();
    
})();

