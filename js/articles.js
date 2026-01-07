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

            let html = '<div class="articles-dense-grid">';

            for (const category of categories) {
                const articles = category.articles || [];
                for (const article of articles) {
                    html += `<a href="${article.url}" class="dense-article-link">${article.title}</a>`;
                }
            }

            html += '</div>';
            container.innerHTML = html;
        })
        .catch(() => {
            container.innerHTML = "<p>Error loading articles.</p>";
        });
});