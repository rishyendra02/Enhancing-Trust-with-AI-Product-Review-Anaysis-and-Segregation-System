function filterReviews(sentiment) {
    var rows = document.querySelectorAll('.review-row');
    
    rows.forEach(function(row) {
        var rowSentiment = row.getAttribute('data-sentiment');
        
        if (sentiment === 'All' || rowSentiment === sentiment) {
            row.style.display = 'table-row';
        } else {
            row.style.display = 'none';
        }
    });
}