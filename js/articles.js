document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("all-articles-container");
    if (!container) {
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

            // Keep categories in their original order from posts.json
            let allHtml = "";

            for (const category of categories) {
                const articles = category.articles || [];
                const totalArticles = articles.length;
                const categoryId = category.name.toLowerCase().replace(/[^a-z0-9]+/g, '-');

                // Build category section with collapsible functionality
                allHtml += `
                    <div class="category-section">
                        <div class="category-header" onclick="toggleCategory('${categoryId}')">
                            <h3>
                                <span class="category-toggle" id="toggle-${categoryId}">▼</span>
                                ${category.name}
                                <span class="category-count">(${totalArticles} article${totalArticles !== 1 ? 's' : ''})</span>
                            </h3>
                        </div>

                        <div class="category-content" id="content-${categoryId}">
                            <p class="category-description">${category.description || ''}</p>

                            <ul class="article-list" id="list-${categoryId}">
                `;

                // Add articles to list (all of them, control visibility with CSS)
                for (let i = 0; i < articles.length; i++) {
                    const article = articles[i];
                    const isInitiallyHidden = i >= 7; // Hide after first 7

                    allHtml += `
                        <li class="${isInitiallyHidden ? 'hidden-article' : ''}">
                            <h3><a href="${article.url}">${article.title}</a></h3>
                            <span class="article-date">by ${article.author || 'Tok Varol Cagdas'}</span>
                        </li>
                    `;
                }

                allHtml += `
                            </ul>

                            ${totalArticles > 7 ? `
                                <button class="show-more-btn" id="btn-${categoryId}" onclick="toggleShowMore('${categoryId}', ${totalArticles})">
                                    Show All ${totalArticles} Articles ▼
                                </button>
                            ` : ''}
                        </div>
                    </div>
                `;
            }

            container.innerHTML = allHtml;

        })
        .catch(error => {
            console.error("Error fetching or processing articles:", error);
            container.innerHTML = "<p>Error loading articles. Please check the `js/posts.json` file and make sure it is valid.</p>";
        });
});

// Toggle category collapse/expand
function toggleCategory(categoryId) {
    const content = document.getElementById(`content-${categoryId}`);
    const toggle = document.getElementById(`toggle-${categoryId}`);

    if (content.style.display === "none") {
        content.style.display = "block";
        toggle.textContent = "▼";
    } else {
        content.style.display = "none";
        toggle.textContent = "▶";
    }
}

// Toggle show more/less articles
function toggleShowMore(categoryId, totalArticles) {
    const list = document.getElementById(`list-${categoryId}`);
    const button = document.getElementById(`btn-${categoryId}`);
    const hiddenArticles = list.querySelectorAll('.hidden-article');

    if (button.classList.contains('showing-all')) {
        // Collapse back to showing 7
        hiddenArticles.forEach(article => {
            article.style.display = 'none';
        });
        button.textContent = `Show All ${totalArticles} Articles ▼`;
        button.classList.remove('showing-all');
    } else {
        // Expand to show all
        hiddenArticles.forEach(article => {
            article.style.display = 'list-item';
        });
        button.textContent = `Show Less ▲`;
        button.classList.add('showing-all');
    }
}