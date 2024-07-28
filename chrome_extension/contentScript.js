// contentScript.js

function addSummaryButton() {
    // Check if the button is already added
    if (document.getElementById('summaryContainer')) {
        return;
    }

    // Find the comment section
    const commentSection = document.querySelector('#comments');

    if (commentSection) {
        // Create the container for the button and summary
        const container = document.createElement('div');
        container.id = 'summaryContainer';

        // Create the button
        const button = document.createElement('button');
        button.id = 'summarizeBtn';
        button.innerText = 'Get Summary';
        button.style.marginBottom = '10px';

        // Create the summary display area
        const summaryDiv = document.createElement('div');
        summaryDiv.id = 'summary';
        summaryDiv.style.border = '1px solid #ccc';
        summaryDiv.style.padding = '10px';
        summaryDiv.style.borderRadius = '5px';

        // Append the button and summary div to the container
        container.appendChild(button);
        container.appendChild(summaryDiv);

        // Insert the container into the comment section
        commentSection.insertBefore(container, commentSection.firstChild);

        // Add event listener to the button
        button.addEventListener('click', summarizeComments);
    }
}

async function summarizeComments() {
    const videoUrl = window.location.href;
    const summaryDiv = document.getElementById('summary');

    summaryDiv.innerText = 'Summarizing...';

    try {
        const response = await fetch('http://localhost:5000/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: videoUrl })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        summaryDiv.innerHTML = `<h2>Summary</h2><p>${data.summary}</p>`;
    } catch (error) {
        summaryDiv.innerText = `Error: ${error.message}`;
    }
}

function init() {
    // Observe changes in the body to catch dynamically loaded comments section
    const observer = new MutationObserver(() => {
        addSummaryButton();
    });

    observer.observe(document.body, { childList: true, subtree: true });
}

// Wait for the DOM to load
window.addEventListener('load', () => {
    init();
});
