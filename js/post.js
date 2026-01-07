document.addEventListener("DOMContentLoaded", () => {
    const articleContent = document.getElementById("article-content");
    const params = new URLSearchParams(window.location.search);
    const postName = params.get('name');

    if (!postName) {
        articleContent.innerHTML = "<h1>Error</h1><p>No article specified.</p>";
        return;
    }

    fetch(`posts/${postName}.md`)
        .then(response => {
            if (!response.ok) throw new Error("Not found");
            return response.text();
        })
        .then(markdown => {
            articleContent.innerHTML = marked.parse(markdown);

            if (window.MathJax) {
                MathJax.typesetPromise([articleContent]).catch(() => { });
            }

            const h1 = articleContent.querySelector("h1");
            if (h1) document.title = h1.textContent + " - Varol Cagdas Tok";
        })
        .catch(() => {
            articleContent.innerHTML = "<h1>404</h1><p>Article not found.</p>";
        });
});