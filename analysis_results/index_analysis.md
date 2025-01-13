```markdown
# Coding∞bit ｜ 首頁 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/Coding-bit/index.html`
- **頁面用途**: 提供用戶關於程式學習平台的概覽，展示平台功能與服務，吸引用戶註冊或訂閱會員。
- **主要功能**:
  - 精選課程瀏覽
  - 一對一教學預約
  - 課程客製化需求提交
  - 訂閱會員方案介紹
  - 吸引使用者轉換（註冊會員或訂閱付費方案）

---

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供全站導航，包含課程列表、一對一教學、課程客製化等主要功能。
- **包含元素**:
  - 平台 Logo
  - 導覽連結（精選課程、一對一教學、課程客製化）
  - 搜尋功能
  - 註冊/登入按鈕
- **數據需求**:
  - 使用者登入狀態（顯示不同按鈕或訊息）
- **互動行為**:
  - 點擊連結導向相應頁面
  - 搜尋框輸入文字後觸發搜尋
- **相依性**: 與用戶驗證 API 相關。

---

### 2.2 首頁橫幅 (Hero Banner)
- **用途**: 吸引用戶注意，強調平台賣點（量身訂製課程、一對一教學）。
- **包含元素**:
  - 輪播圖片
  - 主要標題與描述
  - 行動按鈕（CTA）
- **數據需求**:
  - 輪播內容（圖片、標題、描述、CTA 按鈕連結）
- **互動行為**: 
  - 點擊 CTA 按鈕跳轉至相應頁面
  - 輪播自動切換或用戶手動切換
- **相依性**: 靜態內容，無動態數據依賴。

---

### 2.3 精選課程區塊
- **用途**: 展示課程卡片，吸引用戶查看更多課程。
- **包含元素**:
  - 課程圖片
  - 課程名稱
  - 講師名稱
  - 總時長、購買次數、評分
  - 查看更多按鈕
- **數據需求**:
  - 課程清單（名稱、圖片、講師、時長、購買次數、評分）
- **互動行為**:
  - 點擊課程卡片跳轉至課程詳情頁
  - 點擊「了解更多」查看完整課程清單
- **相依性**: 與課程 API 相關。

---

### 2.4 訂閱方案區塊
- **用途**: 介紹免費、基本、高級會員方案，吸引用戶訂閱。
- **包含元素**:
  - 方案名稱與描述
  - 價格
  - 服務內容
  - 訂閱按鈕
- **數據需求**:
  - 會員方案的詳細資訊
- **互動行為**:
  - 點擊訂閱按鈕跳轉至訂閱詳情頁
- **相依性**: 與會員方案 API 相關。

---

### 2.5 預約一對一教學流程
- **用途**: 解釋如何進行一對一教學預約。
- **包含元素**:
  - 步驟圖示與文字描述
- **數據需求**: 靜態內容，無動態需求。
- **互動行為**: 無特殊互動行為。
- **相依性**: 無。

---

## 3. API 規格

### 3.1 獲取課程清單
```json
{
  "name": "GetCourseList",
  "endpoint": "/api/v1/courses",
  "method": "GET",
  "description": "取得課程列表",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "query": {
      "page": "number",
      "limit": "number",
      "keyword": "string"
    }
  },
  "response": {
    "data": [
      {
        "courseId": "string",
        "courseName": "string",
        "img": "string",
        "teacher": "string",
        "totalDuration": "string",
        "purchaseCount": "number",
        "star": "number"
      }
    ],
    "message": "string"
  },
  "relatedBlocks": ["精選課程區塊"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "未登入或 Token 無效"
    },
    {
      "status": 500,
      "message": "Internal Server Error",
      "description": "伺服器錯誤"
    }
  ]
}
```

### 3.2 訂閱會員方案
```json
{
  "name": "SubscribePlan",
  "endpoint": "/api/v1/subscription",
  "method": "POST",
  "description": "訂閱會員方案",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "body": {
      "planId": "string",
      "paymentToken": "string"
    }
  },
  "response": {
    "data": {
      "subscriptionId": "string",
      "status": "string"
    },
    "message": "string"
  },
  "relatedBlocks": ["訂閱方案區塊"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "未登入或 Token 無效"
    },
    {
      "status": 400,
      "message": "Bad Request",
      "description": "訂閱資訊有誤"
    }
  ]
}
```

---

## 4. Mock 數據結構
### 精選課程
```json
{
  "/api/v1/courses": {
    "mockData": [
      {
        "courseId": "course-001",
        "courseName": "JavaScript 基礎課程",
        "img": "course-js.png",
        "teacher": "John Doe",
        "totalDuration": "8 小時",
        "purchaseCount": 150,
        "star": 4.8
      },
      {
        "courseId": "course-002",
        "courseName": "Python 資料科學入門",
        "img": "course-python.png",
        "teacher": "Jane Smith",
        "totalDuration": "10 小時",
        "purchaseCount": 200,
        "star": 4.9
      }
    ]
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**:
  - 所有 API 請求需通過 JWT 驗證
  - 敏感數據如會員訂閱交易需使用 HTTPS 加密
- **效能優化建議**:
  - 使用伺服器端快取（如 Redis）加速熱門課程查詢
  - 針對輪播圖片等靜態資源實施 CDN 加速
- **錯誤處理建議**:
  - 用戶端需顯示友好的錯誤訊息，例如「伺服器繁忙，請稍後再試」
  - 網頁需處理 API 請求超時情況
- **快取策略建議**:
  - 精選課程與訂閱方案的靜態內容可快取 1 小時
  - 動態數據如用戶訂閱狀態應即時更新
```