// Wait for the HTML document to be fully loaded
document.addEventListener("DOMContentLoaded", () => {
    
    // Find the container for our articles
    const articlesList = document.getElementById("articles-list");

    // Only run this code if we are on a page that HAS the "articles-list" element
    if (articlesList) {
        
        // Fetch the list of articles from our JSON file
        fetch("js/posts.json")
            .then(response => {
                if (!response.ok) {
                    throw new Error("Network response was not ok: " + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // 1. Flatten all articles from all categories into one list
                const allArticles = data.categories.flatMap(category => category.articles || []);
                
                // You can change this number to show more or fewer "latest" articles
                const articlesToShow = 3;
                
                // 2. Sort all articles by date, newest first.
                allArticles.sort((a, b) => new Date(b.date) - new Date(a.date));
                
                // 3. Get the most recent articles
                const recentArticles = allArticles.slice(0, articlesToShow);

                // If there are no articles, show a message
                if (recentArticles.length === 0) {
                    articlesList.innerHTML = "<li>No articles published yet.</li>";
                    return;
                }

                // Build the HTML for each article
                const articlesHTML = recentArticles.map(article => {
                    // Format the date for display
                    const displayDate = new Date(article.date).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                    });

                    return `
                        <li>
                            <h3><a href="${article.url}">${article.title}</a></h3>
                            <p class="article-date">${displayDate}</p>
                            <p>${article.summary}</p>
                        </li>
                    `;
                }).join(""); // Join all list items into a single string

                // Add the HTML to the page
                articlesList.innerHTML = articlesHTML;
            })
            .catch(error => {
                console.error("Error fetching articles:", error);
                articlesList.innerHTML = "<li>Error loading articles. Please check file paths and JSON format.</li>";
            });
    }
});