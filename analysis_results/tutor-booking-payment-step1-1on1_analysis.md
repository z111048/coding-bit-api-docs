```markdown
# 講師預約頁面 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/tutor-booking.html`
- **頁面用途**: 用戶填寫並確認預約講師的相關資訊
- **主要功能**: 
  1. 顯示預約詳細信息（講師、類型、日期、時段）。
  2. 提供用戶填寫指導需求的輸入框。
  3. 計算並顯示預約的費用明細（小計、折扣、總計）。
  4. 提供折扣碼輸入功能。
  5. 支援桌面版與行動版的適配設計。

---

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供用戶快速導航到其他主要頁面。
- **包含元素**: Logo、搜尋欄、導航按鈕（精選課程、一對一教學、課程客製化、幫助中心）、登入/註冊按鈕。
- **數據需求**: 無直接數據需求。
- **互動行為**:
  - 導覽列的開關（在行動裝置上切換顯示/隱藏）。
  - 搜尋欄的輸入行為。
- **相依性**: 靜態元素，與其他區塊無直接數據依賴。

### 2.2 預約流程追蹤 (Step Tracking)
- **用途**: 指示用戶當前處於預約流程中的哪一步。
- **包含元素**: 流程步驟 (Step 1/3、Step 2/3、Step 3/3) 的名稱與描述。
- **數據需求**: 當前步驟的狀態（Highlight 樣式）。
- **互動行為**: 無互動行為。
- **相依性**: 前端靜態渲染。

### 2.3 預約資訊表單
- **用途**: 顯示並讓用戶確認預約的相關資訊。
- **包含元素**:
  - 預約講師名稱。
  - 預約類型。
  - 預約日期與時段。
  - 用戶輸入的指導需求。
- **數據需求**: 
  - 從伺服器獲取的預約詳細數據（講師名稱、類型、日期、時段）。
  - 用戶輸入的指導需求。
- **互動行為**: 用戶輸入需求內容。
- **相依性**: 
  - 須依賴伺服器返回的預約相關數據。
  - 提交數據至伺服器進一步處理。

### 2.4 預約明細 (費用計算區塊)
- **用途**: 計算並顯示預約的費用明細（小計、折扣、總計）。
- **包含元素**:
  - 費用小計、折扣、總計的金額顯示。
  - 折扣碼輸入框與提交按鈕。
  - 前往付款按鈕。
- **數據需求**:
  - 費用明細數據（小計、折扣、總計）。
  - 折扣碼驗證結果。
- **互動行為**:
  - 用戶輸入折扣碼並提交。
  - 點擊「前往付款」按鈕。
- **相依性**:
  - 從伺服器獲取費用明細數據。
  - 提交折扣碼驗證請求至伺服器。

### 2.5 行動版底部固定明細
- **用途**: 在行動版中提供固定的費用明細及付款按鈕。
- **包含元素**: 小計金額顯示、前往付款按鈕。
- **數據需求**: 費用小計數據。
- **互動行為**: 點擊「前往付款」按鈕。
- **相依性**: 與費用計算區塊共享數據。

### 2.6 頁腳 (Footer)
- **用途**: 提供網站基本資訊與社交媒體連結。
- **包含元素**: 聯絡電話、營業時間、導航連結。
- **數據需求**: 無直接數據需求。
- **互動行為**: 點擊連結跳轉。
- **相依性**: 靜態元素。

---

## 3. API 規格

### 3.1 獲取預約資訊
```json
{
  "name": "GetBookingInfo",
  "endpoint": "/api/v1/booking/info",
  "method": "GET",
  "description": "取得用戶的預約資訊",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {
      "bookingId": "string"
    },
    "query": {}
  },
  "response": {
    "data": {
      "tutor": "string",
      "bookingType": "string",
      "date": "string",
      "timeslot": "string",
      "subtotal": "number",
      "discount": "number",
      "total": "number"
    },
    "message": "string"
  },
  "relatedBlocks": ["預約資訊表單", "預約明細"],
  "errorResponses": [
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未登入，無法取得預約資訊"
    },
    {
      "status": 404,
      "message": "Booking not found",
      "description": "查無此預約 ID"
    }
  ]
}
```

### 3.2 提交折扣碼
```json
{
  "name": "ApplyDiscountCode",
  "endpoint": "/api/v1/discount/apply",
  "method": "POST",
  "description": "提交折扣碼並取得折扣後的費用資訊",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "body": {
      "discountCode": "string",
      "bookingId": "string"
    }
  },
  "response": {
    "data": {
      "discount": "number",
      "total": "number"
    },
    "message": "Discount applied successfully"
  },
  "relatedBlocks": ["預約明細"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid discount code",
      "description": "折扣碼無效或已過期"
    },
    {
      "status": 404,
      "message": "Booking not found",
      "description": "查無此預約 ID"
    }
  ]
}
```

---

## 4. Mock 數據結構

### 4.1 獲取預約資訊
```json
{
  "apiEndpoint": "/api/v1/booking/info",
  "mockData": {
    "data": {
      "tutor": "卡斯伯 Casper",
      "bookingType": "一對一教學",
      "date": "2024/08/11",
      "timeslot": "10:00-11:00",
      "subtotal": 250,
      "discount": 0,
      "total": 250
    },
    "message": "Booking info retrieved successfully"
  }
}
```

### 4.2 提交折扣碼
```json
{
  "apiEndpoint": "/api/v1/discount/apply",
  "mockData": {
    "data": {
      "discount": 50,
      "total": 200
    },
    "message": "Discount applied successfully"
  }
}
```

---

## 5. 注意事項
1. **API 安全性考量**:
   - 確保所有 API 請求需攜帶有效的 Authorization Token。
   - 防止越權存取（如用戶嘗試操作非本人預約的資料）。

2. **效能優化建議**:
   - 預約資訊可進行伺服器端快取，降低頻繁查詢的負擔。
   - 使用 CDN 儲存靜態資源（圖片、CSS、JS）。

3. **錯誤處理建議**:
   - 提供清楚的錯誤提示，如「預約資訊加載失敗，請稍後再試」。
   - 對折扣碼驗證失敗時顯示適當提示。

4. **快取策略建議**:
   - 預約明細卡片的數據可以設置短期快取（數分鐘即可）。
   - 靜態頁腳與導覽列內容可長期快取。
```