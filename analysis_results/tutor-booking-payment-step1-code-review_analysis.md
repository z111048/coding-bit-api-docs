```markdown
# 講師預約 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/tutor-booking-step1.html`
- **頁面用途**: 提供用戶預約講師並填寫相關資訊的介面
- **主要功能**:
  - 用戶填寫預約資訊（如講師、類型、時段等）
  - 填寫檢視程式碼的儲存庫 URL 與希望接受指導的項目
  - 顯示預約明細與價格
  - 支援折扣碼的輸入
  - 導向至付款頁面

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供全站導覽功能
- **包含元素**: 
  - 品牌 Logo
  - 搜尋欄
  - 導覽連結（精選課程、一對一教學、課程客製化、幫助中心）
  - 登入/註冊按鈕
- **數據需求**: 無直接數據需求，但可支援動態搜尋建議的 API
- **互動行為**:
  - 手機版支援展開/收起選單
  - 搜尋欄輸入觸發建議功能（若有支援）
- **相依性**: 頁面導航連結、搜尋相關 API

### 2.2 預約流程追蹤 (Step Tracking)
- **用途**: 提供用戶清晰的預約流程進度顯示
- **包含元素**: 步驟名稱與圖示
- **數據需求**: 當前步驟資訊（靜態表示）
- **互動行為**: 無互動行為
- **相依性**: 無

### 2.3 預約資訊表單 (Booking Form)
- **用途**: 讓用戶填寫預約相關資訊
- **包含元素**: 
  - 已填寫的靜態資訊（講師、類型、日期、時段）
  - 程式碼儲存庫 URL
  - 希望接受指導的項目
- **數據需求**:
  - 從後端獲取預設的預約資訊（講師、類型等）
  - 用戶輸入的程式碼儲存庫 URL 與指導項目
- **互動行為**: 
  - 用戶輸入程式碼 URL 與希望指導項目
  - 表單驗證（必填項目檢查）
- **相依性**: 後端 API 提供已預約資料

### 2.4 預約明細卡片 (Summary Card)
- **用途**: 顯示用戶的預約費用明細並支援折扣碼輸入
- **包含元素**: 
  - 小計、折扣、總計
  - 折扣碼輸入框
  - 確認付款按鈕
- **數據需求**:
  - 後端提供的價格資訊
  - 折扣碼驗證結果
- **互動行為**: 
  - 用戶輸入折扣碼並驗證
  - 點擊按鈕跳轉至付款頁面
- **相依性**: 價格計算 API、折扣碼驗證 API

### 2.5 頁尾 (Footer)
- **用途**: 提供站點資訊與快速連結
- **包含元素**: 
  - 聯絡方式
  - 導覽連結
  - 社群媒體圖示
- **數據需求**: 無直接數據需求
- **互動行為**: 無互動行為
- **相依性**: 無

## 3. API 規格

### 3.1 取得預約資訊 API
```json
{
  "name": "GetBookingDetails",
  "endpoint": "/api/v1/booking/details",
  "method": "GET",
  "description": "取得用戶的預約資訊",
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
      "tutor": "string",
      "bookingType": "string",
      "date": "string",
      "timeslot": "string",
      "price": "number",
      "discount": "number"
    },
    "message": "string"
  },
  "relatedBlocks": ["預約資訊表單", "預約明細卡片"],
  "errorResponses": [
    {
      "status": 404,
      "message": "Booking not found",
      "description": "找不到對應的預約資訊"
    },
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "用戶未通過驗證"
    }
  ]
}
```

### 3.2 折扣碼驗證 API
```json
{
  "name": "ValidateDiscountCode",
  "endpoint": "/api/v1/discount/validate",
  "method": "POST",
  "description": "驗證用戶輸入的折扣碼是否有效",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    },
    "params": {},
    "query": {},
    "body": {
      "discountCode": "string"
    }
  },
  "response": {
    "data": {
      "isValid": "boolean",
      "discountAmount": "number"
    },
    "message": "string"
  },
  "relatedBlocks": ["預約明細卡片"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid discount code",
      "description": "折扣碼無效或格式錯誤"
    }
  ]
}
```

## 4. Mock 數據結構
```json
{
  "/api/v1/booking/details": {
    "mockData": {
      "tutor": "卡斯伯 Casper",
      "bookingType": "程式碼檢視",
      "date": "2024/08/11",
      "timeslot": "10:00-11:00",
      "price": 250,
      "discount": 0
    }
  },
  "/api/v1/discount/validate": {
    "mockData": {
      "isValid": true,
      "discountAmount": 50
    }
  }
}
```

## 5. 注意事項
- **API 安全性考量**:
  - 所有 API 請求需進行使用者身份驗證（OAuth 或 JWT）
  - 避免敏感數據暴露
- **效能優化建議**:
  - 使用伺服器端快取來減少重複查詢
  - CDNs 用於靜態資源（如圖片、CSS、JS）
- **錯誤處理建議**:
  - 提供用戶友好的錯誤提示
  - 確保表單驗證的即時性（前端與後端雙向驗證）
- **快取策略建議**:
  - 預約資訊可使用短時間快取（如 5 分鐘），以減低伺服器查詢壓力
  - 折扣碼驗證結果應即時，不建議快取
```