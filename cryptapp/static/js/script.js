var $ = jQuery.noConflict();



// Progress Bar

$(document).ready(function ($) {
    "use strict";
    
    $('.skill-shortcode').appear(function () {
        $('.progress').each(function () {
            $('.progress-bar').css('width',  function () { return ($(this).attr('data-percentage') + '%')});
        });
    }, {accY: -100});
        
    var frm = $('#SystemForm');
    $("#click").click(function () {
        $.ajax({
            url:'/system/',
            success: function (data) {
                $("#result").html(data);
            },
            error: function(data) {
                $("#result").html("Something went wrong!");
            }
        });
        return false;
    });    
});