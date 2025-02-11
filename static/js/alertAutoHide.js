document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert.alert-danger, .alert.alert-success');
        alerts.forEach(function(alert) {
            alert.style.display = 'none';
        });
    }, 3000);
}); 