chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "fetchSummary") {
    const videoUrl = window.location.href;
    console.log("Video URL:", videoUrl); // Debugging: log the video URL
    fetch('http://localhost:5000/summarize', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: videoUrl })
    })
    .then(response => response.json())
    .then(data => {
      console.log("Summary data:", data); // Debugging: log the summary data
      sendResponse({ summary: data.summary });
    })
    .catch(error => {
      console.error('Error:', error); // Debugging: log any errors
    });
    return true; // Will respond asynchronously.
  }
});
