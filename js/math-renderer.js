function renderMarkdownWithMath(text) {
    if (!text) return '';

    if (text.startsWith('---')) {
        const parts = text.split('---');
        if (parts.length >= 3) {
            text = parts.slice(2).join('---').trim();
        }
    }

    const mathBlocks = [];

    text = text.replace(/\$\$([\s\S]*?)\$\$/g, function (match, math) {
        mathBlocks.push({ type: 'display', math: math.trim() });
        return `%%%MATH_BLOCK_${mathBlocks.length - 1}%%%`;
    });

    text = text.replace(/\$([^$\n]+?)\$/g, function (match, math) {
        mathBlocks.push({ type: 'inline', math: math.trim() });
        return `%%%MATH_INLINE_${mathBlocks.length - 1}%%%`;
    });

    let html = marked.parse(text);

    html = html.replace(/%%%MATH_INLINE_(\d+)%%%/g, function (match, index) {
        const block = mathBlocks[parseInt(index)];
        return `<span class="math-inline">\\(${block.math}\\)</span>`;
    });

    html = html.replace(/%%%MATH_BLOCK_(\d+)%%%/g, function (match, index) {
        const block = mathBlocks[parseInt(index)];
        return `<div class="math-display">\\[${block.math}\\]</div>`;
    });

    return html;
}

function renderMath() {
    const element = document.getElementById('article-content');
    if (!element || !window.renderMathInElement) return;

    renderMathInElement(element, {
        delimiters: [
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false,
        errorColor: '#cc0000',
        strict: false,
        trust: true,
        macros: {
            "\\R": "\\mathbb{R}",
            "\\N": "\\mathbb{N}",
            "\\Z": "\\mathbb{Z}"
        }
    });
}

window.renderMarkdownWithMath = renderMarkdownWithMath;
window.renderMath = renderMath;
