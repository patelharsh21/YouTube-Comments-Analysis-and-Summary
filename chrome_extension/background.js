chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    // Check if the tab is fully loaded and if it is a YouTube video page
    if (changeInfo.status === 'complete' && tab.url.includes('youtube.com/watch')) {
        // Inject the content script
        chrome.scripting.executeScript({
            target: { tabId: tabId },
            files: ['contentScript.js']
        });
    }
});

// chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
//     // Check if the tab is fully loaded and if it is a YouTube video page
//     if (changeInfo.status === 'complete' && tab.url && tab.url.includes('youtube.com/watch')) {
//         // Inject the content script
//         chrome.scripting.executeScript({
//             target: { tabId: tabId },
//             files: ['contentScript.js']
//         });
//     }
// });
