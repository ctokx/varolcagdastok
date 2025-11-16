document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("all-articles-container");
    if (!container) {
        // Failsafe in case the ID is wrong
        console.error("Error: Could not find element #all-articles-container.");
        return;
    }

    fetch("js/posts.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const categories = data.categories;

            if (!categories || categories.length === 0) {
                container.innerHTML = "<p>No articles have been published yet.</p>";
                return;
            }

            // 1. Sort categories alphabetically for a consistent order
            categories.sort((a, b) => a.name.localeCompare(b.name));

            // 2. Build the HTML
            let allHtml = "";
            
            for (const category of categories) {
                allHtml += `<section class="category">`;
                allHtml += `<h3>${category.name}</h3>`;
                
                // Add the new description
                if (category.description) {
                    allHtml += `<p class="category-description">${category.description}</p>`;
                }
                
                allHtml += `<ul class="article-list">`;
                
                const articles = category.articles || [];
                
                // 3. Sort articles within each category by date (newest first)
                articles.sort((a, b) => new Date(b.date) - new Date(a.date));
                
                for (const article of articles) {
                    // Format the date for display
                    const displayDate = new Date(article.date).toLocaleDateString('en-US', {
                        year: 'numeric',
                        month: 'long',
                        day: 'numeric'
                    });
                    
                    allHtml += `
                        <li>
                            <a href="${article.url}">${article.title}</a>
                            <span class="post-date">(${displayDate})</span>
                        </li>
                    `;
                }
                
                allHtml += `</ul></section>`;
            }

            // 4. Inject the final HTML into the page
            container.innerHTML = allHtml;

        })
        .catch(error => {
            console.error("Error fetching or processing articles:", error);
            container.innerHTML = "<p>Error loading articles. Please check the `js/posts.json` file and make sure it is valid.</p>";
        });
});