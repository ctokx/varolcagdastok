document.addEventListener("DOMContentLoaded", () => {
    const container = document.getElementById("all-articles-container");
    if (!container) return;

    fetch("js/posts.json")
        .then(response => {
            if (!response.ok) throw new Error("Network error");
            return response.json();
        })
        .then(data => {
            const categories = data.categories;
            if (!categories || categories.length === 0) {
                container.innerHTML = "<p>No articles yet.</p>";
                return;
            }

            let html = '';

            for (const category of categories) {
                const articles = category.articles || [];
                if (articles.length === 0) continue;

                html += `<div class="category">`;
                html += `<h2>${category.name}</h2>`;
                if (category.description) {
                    html += `<p class="category-description">${category.description}</p>`;
                }
                html += `<ul class="article-list">`;

                for (const article of articles) {
                    html += `<li>`;
                    html += `<h3><a href="${article.url}">${article.title}</a></h3>`;
                    // html += `<span class="post-date">Order: ${article.order}</span>`; // Optional
                    html += `</li>`;
                }

                html += `</ul>`;
                html += `</div>`;
            }

            container.innerHTML = html;
        })
        .catch(() => {
            container.innerHTML = "<p>Error loading articles.</p>";
        });
});