// Configure MathJax before it loads
window.MathJax = {
    tex: {
        inlineMath: [['$', '$']],
        displayMath: [['$$', '$$']],
        processEscapes: true,
        processEnvironments: true
    },
    options: {
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
    }
};

function renderMath() {
    // If MathJax is available, tell it to re-render the page
    if (window.MathJax && window.MathJax.typeset) {
        window.MathJax.typeset();
    }
}
