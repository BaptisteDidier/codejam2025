// src/services/api.js
export async function uploadFile(file) {
    await new Promise(resolve => setTimeout(resolve, 500));
  
    return {
      id: Math.floor(Math.random() * 1000),
      filename: file.name,
      status: 'Processed',
      uploadTime: new Date().toLocaleString(),
      insights: [
        { label: 'Metric A', value: Math.floor(Math.random() * 50) },
        { label: 'Metric B', value: Math.floor(Math.random() * 50) },
        { label: 'Metric C', value: Math.floor(Math.random() * 50) }
      ]
    };
  }
  
  export async function fetchHistory() {
    await new Promise(resolve => setTimeout(resolve, 500));
  
    return [
      { id: 1, filename: 'sales.csv', status: 'Processed', uploadTime: '2025-11-15 12:00' },
      { id: 2, filename: 'inventory.json', status: 'Processed', uploadTime: '2025-11-14 15:30' }
    ];
  }

  export async function fetchInsights(fileId) {
    await new Promise(resolve => setTimeout(resolve, 500));
  
    return [
      { label: 'Metric A', value: Math.floor(Math.random() * 50) },
      { label: 'Metric B', value: Math.floor(Math.random() * 50) },
      { label: 'Metric C', value: Math.floor(Math.random() * 50) }
    ];
  }
  
  