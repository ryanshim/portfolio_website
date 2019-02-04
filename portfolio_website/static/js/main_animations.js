$("#main-btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#trgt-main").offset().top
    }, 1000);
});

$("#prj-btn").click(function() {
    $('html, body').animate({
        scrollTop: $("#trgt-projects").offset().top
    }, 1000);
});

$("#contact-btn").click(function() {
    $('html, body').animate({
        scrollTop:$("#trgt-contact").offset().top
    }, 1000);
});
