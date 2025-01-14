# Coding∞bit 課程需求一覽表 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: 無明確 URL，假設為 `/course-needs`
- **頁面用途**: 用於展示和管理課程需求，包括查看、篩選、排序、回應和新增課程需求。
- **主要功能**: 
  - 查看課程需求卡片
  - 搜尋與篩選課程需求
  - 新增學習需求
  - 回應課程需求
  - 查看課程需求詳細資訊（Modal 彈窗）

---

## 2. 區塊分析

### 2.1 頁首區塊（Header）
- **用途**: 提供導航與功能入口，包括搜尋功能、篩選功能、排序功能和返回首頁按鈕。
- **包含元素**: 搜尋框、篩選器、排序下拉選單、返回首頁按鈕。
- **數據需求**: 無動態數據，僅靜態功能描述。
- **互動行為**: 
  - 搜尋框支持即時搜尋課程需求。
  - 篩選器支持狀態篩選（已完成、已回應）。
  - 排序按鈕支持按時間遞增、遞減排序。
- **相依性**: 篩選和排序功能需與卡片數據同步更新。

### 2.2 課程需求卡片區塊
- **用途**: 展示所有課程需求的卡片列表。
- **包含元素**: 卡片標題、分類、內容摘要、回應數量、狀態標記。
- **數據需求**: 
  - 卡片基本資訊（如標題、內容、作者、分類等）
  - 回應數量和狀態標記
- **互動行為**: 
  - 點擊卡片可打開詳情 Modal。
  - 滑動支持（橫向滾動）。
- **相依性**: 
  - 依賴篩選器、搜尋框與排序選項。
  - 依賴後端提供課程需求數據。

### 2.3 詳情 Modal（課程需求詳情）
- **用途**: 顯示課程需求的完整資訊及回應。
- **包含元素**: 詳情標題、作者資訊、回應列表、新增回應表單。
- **數據需求**: 
  - 完整課程需求資訊（例如標題、內容、標籤、日期等）
  - 回應列表（回應內容、作者、時間、讚數等）
- **互動行為**: 
  - 新增回應表單提交後，更新回應列表。
  - 支援點擊讚按鈕。
- **相依性**: 需與後端 API 交互以提交回應或獲取更新數據。

### 2.4 新增學習需求 Modal
- **用途**: 提供用戶提交新課程需求的表單。
- **包含元素**: 表單（標題、類別、內容、標籤、照片連結）、照片預覽區。
- **數據需求**: 
  - 表單輸入值（標題、類別、內容、標籤、照片）
- **互動行為**: 
  - 實時更新照片預覽。
  - 表單提交後，新增課程需求並更新卡片列表。
- **相依性**: 提交後需與後端 API 交互，返回新增的需求數據。

### 2.5 頁尾區塊（Footer）
- **用途**: 顯示頁面結尾的宣傳內容，支持收起/展開操作。
- **包含元素**: 宣傳標題與副標題、切換按鈕。
- **數據需求**: 無動態數據，僅靜態標題描述。
- **互動行為**: 
  - 點擊切換按鈕控制 Footer 的顯示或隱藏。
- **相依性**: 無。

---

## 3. API 規格

### 3.1 獲取課程需求列表
```json
{
  "name": "GetCourseNeeds",
  "endpoint": "/api/v1/course-needs",
  "method": "GET",
  "description": "獲取所有課程需求列表",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "query": {
      "search": "string",
      "tags": ["string"],
      "status": "string",
      "sortBy": "string"
    }
  },
  "response": {
    "data": [
      {
        "id": "string",
        "category": "string",
        "responseCount": "number",
        "title": "string",
        "content": "string",
        "date": "string",
        "author": {
          "name": "string",
          "avatar": "string"
        },
        "status": "string",
        "tags": ["string"],
        "isCompleted": "boolean",
        "hasResponses": "boolean",
        "timestamp": "number",
        "searchKeywords": "string"
      }
    ],
    "message": "string"
  },
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未授權"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "服務端錯誤"
    }
  ]
}
```

### 3.2 新增課程需求
```json
{
  "name": "AddCourseNeed",
  "endpoint": "/api/v1/course-needs",
  "method": "POST",
  "description": "新增課程需求",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "body": {
      "title": "string",
      "category": "string",
      "content": "string",
      "tags": ["string"],
      "photos": ["string"]
    }
  },
  "response": {
    "data": {
      "id": "string",
      "category": "string",
      "responseCount": 0,
      "title": "string",
      "content": "string",
      "date": "string",
      "author": {
        "name": "string",
        "avatar": "string"
      },
      "status": "in-progress",
      "tags": ["string"],
      "isCompleted": false,
      "hasResponses": false,
      "timestamp": "number",
      "searchKeywords": "string"
    },
    "message": "string"
  },
  "errorResponses": [
    {
      "status": 400,
      "message": "Bad Request",
      "description": "請求參數錯誤"
    },
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未授權"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "服務端錯誤"
    }
  ]
}
```

---

## 4. Mock 數據結構

### Mock: 獲取課程需求列表
```json
{
  "/api/v1/course-needs": {
    "mockData": [
      {
        "id": "1",
        "category": "CSS",
        "responseCount": 15,
        "title": "CSS 毛玻璃製作效果",
        "content": "想知道CSS毛玻璃效果如何製作...",
        "date": "2024-10-01 09:15",
        "author": {
          "name": "阿麥",
          "avatar": "https://example.com/avatar.jpg"
        },
        "status": "in-progress",
        "tags": ["CSS3", "UI/UX", "視覺效果"],
        "isCompleted": false,
        "hasResponses": true,
        "timestamp": 1727827200000,
        "searchKeywords": "css css毛玻璃製作效果 css3 ui/ux 視覺效果"
      }
    ]
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**
  - 使用 JWT 驗證（Authorization Header）。
  - 避免透過 GET 傳遞敏感數據。
  - 僅限授權用戶訪問新增與更新功能。

- **效能優化建議**
  - 卡片列表支持分頁與懶加載功能。
  - 照片預覽區域應使用壓縮圖片格式（如 WebP）。
  - 預加載熱門課程需求的資料。

- **錯誤處理建議**
  - 為表單提交添加用戶友好的錯誤提示。
  - API 返回標準化的錯誤碼與訊息。

- **快取策略建議**
  - 使用瀏覽器快取（ETag 或 Last-Modified）。
  - 靜態資源（如圖片和腳本）應加強 CDN 支援。
