$(document).ready(function(){
    // Hide menu when menu item is clicked (for small screen)
    $('#content').on('click', '#nav-items a', function() {
        $("#nav-items.show").collapse('hide');
    });
});