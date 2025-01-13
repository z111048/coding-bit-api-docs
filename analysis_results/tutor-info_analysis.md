```markdown
# 講師介紹 ｜ 卡斯伯 Casper 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: 無（需補充具體 URL）
- **頁面用途**: 提供用戶瀏覽講師「卡斯伯 Casper」的個人介紹、專業背景與課程資訊。
- **主要功能**:
  - 展示講師基本資訊（頭像、背景簡介、技能標籤）。
  - 提供講師提供的課程類型分類（主題式課程、客製化需求、技術短影片）。
  - 顯示課程詳細資訊（標題、講師、時長、購買人數、評分）。
  - 支援頁面互動（回到頂部按鈕、展開更多內容、導航選單切換）。

---

## 2. 區塊分析

### 2.1 頁面導航欄（Navbar）
- **用途**: 提供主要網站導覽功能。
- **包含元素**: 搜尋框、課程連結、用戶登入／註冊按鈕。
- **數據需求**:
  - 搜尋框：需要連接課程搜尋 API。
  - 導航連結：靜態頁面 URL。
- **互動行為**: 
  - 手機版切換選單按鈕（開啟／關閉）。
  - 搜尋框支援輸入查詢。
- **相依性**: 與課程搜尋 API 相關。

### 2.2 講師資訊區塊
- **用途**: 展示講師的個人信息及專業背景。
- **包含元素**: 頭像、講師簡介、技能標籤、社交媒體圖標。
- **數據需求**:
  - 講師名稱、簡介、技能標籤等靜態內容。
  - 社交媒體連結。
- **互動行為**: 
  - 點擊技能標籤可能觸發相關課程篩選。
  - 點擊社交媒體圖標跳轉外部連結。
- **相依性**: 靜態數據，無外部 API 相依性。

### 2.3 課程分類選單與顯示區
- **用途**: 提供課程分類篩選（主題式課程、客製化需求、技術短影片）。
- **包含元素**: 標籤切換按鈕、課程卡片。
- **數據需求**:
  - API 提供的課程數據（課程名稱、講師、時長、購買人數、評分）。
- **互動行為**:
  - 點擊分類切換顯示不同類別課程。
  - 點擊課程卡片跳轉課程詳情頁。
- **相依性**: 與課程數據 API 相關。

### 2.4 頁面底部區塊（Footer）
- **用途**: 提供聯絡資訊與次要導覽功能。
- **包含元素**: 聯絡電話、營業時間、靜態連結、社交媒體按鈕。
- **數據需求**:
  - 聯絡資訊為靜態內容。
  - 社交媒體按鈕跳轉連結。
- **互動行為**: 點擊按鈕跳轉外部連結。
- **相依性**: 靜態數據，無外部 API 相依性。

---

## 3. API 規格

### 3.1 課程列表 API
```json
{
  "name": "課程列表 API",
  "endpoint": "/api/v1/courses",
  "method": "GET",
  "description": "提供課程的詳細資料，包括分類、名稱、講師、時長、購買人數與評分。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {
      "category": "string (optional)", 
      "limit": "number (optional)"
    },
    "body": null
  },
  "response": {
    "data": [
      {
        "id": "string",
        "category": "string",
        "courseName": "string",
        "teacher": "string",
        "totalDuration": "string",
        "purchaseCount": "number",
        "star": "number",
        "img": "string (URL)"
      }
    ],
    "message": "string"
  },
  "relatedBlocks": ["課程分類選單與顯示區"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未登入或 token 無效。"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "伺服器發生錯誤。"
    }
  ]
}
```

### 3.2 搜尋課程 API
```json
{
  "name": "搜尋課程 API",
  "endpoint": "/api/v1/search",
  "method": "GET",
  "description": "根據用戶輸入搜尋課程。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {
      "keyword": "string"
    },
    "body": null
  },
  "response": {
    "data": [
      {
        "id": "string",
        "courseName": "string",
        "teacher": "string",
        "img": "string (URL)"
      }
    ],
    "message": "string"
  },
  "relatedBlocks": ["頁面導航欄"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Bad Request",
      "description": "請求參數有誤，缺少 keyword。"
    },
    {
      "status": 404,
      "message": "Not Found",
      "description": "未找到符合條件的課程。"
    }
  ]
}
```

---

## 4. Mock 數據結構
```json
{
  "apiEndpoint": "/api/v1/courses",
  "mockData": [
    {
      "id": "1",
      "category": "主題式課程影片",
      "courseName": "進階 React 開發",
      "teacher": "卡斯伯 Casper",
      "totalDuration": "4 小時",
      "purchaseCount": 120,
      "star": 4.9,
      "img": "course-react.jpg"
    },
    {
      "id": "2",
      "category": "客製化需求影片",
      "courseName": "HTML/CSS 基礎",
      "teacher": "卡斯伯 Casper",
      "totalDuration": "3 小時",
      "purchaseCount": 85,
      "star": 4.8,
      "img": "course-html-css.jpg"
    }
  ]
}
```

---

## 5. 注意事項
- **API 安全性考量**:
  - 使用 Authorization Header 搭配 Bearer Token 驗證用戶身份。
  - 僅允許 HTTPS 請求。
- **效能優化建議**:
  - 提供分頁與限制回傳數量（`limit`）。
  - 使用 CDN 儲存靜態資源（如課程圖片）。
- **錯誤處理建議**:
  - 提供友善的錯誤訊息，提示用戶操作。
  - 確保伺服器錯誤（500）不洩露內部細節。
- **快取策略建議**:
  - 針對課程列表 API 實施快取，減少頻繁查詢。
  - 使用 ETag 或 Last-Modified Header 標記版本。
```