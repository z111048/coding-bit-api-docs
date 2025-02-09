# 客製化學習需求影片一覽 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/custom-course.html`
- **頁面用途**: 提供客製化學習需求的教學影片一覽。
- **主要功能**: 
  - 顯示客製化學習影片的清單。
  - 支援分類篩選與搜尋功能。
  - 提供排序選項（最熱門、最高評價、時間排序）。
  - 分頁導航。
  - 支援導覽連結至其他相關頁面（如精選課程、一對一教學、幫助中心等）。

---

## 2. 區塊分析

### 2.1 頁面頂部導航列
- **用途**: 提供全站導航功能。
- **包含元素**: 
  - 主選單（精選課程、一對一教學、課程客製化、幫助中心）。
  - 搜尋框（桌面與手機版）。
  - 登入/註冊按鈕。
- **數據需求**: 無需動態數據，但可根據登入狀態顯示不同的按鈕（登入/註冊或登出）。
- **互動行為**: 
  - 搜尋框輸入互動。
  - 導航選單開關行為（手機版）。
- **相依性**: 與登入狀態相關，需後端提供登入驗證資訊。

---

### 2.2 頁面標題區塊
- **用途**: 呈現當前頁面標題與簡介。
- **包含元素**: 
  - 頁面標題。
  - 簡介文字。
  - 麵包屑導航。
- **數據需求**: 無需動態數據。
- **互動行為**: 麵包屑導航連結至其他頁面。
- **相依性**: 與其他頁面的 URL 結構相關。

---

### 2.3 分類篩選區塊
- **用途**: 提供影片分類篩選功能。
- **包含元素**: 
  - 分類按鈕（如 HTML & CSS、JavaScript、Python 等）。
  - 左右箭頭（控制分類按鈕的滾動）。
- **數據需求**: 
  - 從後端獲取分類清單。
  - 每個分類按鈕需綁定對應的分類 ID。
- **互動行為**: 
  - 點擊分類按鈕時過濾顯示對應的影片。
  - 點擊箭頭時滾動分類。
- **相依性**: 與後端的分類數據同步。

---

### 2.4 搜尋與排序控制區塊
- **用途**: 支援影片的搜尋與排序功能。
- **包含元素**: 
  - 搜尋框。
  - 排序下拉選單（最熱門、最高評價、時間排序）。
- **數據需求**: 
  - 搜尋框需動態過濾影片清單。
  - 排序選單需影響影片排列順序。
- **互動行為**: 
  - 搜尋框輸入時觸發搜尋 API。
  - 選擇排序選項時重新加載影片清單。
- **相依性**: 與後端的影片數據與篩選邏輯相關。

---

### 2.5 影片列表區塊
- **用途**: 顯示客製化教學影片清單。
- **包含元素**: 
  - 單個影片卡片（封面圖片、標題、作者、影片時長、觀看人數、評分）。
- **數據需求**: 
  - 從後端獲取影片數據清單。
  - 每個影片需包含標題、封面圖片、作者名稱、時長、觀看次數、評分等資訊。
- **互動行為**: 點擊影片卡片跳轉至影片詳細頁面。
- **相依性**: 與後端的影片數據 API 相關。

---

### 2.6 分頁導航區塊
- **用途**: 支援分頁瀏覽功能。
- **包含元素**: 
  - 分頁按鈕（上一頁、下一頁、頁碼）。
- **數據需求**: 
  - 從後端獲取當前頁碼與總頁數資訊。
- **互動行為**: 點擊分頁按鈕時加載對應頁面的影片清單。
- **相依性**: 與後端的分頁 API 相關。

---

### 2.7 頁尾區塊
- **用途**: 提供網站聯繫資訊與次要導航。
- **包含元素**: 
  - 聯絡資訊（電話、營業時間）。
  - 次要導航連結（幫助中心、訂閱方案選擇）。
  - 社交媒體連結。
- **數據需求**: 無需動態數據。
- **互動行為**: 點擊連結跳轉至對應頁面或外部平台。
- **相依性**: 無。

---

## 3. API 規格

### 3.1 影片清單 API
```json
{
  "name": "影片清單 API",
  "endpoint": "/api/v1/videos",
  "method": "GET",
  "description": "獲取符合篩選條件的影片清單",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "query": {
      "category": "string",
      "search": "string",
      "sort": "string",
      "page": "number",
      "limit": "number"
    }
  },
  "response": {
    "data": [
      {
        "id": "string",
        "title": "string",
        "author": "string",
        "duration": "string",
        "views": "number",
        "rating": "number",
        "image": "string"
      }
    ],
    "pagination": {
      "currentPage": "number",
      "totalPages": "number"
    },
    "message": "string"
  },
  "relatedBlocks": ["影片列表區塊", "搜尋與排序控制區塊", "分頁導航區塊"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid query parameters",
      "description": "當查詢參數格式不正確時返回。"
    },
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "當用戶未登入或驗證失敗時返回。"
    },
    {
      "status": 500,
      "message": "Internal server error",
      "description": "伺服器內部錯誤。"
    }
  ]
}
```

---

## 4. Mock 數據結構
```json
{
  "/api/v1/videos": {
    "mockData": {
      "data": [
        {
          "id": "1",
          "title": "CSS 毛玻璃製作效果",
          "author": "卡斯伯 Casper",
          "duration": "8分16秒",
          "views": 1100,
          "rating": 4.0,
          "image": "https://example.com/image1.png"
        },
        {
          "id": "2",
          "title": "JavaScript 基本語法",
          "author": "林老師",
          "duration": "12分30秒",
          "views": 900,
          "rating": 4.5,
          "image": "https://example.com/image2.png"
        }
      ],
      "pagination": {
        "currentPage": 1,
        "totalPages": 3
      },
      "message": "Success"
    }
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**: 
  - 使用 OAuth 或 JWT 驗證。
  - 對敏感操作設定適當的權限控制。
- **效能優化建議**: 
  - 分頁與限制每頁數量（`limit`）。
  - 運用 CDN 儲存與快取圖片資源。
- **錯誤處理建議**: 
  - 提供清晰的錯誤訊息給前端。
  - 適當處理 API 超時與伺服器錯誤。
- **快取策略建議**: 
  - 對靜態資源（如圖片與 CSS）設置長時間快取。
  - 對 API 回應設置短時間快取以減少伺服器負擔。
