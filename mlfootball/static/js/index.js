$(document).ready(function() {
  $('.all').click(function(e){        
    $('.1729').show();
    $('.21518').show();
    $('.premiere').removeClass('active');
    $('.laliga').removeClass('active');
    $('.all').addClass('active');
  });

  $('.premiere').click(function(e){        
    $('.1729').show();
    $('.21518').hide();
    $('.premiere').addClass('active');
    $('.laliga').removeClass('active');
    $('.all').removeClass('active');
  });

  $('.laliga').click(function(e){        
    $('.1729').hide();
    $('.21518').show();
    $('.laliga').addClass('active');
    $('.premiere').removeClass('active');
    $('.all').removeClass('active');
  });
});