function renderMath() {
    // If MathJax is available, tell it to re-render the page
    if (window.MathJax) {
        window.MathJax.typeset();
    }
}
