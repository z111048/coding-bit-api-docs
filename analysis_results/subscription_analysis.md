# 訂閱方案頁面分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/subscription.html`
- **頁面用途**: 提供用戶選擇並購買訂閱方案（免費會員、基本會員、高級會員）。
- **主要功能**: 展示訂閱方案的詳細資訊（價格、功能），用戶可切換「月繳」和「年繳」方案，並進行訂閱操作。

---

## 2. 區塊分析

### 2.1 加載動畫（Loader）
- **用途**: 在頁面加載時顯示動畫，提升用戶體驗。
- **包含元素**: SVG 動畫 (圖案)。
- **數據需求**: 無需動態數據。
- **互動行為**: 無互動行為。
- **相依性**: 無。

### 2.2 導航欄（Navbar）
- **用途**: 提供網站導航，便於用戶訪問不同頁面。
- **包含元素**: 
  - 搜尋框
  - 導航連結（精選課程、一對一教學、課程客製化、幫助中心）
  - 登入/註冊按鈕
- **數據需求**: 無需動態數據，但登入狀態可影響按鈕顯示（登入/登出）。
- **互動行為**: 
  - 搜尋框輸入關鍵字。
  - 展開/收起導航欄（小螢幕）。
- **相依性**: 搜尋功能需要後端 API 支援。

### 2.3 訂閱方案區（Subscription Section）
- **用途**: 展示訂閱方案（免費會員、基本會員、高級會員）並提供訂閱操作。
- **包含元素**: 
  - 面包屑導航
  - 方案切換選項卡（「月繳」與「年繳」）
  - 各方案卡片（價格、功能列表、行動按鈕）
- **數據需求**:
  - 方案名稱、價格、功能描述。
  - 方案切換（「月繳」與「年繳」）需後端支援不同價格點。
- **互動行為**:
  - 切換「月繳」與「年繳」。
  - 點擊「立即註冊」或「立即訂閱」按鈕。
- **相依性**: 
  - 方案數據需從後端 API 獲取。
  - 訂閱按鈕需調用後端 API 完成訂閱。

### 2.4 頁尾（Footer）
- **用途**: 提供聯絡資訊與快捷連結。
- **包含元素**: 
  - 聯絡電話與營業時間
  - 網站連結（課程相關、幫助中心、訂閱方案選擇）
  - 社群媒體圖示
- **數據需求**: 無需動態數據。
- **互動行為**: 點擊外部連結。
- **相依性**: 無。

---

## 3. API 規格

### 3.1 獲取訂閱方案 API
```json
{
  "name": "取得訂閱方案",
  "endpoint": "/api/v1/subscription-options",
  "method": "GET",
  "description": "用於獲取訂閱方案的詳細資訊（包括名稱、價格、功能等）。",
  "request": {
    "headers": {
      "Content-Type": "application/json"
    },
    "params": {},
    "query": {
      "type": "string" // 可選值：monthly 或 annually，用於切換價格模式
    },
    "body": {}
  },
  "response": {
    "data": [
      {
        "id": "string",
        "name": "string", // 訂閱方案名稱
        "price": "number", // 價格
        "billingCycle": "string", // 計費週期（monthly 或 annually）
        "features": ["string"] // 功能列表
      }
    ],
    "message": "string"
  },
  "relatedBlocks": ["訂閱方案區"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid Request",
      "description": "當查詢參數無效時返回。"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "伺服器內部錯誤。"
    }
  ]
}
```

### 3.2 提交訂閱 API
```json
{
  "name": "提交訂閱",
  "endpoint": "/api/v1/subscribe",
  "method": "POST",
  "description": "用於提交用戶的訂閱請求。",
  "request": {
    "headers": {
      "Content-Type": "application/json",
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {},
    "body": {
      "userId": "string",
      "subscriptionId": "string", // 訂閱方案 ID
      "billingCycle": "string" // 計費週期
    }
  },
  "response": {
    "data": {
      "subscriptionId": "string",
      "status": "string" // 訂閱狀態（如 success 或 pending）
    },
    "message": "string"
  },
  "relatedBlocks": ["訂閱方案區"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "未登入或權限不足。"
    },
    {
      "status": 400,
      "message": "Invalid Request",
      "description": "當提交資訊有誤時返回。"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "伺服器內部錯誤。"
    }
  ]
}
```

---

## 4. Mock 數據結構
```json
{
  "/api/v1/subscription-options": {
    "mockData": [
      {
        "id": "free",
        "name": "免費會員",
        "price": 0,
        "billingCycle": "monthly",
        "features": [
          "只需註冊帳號，即可享有服務",
          "可觀看免費影片",
          "可參與影片討論區，與其他使用者交流"
        ]
      },
      {
        "id": "basic",
        "name": "基本會員",
        "price": 299,
        "billingCycle": "monthly",
        "features": [
          "不限次數、不限時長，觀看所有教學影片",
          "可預約一對一教學、程式碼檢視",
          "可成為老師，上傳教學影片，接受學生預約與客製化需求"
        ]
      },
      {
        "id": "premium",
        "name": "高級會員",
        "price": 499,
        "billingCycle": "monthly",
        "features": [
          "包含基本會員擁有的所有服務",
          "可發佈學習客製化需求"
        ]
      }
    ]
  }
}
```

---

## 5. 注意事項
### API 安全性考量
- **驗證**: 所有需要用戶身份的 API 必須包含 JWT 驗證。
- **授權**: 不同用戶角色應有不同權限（如免費會員無法存取付費內容）。
- **數據過濾**: 僅返回必要的訂閱方案資訊，避免洩漏不必要的內部數據。

### 效能優化建議
- **快取機制**: 訂閱方案為靜態資訊，可設置短期快取以減少伺服器負擔。
- **圖片優化**: 訂閱卡片中的圖片應使用壓縮後格式（如 WebP）。

### 錯誤處理建議
- **用戶端提示**: 當訂閱失敗時，應顯示清晰的錯誤提示（如網路錯誤、資料格式錯誤）。
- **後端日誌**: 紀錄錯誤請求供開發者排查。

### 快取策略建議
- **方案數據快取**: 訂閱方案的內容可設置為 24 小時快取，減少頻繁查詢。
- **CDN**: 使用 CDN 提供靜態資源（如圖片、樣式表）。

