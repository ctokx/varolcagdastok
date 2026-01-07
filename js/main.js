document.addEventListener("DOMContentLoaded", () => {
    const articlesList = document.getElementById("articles-list");
    if (!articlesList) return;

    fetch("js/posts.json")
        .then(response => {
            if (!response.ok) throw new Error("Network error");
            return response.json();
        })
        .then(data => {
            const allArticles = data.categories.flatMap(c => c.articles || []);
            const articlesToShow = 3;
            const recent = allArticles.slice(0, articlesToShow);

            if (recent.length === 0) {
                articlesList.innerHTML = "<li>No articles yet.</li>";
                return;
            }

            articlesList.innerHTML = recent.map(article => {
                return `<li>
                    <h3><a href="${article.url}">${article.title}</a></h3>
                    <p>${article.summary}</p>
                </li>`;
            }).join("");
        })
        .catch(() => {
            articlesList.innerHTML = "<li>Error loading articles.</li>";
        });
});