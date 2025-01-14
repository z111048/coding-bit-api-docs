# React 進階開發技巧 ｜ 課程詳細 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: /Coding-bit/video-details.html
- **頁面用途**: 課程詳細資訊展示，包含影片播放、課程內容介紹、留言互動區以及相關推薦課程。
- **主要功能**: 
  - 提供課程影片播放功能。
  - 展示課程相關資訊（名稱、觀看次數、評分、標籤、作者資訊）。
  - 顯示課程簡介和留言互動區。
  - 推薦相關課程及講師其他課程。
  - 章節導航功能。

---

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供頁面導航功能，快速跳轉至其他頁面。
- **包含元素**: 搜尋框、導航連結（精選課程、一對一教學、課程客製化、幫助中心），登入/註冊按鈕。
- **數據需求**: 無（靜態內容）。
- **互動行為**: 
  - 搜尋框輸入關鍵字觸發搜尋。
  - 點擊導航連結跳轉。
  - 點擊「登入/註冊」按鈕跳轉至對應頁面。
- **相依性**: 搜尋功能需後端 API 支援。

---

### 2.2 影片播放區
- **用途**: 播放課程影片，顯示課程標題、觀看次數、評分。
- **包含元素**: 影片播放器、課程標題、觀看次數、評分。
- **數據需求**: 
  - 影片 URL。
  - 影片封面圖片。
  - 課程標題。
  - 觀看次數。
  - 評分數值。
- **互動行為**: 
  - 點擊播放影片。
  - 評分或收藏按鈕狀態切換。
- **相依性**: 影片 URL 和數據需從後端 API 提供。

---

### 2.3 標籤區
- **用途**: 顯示課程相關的分類標籤，便於用戶篩選或了解課程內容。
- **包含元素**: 標籤按鈕（如 React、前端開發、效能優化）。
- **數據需求**: 標籤名稱。
- **互動行為**: 點擊標籤可觸發篩選或關聯課程推薦。
- **相依性**: 標籤數據由後端 API 提供。

---

### 2.4 留言互動區
- **用途**: 提供用戶發表評論及留言回覆功能。
- **包含元素**: 留言輸入框、留言列表（包含用戶名稱、時間、內容、回覆按鈕）。
- **數據需求**: 
  - 用戶名與頭像。
  - 評論內容及留言時間。
  - 回覆數據（如回覆內容、回覆用戶資訊）。
- **互動行為**: 
  - 發表新留言。
  - 回覆評論。
  - 刪除留言。
- **相依性**: 需要後端 API 支援留言 CRUD 操作。

---

### 2.5 推薦課程區
- **用途**: 顯示相關課程內容及講師其他課程。
- **包含元素**: 課程名稱、縮略圖、簡短介紹。
- **數據需求**: 
  - 課程名稱。
  - 縮略圖 URL。
  - 簡短介紹。
- **互動行為**: 點擊課程跳轉至詳細頁面。
- **相依性**: 推薦課程數據需要從後端 API 加載。

---

## 3. API 規格

### 3.1 獲取課程詳細資訊
```json
{
  "name": "GetCourseDetails",
  "endpoint": "/api/v1/courses/{courseId}",
  "method": "GET",
  "description": "獲取課程的詳細資訊，包括影片 URL、觀看次數、評分、標籤等。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {
      "courseId": "string"
    },
    "query": {}
  },
  "response": {
    "data": {
      "courseId": "string",
      "title": "string",
      "videoUrl": "string",
      "posterUrl": "string",
      "viewCount": "number",
      "rating": "number",
      "tags": ["string"],
      "author": {
        "name": "string",
        "avatarUrl": "string",
        "description": "string"
      }
    },
    "message": "string"
  },
  "errorResponses": [
    {
      "status": 404,
      "message": "課程未找到",
      "description": "指定的課程不存在。"
    },
    {
      "status": 401,
      "message": "未授權",
      "description": "用戶未登入或授權無效。"
    }
  ]
}
```

### 3.2 發表留言
```json
{
  "name": "PostComment",
  "endpoint": "/api/v1/courses/{courseId}/comments",
  "method": "POST",
  "description": "提交新留言。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {
      "courseId": "string"
    },
    "body": {
      "content": "string"
    }
  },
  "response": {
    "data": {
      "commentId": "string",
      "userId": "string",
      "content": "string",
      "createdAt": "timestamp"
    },
    "message": "string"
  },
  "errorResponses": [
    {
      "status": 400,
      "message": "留言內容無效",
      "description": "留言內容為空或超過字數限制。"
    },
    {
      "status": 401,
      "message": "未授權",
      "description": "用戶未登入或授權無效。"
    }
  ]
}
```

---

## 4. Mock 數據結構
```json
{
  "/api/v1/courses/12345": {
    "mockData": {
      "courseId": "12345",
      "title": "React 進階開發技巧",
      "videoUrl": "https://example.com/video.mp4",
      "posterUrl": "/assets/video-thumbnail.jpg",
      "viewCount": 12345,
      "rating": 4.8,
      "tags": ["React", "前端開發", "效能優化"],
      "author": {
        "name": "卡斯伯Casper",
        "avatarUrl": "/assets/user-author.jpg",
        "description": "10年經驗的前端工程師"
      }
    }
  },
  "/api/v1/courses/12345/comments": {
    "mockData": [
      {
        "commentId": "67890",
        "userId": "98765",
        "content": "這個課程很棒！",
        "createdAt": "2024-08-06T08:00:00Z"
      }
    ]
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**:
  - 使用 OAuth 2.0 或 JWT 進行用戶驗證。
  - 對敏感操作（如發表留言、刪除留言）進行權限檢查。

- **效能優化建議**:
  - 影片資源使用 CDN 加速。
  - 資料請求結果進行快取（如使用 Redis）。
  - 分頁載入留言，避免一次加載過多數據。

- **錯誤處理建議**:
  - 提供清晰的錯誤提示（如「課程未找到」、「留言內容無效」）。
  - 前端捕獲 API 錯誤並顯示友好信息。

- **快取策略建議**:
  - 使用 HTTP Cache-Control 標頭提高靜態資源（如圖片、CSS、JS）的加載速度。
  - 對課程詳細數據設置短期快取（如 5 分鐘），減少伺服器負載。
