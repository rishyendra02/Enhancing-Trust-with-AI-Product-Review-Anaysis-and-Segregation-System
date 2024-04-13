// Function to filter reviews based on sentiment
function filterReviews(sentiment) {
    var rows = document.querySelectorAll('.review-row');
    
    // Initialize counts for positive, negative, and neutral reviews
    var positiveCount = 0;
    var negativeCount = 0;
    var neutralCount = 0;
    
    rows.forEach(function(row) {
        var rowSentiment = row.getAttribute('data-sentiment');
        
        if (sentiment === 'All' || rowSentiment === sentiment) {
            row.style.display = 'table-row';
            
            // Increment respective count based on sentiment
            if (rowSentiment === 'Positive') {
                positiveCount++;
            } else if (rowSentiment === 'Negative') {
                negativeCount++;
            } else if (rowSentiment === 'Neutral') {
                neutralCount++;
            }
        } else {
            row.style.display = 'none';
        }
    });
    
    // Render bar graph using counts
    renderBarGraph(positiveCount, negativeCount, neutralCount);
}

// Function to render the bar graph
function renderBarGraph(positiveCount, negativeCount, neutralCount) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');

    const myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Positive', 'Negative', 'Neutral'],
            datasets: [{
                label: 'Number of Reviews',
                data: [positiveCount, negativeCount, neutralCount],
                backgroundColor: [
                    'rgba(50, 205, 50, 0.5)',  // Green for positive
                    'rgba(255, 99, 71, 0.5)',   // Red for negative
                    'rgba(135, 206, 250, 0.5)' 
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
