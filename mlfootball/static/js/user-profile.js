$(document).ready(function() { 
	$("#settings").click(function() {
   		$("#overview").removeClass("active");
   		$("#help").removeClass("active");
    	$("#settings").addClass("active");
    	$("#overview_content").hide();
    	$("#help_content").hide();
    	$("#settings_content").show();
	});

	$("#overview").click(function() {
   		$("#settings").removeClass("active");
   		$("#help").removeClass("active");
    	$("#overview").addClass("active");
    	$("#overview_content").show();
    	$("#help_content").hide();
    	$("#settings_content").hide();
	});

	$("#help").click(function() {
   		$("#overview").removeClass("active");
   		$("#settings").removeClass("active");
    	$("#help").addClass("active");
    	$("#overview_content").hide();
    	$("#help_content").show();
    	$("#settings_content").hide();
	});
});
