document.getElementById('summarizeBtn').addEventListener('click', async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const videoUrl = tab.url;

  if (!videoUrl.includes("youtube.com/watch")) {
      document.getElementById('summary').innerText = 'Please open a YouTube video.';
      return;
  }

  document.getElementById('summary').innerText = 'Summarizing...';

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
      document.getElementById('summary').innerHTML = `<h2>Summary</h2><p>${data.summary}</p>`;
  } catch (error) {
      document.getElementById('summary').innerText = `Error: ${error.message}`;
  }
});
