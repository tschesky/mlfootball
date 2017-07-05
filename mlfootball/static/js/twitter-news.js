$(document).ready(function() {
	$(".twitter_buttons").click(function() {
	    $(".twitter-content").css("display", "none");
	    var buttonId = jQuery(this).attr("id");
	    var twitterPaneId = "#" + buttonId.slice(0, -6) + "content";
        $(twitterPaneId).show();
	});

});