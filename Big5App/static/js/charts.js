document.addEventListener('DOMContentLoaded', function() {
    // Parse JSON data from HTML
    const percentiles = JSON.parse(document.getElementById('percentiles-data').textContent);
    const topCountries = JSON.parse(document.getElementById('top-countries-data').textContent);
    const newUserMeanScores = JSON.parse(document.getElementById('new-user-mean-scores-data').textContent);
    const allUsersMeanScores = JSON.parse(document.getElementById('all-users-mean-scores-data').textContent);

    // Percentile Scores Chart
    const percentileCtx = document.getElementById('percentileChart').getContext('2d');
    new Chart(percentileCtx, {
        type: 'bar',
        data: {
            labels: Object.keys(percentiles),
            datasets: [{
                label: 'Percentile Scores',
                data: Object.values(percentiles),
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Top 5 Countries Chart
    const topCountriesCtx = document.getElementById('topCountriesChart').getContext('2d');
    new Chart(topCountriesCtx, {
        type: 'pie',
        data: {
            labels: topCountries,
            datasets: [{
                label: 'Top 5 Countries',
                data: Array(topCountries.length).fill(1), // Dummy data for pie chart
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        }
    });

    // New User Mean Scores Chart
    const newUserMeanScoresCtx = document.getElementById('newUserMeanScoresChart').getContext('2d');
    new Chart(newUserMeanScoresCtx, {
        type: 'radar',
        data: {
            labels: Object.keys(newUserMeanScores),
            datasets: [{
                label: 'New User Mean Scores',
                data: Object.values(newUserMeanScores),
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                r: {
                    beginAtZero: true
                }
            }
        }
    });

    // All Users Mean Scores Chart
    const allUsersMeanScoresCtx = document.getElementById('allUsersMeanScoresChart').getContext('2d');
    new Chart(allUsersMeanScoresCtx, {
        type: 'radar',
        data: {
            labels: Object.keys(allUsersMeanScores),
            datasets: [{
                label: 'All Users Mean Scores',
                data: Object.values(allUsersMeanScores),
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                r: {
                    beginAtZero: true
                }
            }
        }
    });
});
