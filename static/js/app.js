var routes = {
    'up': '/up',
    'down': '/down',
    'watt': '/watt',
    'power': '/power'
};
for(var route in routes) {
    $('#'+route).click(function(e) {
        $.ajax({
            url: '/rest' + routes[e.target.id],
            method: 'GET',
            beforeSend: function() { $('#'+e.target.id).attr('disabled', true) },
            complete: function() { $('#'+e.target.id).attr('disabled', false) }
        });
    });
}
