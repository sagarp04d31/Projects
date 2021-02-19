/* For the sticky navigation */
    $('.jstech').waypoint(function(direction) {
        if (direction == "down") {
            $('nav').addClass('.sticky');
        } else {
            $('nav').removeClass('.sticky');
        }
    }, {
      offset: '60px;'
    });
    