document.addEventListener("DOMContentLoaded", () => {
    const articleContent = document.getElementById("article-content");

    // 1. Get the post name from the URL
    const params = new URLSearchParams(window.location.search);
    const postName = params.get('name'); // e.g., "post1"

    if (!postName) {
        articleContent.innerHTML = "<h1>Error</h1><p>No article specified. Please return to the home page.</p>";
        return;
    }

    // 2. Define the path to the Markdown file
    const postPath = `posts/${postName}.md`;

    // 3. Fetch the Markdown file
    fetch(postPath)
        .then(response => {
            if (!response.ok) {
                throw new Error("Could not load article.");
            }
            return response.text();
        })
        .then(markdownText => {
            // 4. Convert Markdown to HTML using marked.js
            const htmlContent = marked.parse(markdownText);

            // 5. Inject the HTML into the page
            articleContent.innerHTML = htmlContent;

            // 6. Trigger MathJax to render LaTeX expressions
            if (window.MathJax) {
                MathJax.typesetPromise([articleContent]).catch((err) => console.log('MathJax error:', err));
            }

            // 7. (Optional) Set the page title from the first <h1>
            const firstHeading = articleContent.querySelector("h1");
            if (firstHeading) {
                document.title = firstHeading.textContent + " - Varol Cagdas Tok";
            }
        })
        .catch(error => {
            console.error("Error fetching article:", error);
            articleContent.innerHTML = "<h1>Error 404</h1><p>Article not found. Please check the URL and try again.</p>";
        });
});