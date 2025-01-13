```markdown
# 一對一講師預約頁面 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/tutor-list.html`
- **頁面用途**: 用戶可以尋找並預約一對一的程式講師課程。
- **主要功能**: 
  - 展示講師列表及其詳細資料。
  - 提供講師篩選、搜尋和排序功能。
  - 支援動態收藏講師功能。
  - 提供課程分類導航。
  - 用戶可跳轉至講師預約頁面。

---

## 2. 區塊分析

### 2.1 導覽列區塊 (Navbar)
- **用途**: 提供導航功能，連結至各主要頁面（如精選課程、一對一教學、課程客製化等）。
- **包含元素**: 搜尋框、導航按鈕、登入/註冊按鈕。
- **數據需求**: 無動態數據需求。
- **互動行為**: 
  - 搜尋框支援用戶輸入文字並觸發搜尋。
  - 導航按鈕可展開/收起選單。
- **相依性**: 無特別依賴。

### 2.2 英雄區塊 (Hero Section)
- **用途**: 提供頁面開頭的吸引性介紹，強調核心功能（尋找一對一講師）。
- **包含元素**: 文字標題、按鈕、講師頭像集合。
- **數據需求**: 
  - 講師數量動態數據（如 `100+`）。
- **互動行為**: 按下按鈕可跳轉至講師列表區塊。
- **相依性**: 無。

### 2.3 服務介紹區塊 (Service Introduction)
- **用途**: 說明一對一教學和程式碼檢視的服務內容。
- **包含元素**: 服務描述文字、圖片。
- **數據需求**: 靜態內容，無動態數據需求。
- **互動行為**: 點擊「點我前往訂閱」連結跳轉到訂閱方案頁面。
- **相依性**: 無。

### 2.4 分類區塊 (Category)
- **用途**: 提供課程分類篩選功能。
- **包含元素**: 動態分類按鈕（如 HTML & CSS, JavaScript 等）。
- **數據需求**:
  - 分類名稱清單。
- **互動行為**: 點擊分類按鈕過濾顯示符合分類的講師。
- **相依性**: 與講師列表相依。

### 2.5 講師列表區塊 (Tutor List)
- **用途**: 動態展示講師卡片，提供講師搜尋、排序和收藏功能。
- **包含元素**: 
  - 搜尋框、排序按鈕。
  - 講師卡片（包括講師名稱、專業、評分、標籤、價格等）。
- **數據需求**:
  - 講師資料（名稱、專業、評分、標籤、價格、收藏狀態等）。
  - 排序選項。
- **互動行為**:
  - 搜尋框觸發講師搜尋。
  - 點擊收藏按鈕更改收藏狀態。
  - 點擊「立即預約」跳轉至講師預約頁面。
- **相依性**: 與後端 API 相依。

### 2.6 分頁區塊 (Pagination)
- **用途**: 提供講師列表的分頁功能。
- **包含元素**: 分頁按鈕（上一頁、下一頁、頁碼）。
- **數據需求**:
  - 當前頁碼、總頁數。
- **互動行為**: 點擊按鈕切換分頁。
- **相依性**: 與講師列表及後端 API 相依。

---

## 3. API 規格

### 3.1 獲取講師列表 (Get Tutors)
```json
{
  "name": "Get Tutors",
  "endpoint": "/api/v1/tutors",
  "method": "GET",
  "description": "取得講師列表及相關資訊。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {
      "search": "string",
      "category": "string",
      "sort": "string",
      "page": "number",
      "limit": "number"
    },
    "body": {}
  },
  "response": {
    "data": [
      {
        "id": "string",
        "name": "string",
        "title": "string",
        "profileImage": "string",
        "tags": ["string"],
        "rating": "number",
        "pricePerHour": "number",
        "isFavorite": "boolean"
      }
    ],
    "pagination": {
      "currentPage": "number",
      "totalPages": "number",
      "totalItems": "number"
    },
    "message": "string"
  },
  "relatedBlocks": ["講師列表區塊"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未登入或驗證失敗。"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "伺服器內部錯誤。"
    }
  ]
}
```

### 3.2 收藏/取消收藏講師 (Toggle Favorite)
```json
{
  "name": "Toggle Favorite",
  "endpoint": "/api/v1/tutors/{id}/favorite",
  "method": "POST",
  "description": "收藏或取消收藏講師。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {
      "id": "string"
    },
    "query": {},
    "body": {
      "isFavorite": "boolean"
    }
  },
  "response": {
    "data": {
      "id": "string",
      "isFavorite": "boolean"
    },
    "message": "string"
  },
  "relatedBlocks": ["講師列表區塊"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未登入或驗證失敗。"
    },
    {
      "status": 404,
      "message": "Not Found",
      "description": "講師不存在。"
    }
  ]
}
```

---

## 4. Mock 數據結構
```json
{
  "/api/v1/tutors": {
    "mockData": {
      "data": [
        {
          "id": "1",
          "name": "卡斯伯 Casper",
          "title": "10年經驗的前端工程師",
          "profileImage": "/Coding-bit/assets/user-1-f526f231.png",
          "tags": ["HTML/CSS", "React"],
          "rating": 4.9,
          "pricePerHour": 250,
          "isFavorite": true
        },
        {
          "id": "2",
          "name": "米克老師",
          "title": "喜歡寫code的前端工程師",
          "profileImage": "/Coding-bit/assets/user-6-aff8550b.png",
          "tags": ["製作 RWD 網站", "Bootstrap"],
          "rating": 3.4,
          "pricePerHour": 100,
          "isFavorite": false
        }
      ],
      "pagination": {
        "currentPage": 1,
        "totalPages": 3,
        "totalItems": 15
      },
      "message": "Successfully retrieved tutors."
    }
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**:
  - 使用 JWT 驗證用戶身份。
  - 講師收藏功能需驗證用戶權限。
  - 避免暴露敏感數據，如用戶信息。

- **效能優化建議**:
  - 支援分頁和分類過濾以減少數據量。
  - 實施伺服器端快取以加速熱門講師數據查詢。

- **錯誤處理建議**:
  - 提供清晰的用戶錯誤提示（如「請登入後再操作收藏功能」）。
  - 捕獲伺服器錯誤並回傳統一錯誤格式。

- **快取策略建議**:
  - 靜態資源（如圖片和 CSS/JS 文件）應使用長快取時間。
  - 動態數據可考慮短時間快取以降低伺服器負載。
```