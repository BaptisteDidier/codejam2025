// src/services/api.js

// Load history (fake static + user uploads)
function loadStoredHistory() {
    const stored = JSON.parse(localStorage.getItem("uploadHistory") || "[]");
  
    // These should always appear (your fake history)
    const baseHistory = [
      { id: 1, filename: 'sales.csv', status: 'Processed', uploadTime: '2025-11-15 12:00' },
      { id: 2, filename: 'inventory.json', status: 'Processed', uploadTime: '2025-11-14 15:30' }
    ];
  
    return [...baseHistory, ...stored];
  }
  
  function saveHistory(item) {
    const stored = JSON.parse(localStorage.getItem("uploadHistory") || "[]");
    stored.push(item);
    localStorage.setItem("uploadHistory", JSON.stringify(stored));
  }
  
  // UPLOAD FILE
  export async function uploadFile(file) {
    await new Promise(resolve => setTimeout(resolve, 500));
  
    const newEntry = {
      id: Math.floor(Math.random() * 100000),
      filename: file.name,
      status: 'Processed',
      uploadTime: new Date().toLocaleString(),
      insights: [
        { label: 'Metric A', value: Math.floor(Math.random() * 50) },
        { label: 'Metric B', value: Math.floor(Math.random() * 50) },
        { label: 'Metric C', value: Math.floor(Math.random() * 50) }
      ]
    };
  
    // Save to localStorage
    saveHistory(newEntry);
  
    return newEntry;
  }
  
  // FETCH HISTORY
  export async function fetchHistory() {
    await new Promise(resolve => setTimeout(resolve, 500));
    return loadStoredHistory();
  }
  
  // FETCH INSIGHTS
  export async function fetchInsights(fileId) {
    await new Promise(resolve => setTimeout(resolve, 500));
  
    return [
      { label: 'Metric A', value: Math.floor(Math.random() * 50) },
      { label: 'Metric B', value: Math.floor(Math.random() * 50) },
      { label: 'Metric C', value: Math.floor(Math.random() * 50) }
    ];
  }
  
  