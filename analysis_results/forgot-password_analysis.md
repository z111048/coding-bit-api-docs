```markdown
# Coding∞bit 忘記密碼頁面分析報告

## 1. 頁面基本資訊
- **頁面 URL**: `/forgot-password`
- **頁面用途**: 此頁面供用戶在忘記密碼時，輸入電子信箱以接收重設密碼的驗證信。
- **主要功能**:
  - 提供電子信箱輸入欄位。
  - 發送重設密碼的驗證信。
  - 提供重新發送驗證信的選項。

## 2. 區塊分析

### 2.1 頁面標頭區塊
- **用途**: 顯示網站標誌，提供用戶品牌識別。
- **包含元素**:
  - 網站標誌 `<img>`。
  - 響應式圖片資源 `<picture>`。
- **數據需求**: 
  - 無動態數據需求，為靜態資源。
- **互動行為**: 點擊網站標誌後返回首頁。
- **相依性**: 與網站首頁的 URL 載入相關。

### 2.2 忘記密碼卡片區塊
- **用途**: 提供用戶輸入電子信箱的表單與操作按鈕。
- **包含元素**:
  - 標題 `<h1>`：提示用戶目前操作目的。
  - 說明文字 `<p>`：解釋操作流程。
  - 電子信箱輸入框 `<input>`。
  - 發送按鈕 `<button>`。
  - 錯誤提示或重新發送提示文字。
- **數據需求**:
  - 用戶輸入的電子信箱。
  - 按鈕狀態（如是否可以重新發送驗證信）。
- **互動行為**:
  - 用戶輸入電子信箱後，點擊按鈕觸發 API 請求，進行驗證信發送。
  - 若用戶未收到驗證信，可在 45 秒後重新發送。
- **相依性**: 
  - 依賴 API 進行驗證信發送的邏輯。
  - 錯誤或成功提示的顯示需依賴 API 回應結果。

### 2.3 重新發送驗證信區塊
- **用途**: 告知用戶驗證信可能延遲，並提供重新發送的選項。
- **包含元素**:
  - 提示文字 `<p>`。
  - 重新發送連結 `<a>`。
- **數據需求**:
  - 計時器數據（如剩餘秒數）。
- **互動行為**:
  - 點擊重新發送連結後重新發送驗證信。
- **相依性**: 與發送驗證信的 API 計時邏輯相關。

## 3. API 規格

### 3.1 發送驗證信 API
```json
{
  "name": "發送驗證信",
  "endpoint": "/api/v1/auth/send-reset-password",
  "method": "POST",
  "description": "用戶輸入電子信箱後，發送重設密碼的驗證信。",
  "request": {
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "email": "string"
    }
  },
  "response": {
    "data": {
      "success": "boolean"
    },
    "message": "string"
  },
  "relatedBlocks": ["忘記密碼卡片區塊", "重新發送驗證信區塊"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid email format",
      "description": "用戶輸入的電子信箱格式不正確。"
    },
    {
      "status": 404,
      "message": "Email not found",
      "description": "系統中未找到該電子信箱的用戶記錄。"
    },
    {
      "status": 429,
      "message": "Too many requests",
      "description": "用戶請求頻率過高，觸發速率限制。"
    }
  ]
}
```

### 3.2 重新發送驗證信 API
```json
{
  "name": "重新發送驗證信",
  "endpoint": "/api/v1/auth/resend-reset-password",
  "method": "POST",
  "description": "重新發送重設密碼的驗證信。",
  "request": {
    "headers": {
      "Content-Type": "application/json"
    },
    "body": {
      "email": "string"
    }
  },
  "response": {
    "data": {
      "success": "boolean"
    },
    "message": "string"
  },
  "relatedBlocks": ["重新發送驗證信區塊"],
  "errorResponses": [
    {
      "status": 429,
      "message": "Too many requests",
      "description": "用戶重新發送次數過多，觸發速率限制。"
    }
  ]
}
```

## 4. Mock 數據結構
```json
{
  "/api/v1/auth/send-reset-password": {
    "mockData": {
      "success": true,
      "message": "Verification email sent successfully."
    }
  },
  "/api/v1/auth/resend-reset-password": {
    "mockData": {
      "success": true,
      "message": "Verification email resent successfully."
    }
  }
}
```

## 5. 注意事項
- **API 安全性考量**:
  - 確保驗證信 API 使用身份驗證或防止惡意濫用。
  - 限制請求速率（Rate Limiting），避免 DDoS 攻擊。
  - 避免返回過多詳細錯誤訊息以防止信息洩漏。
- **效能優化建議**:
  - 使用伺服器快取以減少重複處理相同的請求。
  - 考慮 CDN 加速靜態資源載入。
- **錯誤處理建議**:
  - 提供明確的用戶提示，如電子信箱格式錯誤或系統繁忙。
  - 加入全域錯誤處理機制，避免未預期錯誤影響用戶體驗。
- **快取策略建議**:
  - 驗證信的動態請求應避免快取以確保即時性。
  - 靜態資源（如圖片、CSS、JS）可設定長期快取策略。
```