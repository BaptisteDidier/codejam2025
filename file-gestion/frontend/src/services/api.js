const API_BASE = "http://127.0.0.1:8000";

export async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE}/upload`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    let errDetail = "Upload failed";
    try {
      const errJson = await response.json();
      errDetail = errJson.detail || errDetail;
    } catch (e) {}
    throw new Error(errDetail);
  }

  const data = await response.json();
  return {
    id: data.id,
    filename: file.name,
    status: "Processed",
    uploadTime: new Date().toLocaleString()
  };
}

export async function fetchHistory(limit = 10, offset = 0) {
  const response = await fetch(`${API_BASE}/history?limit=${limit}&offset=${offset}`);

  if (!response.ok) {
    let errDetail = "Failed to fetch history";
    try {
      const errJson = await response.json();
      errDetail = errJson.detail || errDetail;
    } catch (e) {}
    throw new Error(errDetail);
  }

  const data = await response.json();
  return data.history.map(item => ({
    id: item.id,
    filename: item.filename,
    status: "Processed",
    uploadTime: new Date(item.uploaded_at).toLocaleString()
  }));
}

export async function fetchInsights(fileId) {
  return [];
}
