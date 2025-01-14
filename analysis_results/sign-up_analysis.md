# Coding∞bit 會員註冊頁面 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/sign-up.html` (假設)
- **頁面用途**: 用戶註冊頁面，提供用戶創建新帳號的功能。
- **主要功能**: 
  - 提供用戶輸入暱稱、電子信箱及密碼的表單。
  - 支援 Google 第三方帳號註冊功能。
  - 提供導向登入頁面的鏈結。

## 2. 區塊分析

### 2.1 導覽區塊
- **用途**: 顯示網站 Logo，提供返回首頁的功能。
- **包含元素**: 
  - 網站 Logo 圖片（含響應式設計）。
  - 鏈結到首頁 (`index.html`)。
- **數據需求**: 無動態數據需求。
- **互動行為**: 點擊 Logo 導向首頁。
- **相依性**: 靜態資源（Logo 圖片）。

### 2.2 用戶註冊表單
- **用途**: 用戶輸入註冊資料（暱稱、電子信箱、密碼）。
- **包含元素**: 
  - 輸入框（暱稱、電子信箱、密碼、確認密碼）。
  - 按鈕（註冊帳號、Google 註冊）。
  - 表單驗證提示。
- **數據需求**: 
  - 用戶輸入資料：`username`, `email`, `password`, `passwordConfirmation`。
- **互動行為**:
  - 點擊「註冊帳號」按鈕觸發註冊 API。
  - 點擊「使用 Google 註冊」按鈕觸發 Google OAuth 認證。
  - 錯誤提示（如表單驗證失敗或 API 返回錯誤）。
- **相依性**: 
  - 使用者驗證相關 API。
  - 表單驗證邏輯（前端）。
  - Google OAuth 第三方整合。

### 2.3 分隔線與第三方註冊
- **用途**: 提供其他註冊方式（Google）。
- **包含元素**: 
  - 分隔線與「OR」標籤。
  - Google 註冊按鈕。
- **數據需求**: 無，但需觸發 Google OAuth。
- **互動行為**: 點擊按鈕觸發 Google OAuth 流程。
- **相依性**: Google 認證 API。

### 2.4 登入引導
- **用途**: 提供鏈結導向登入頁面。
- **包含元素**: 
  - 提示文字：「已經是會員了？」。
  - 鏈結到登入頁面（`login.html`）。
- **數據需求**: 無。
- **互動行為**: 點擊鏈結導向登入頁面。
- **相依性**: 靜態鏈結。

## 3. API 規格

### 3.1 註冊用戶 API
```json
{
  "name": "註冊用戶",
  "endpoint": "/api/v1/users/register",
  "method": "POST",
  "description": "處理用戶註冊請求，創建新用戶。",
  "request": {
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "username": "string",
      "email": "string",
      "password": "string",
      "passwordConfirmation": "string"
    }
  },
  "response": {
    "data": {
      "userId": "string",
      "username": "string",
      "email": "string"
    },
    "message": "註冊成功"
  },
  "relatedBlocks": ["用戶註冊表單"],
  "errorResponses": [
    {
      "status": 400,
      "message": "輸入資料有誤",
      "description": "例如：表單欄位未填滿或格式錯誤。"
    },
    {
      "status": 409,
      "message": "電子信箱已被註冊",
      "description": "用戶使用已存在的電子信箱進行註冊。"
    },
    {
      "status": 500,
      "message": "伺服器錯誤",
      "description": "內部伺服器錯誤，請稍後再試。"
    }
  ]
}
```

### 3.2 Google OAuth 認證 API
```json
{
  "name": "Google OAuth 認證",
  "endpoint": "/api/v1/auth/google",
  "method": "GET",
  "description": "處理 Google 第三方帳號的認證請求。",
  "request": {
    "headers": {
      "Authorization": "Bearer <token>"
    }
  },
  "response": {
    "data": {
      "userId": "string",
      "username": "string",
      "email": "string",
      "googleId": "string"
    },
    "message": "登入成功"
  },
  "relatedBlocks": ["用戶註冊表單", "分隔線與第三方註冊"],
  "errorResponses": [
    {
      "status": 401,
      "message": "未授權",
      "description": "用戶未正確完成 Google 認證流程。"
    },
    {
      "status": 500,
      "message": "伺服器錯誤",
      "description": "內部伺服器錯誤，請稍後再試。"
    }
  ]
}
```

## 4. Mock 數據結構
### 4.1 註冊用戶 API Mock 數據
```json
{
  "/api/v1/users/register": {
    "mockData": {
      "userId": "abc123",
      "username": "testUser",
      "email": "testuser@example.com"
    }
  }
}
```

### 4.2 Google OAuth API Mock 數據
```json
{
  "/api/v1/auth/google": {
    "mockData": {
      "userId": "xyz789",
      "username": "googleUser",
      "email": "googleuser@example.com",
      "googleId": "GOOGLE12345"
    }
  }
}
```

## 5. 注意事項
- **API 安全性考量**:
  - 使用 HTTPS 確保傳輸安全。
  - 密碼應在後端進行加密存儲（如採用 bcrypt）。
  - 使用 Google OAuth 時，需正確處理 Token 驗證及過期問題。
- **效能優化建議**:
  - 為靜態資源（如圖片、CSS、JS）設置快取策略。
  - 減少 API 回應時間，確保高效處理。
- **錯誤處理建議**:
  - 在前端提供即時表單驗證以減少用戶錯誤。
  - 顯示清楚的錯誤提示，讓用戶知道如何修正。
- **快取策略建議**:
  - 對於靜態資源（Logo、Google 按鈕圖示）使用長效快取。
  - API 回應可根據需求設置短期快取，但需注意即時性資料不應快取。
