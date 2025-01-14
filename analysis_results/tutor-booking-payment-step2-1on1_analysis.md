# 講師預約頁面 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: https://example.com/tutor-booking.html
- **頁面用途**: 用戶可在此頁面進行講師預約，填寫個人資訊並完成付款。
- **主要功能**:
  - 步驟追蹤 (進度條)
  - 預約人資訊填寫
  - 付款方式選擇與填寫
  - 預約明細檢視與確認
  - 提交付款

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供全站導覽功能，允許用戶快速跳轉至其他頁面。
- **包含元素**: Logo、搜尋框、導航連結、登入/註冊按鈕。
- **數據需求**: 無動態數據需求，搜尋框可能需要與後端 API 整合以提供即時建議。
- **互動行為**: 
  - 搜尋框輸入觸發建議查詢。
  - 手機版的導覽列展開/收起功能。
- **相依性**: 搜尋功能需要整合課程相關的 API。

### 2.2 預約步驟追蹤 (Step Tracking)
- **用途**: 引導用戶完成預約流程，顯示目前進度。
- **包含元素**: 三個步驟圖示與描述。
- **數據需求**: 無，屬於靜態內容。
- **互動行為**: 進入不同步驟時可能需改變樣式或高亮當前步驟。
- **相依性**: 需與頁面狀態同步。

### 2.3 預約人資訊表單
- **用途**: 收集用戶的基本資訊如電子信箱、姓名、密碼。
- **包含元素**: 表單字段 (電子信箱、姓名、密碼)、記住我的資訊選項。
- **數據需求**: 用戶輸入的個人資料。
- **互動行為**: 
  - 欄位驗證 (例如：檢查電子信箱格式)。
  - 提交時將數據傳送至後端。
- **相依性**: 表單提交需與後端 API 整合。

### 2.4 付款方式選擇
- **用途**: 用戶填寫信用卡資訊以完成付款。
- **包含元素**: 信用卡號、有效日期、CVC、記住卡片資訊選項。
- **數據需求**: 用戶輸入的信用卡資訊。
- **互動行為**: 
  - 欄位驗證 (例如：檢查信用卡號格式)。
  - 提交時將數據加密後傳送至後端。
- **相依性**: 需整合付款 API。

### 2.5 預約明細
- **用途**: 顯示用戶的預約內容與總價。
- **包含元素**: 小計、折扣、總計。
- **數據需求**: 預約明細數據由後端提供。
- **互動行為**: 
  - 動態顯示折扣或價格變化。
  - 點擊「確定付款」按鈕提交付款。
- **相依性**: 與後端 API 整合以獲取最新數據。

### 2.6 手機版明細卡片
- **用途**: 手機用戶查看預約明細和付款按鈕。
- **包含元素**: 小計、總計、付款按鈕。
- **數據需求**: 與電腦版明細一致。
- **互動行為**: 點擊付款按鈕觸發付款流程。
- **相依性**: 與後端 API 整合。

## 3. API 規格

### 3.1 取得預約明細 API
```json
{
  "name": "取得預約明細",
  "endpoint": "/api/v1/booking/details",
  "method": "GET",
  "description": "獲取預約明細數據。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {
      "bookingId": "string"
    },
    "query": {},
    "body": {}
  },
  "response": {
    "data": {
      "subtotal": 250,
      "discount": 0,
      "total": 250
    },
    "message": "取得成功"
  },
  "relatedBlocks": ["預約明細", "手機版明細卡片"],
  "errorResponses": [
    {
      "status": 401,
      "message": "未授權",
      "description": "用戶未登入或權限不足。"
    },
    {
      "status": 404,
      "message": "未找到",
      "description": "無法找到對應的預約明細。"
    }
  ]
}
```

### 3.2 提交付款 API
```json
{
  "name": "提交付款",
  "endpoint": "/api/v1/booking/payment",
  "method": "POST",
  "description": "提交用戶的付款資訊。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {},
    "body": {
      "email": "string",
      "name": "string",
      "password": "string",
      "creditCard": {
        "number": "string",
        "expiration": "string",
        "cvc": "string"
      },
      "rememberCard": "boolean"
    }
  },
  "response": {
    "data": {
      "paymentStatus": "success",
      "bookingId": "string"
    },
    "message": "付款成功"
  },
  "relatedBlocks": ["付款方式", "預約明細"],
  "errorResponses": [
    {
      "status": 400,
      "message": "付款失敗",
      "description": "信用卡資訊錯誤或餘額不足。"
    },
    {
      "status": 500,
      "message": "伺服器錯誤",
      "description": "處理付款時發生伺服器錯誤。"
    }
  ]
}
```

## 4. Mock 數據結構
```json
{
  "/api/v1/booking/details": {
    "mockData": {
      "subtotal": 250,
      "discount": 0,
      "total": 250
    }
  },
  "/api/v1/booking/payment": {
    "mockData": {
      "paymentStatus": "success",
      "bookingId": "B123456789"
    }
  }
}
```

## 5. 注意事項
- **API 安全性考量**:
  - 使用 HTTPS 確保數據傳輸安全。
  - 信用卡資訊需加密傳輸，並避免存儲於服務器上。
  - 採用 OAuth 或 JWT 驗證機制保護 API。
- **效能優化建議**:
  - 使用 CDN 儲存靜態資源（如圖片與 CSS）。
  - 預約明細數據可使用快取機制，減少後端查詢。
- **錯誤處理建議**:
  - 前端需即時提示用戶輸入錯誤（例如信用卡號格式不正確）。
  - 後端返回錯誤訊息時需提供具體描述以便調試。
- **快取策略建議**:
  - 預約明細與價格數據應設定短期快取。
  - 靜態資源（如圖標與樣式）可設定長期快取。
