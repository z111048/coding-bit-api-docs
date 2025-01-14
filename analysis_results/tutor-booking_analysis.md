# 卡斯柏 ｜ 預約講師 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: N/A
- **頁面用途**: 提供講師預約與相關資訊，讓用戶可以選擇課程、一對一教學或程式碼檢視的服務。
- **主要功能**: 
  - 顯示講師的個人資訊、教學風格、履歷、相關影片與推薦課程。
  - 提供時間表供用戶選擇預約時間。
  - 顯示學生評價。
  - 推薦其他講師。
  - 提供一對一教學與程式碼檢視的服務選項。

---

## 2. 區塊分析

### 2.1 導覽列 (Navbar)
- **用途**: 提供全站導航功能。
- **包含元素**: 搜尋框、精選課程、一對一教學、課程客製化、幫助中心、登入/註冊按鈕。
- **數據需求**: 無動態數據，靜態連結為主。
- **互動行為**: 
  - 手機版本展開與收起選單。
  - 搜尋框即時輸入。
- **相依性**: 無。

### 2.2 講師個人資訊
- **用途**: 展示講師個人檔案，包括照片、名稱、簡介以及技能標籤。
- **包含元素**: 講師照片、名稱、經驗描述、技能標籤。
- **數據需求**: 
  - 講師名稱、經驗描述、技能標籤 (動態數據)。
  - 圖片 URL。
- **互動行為**: 點擊技能標籤可篩選相關內容。
- **相依性**: 後端提供講師資訊 API。

### 2.3 講師影片清單
- **用途**: 提供關於講師的免費教學影片。
- **包含元素**: 影片標題、時長、觀看人數、評分。
- **數據需求**: 
  - 影片標題、時長、觀看次數、評分 (動態數據)。
  - 圖片 URL。
- **互動行為**: 用戶點擊影片後跳轉至影片詳情頁。
- **相依性**: 後端提供影片清單 API。

### 2.4 時間表
- **用途**: 提供用戶選擇可預約的時段。
- **包含元素**: 星期、日期、可用時段。
- **數據需求**: 
  - 日期與可用時段 (動態數據)。
- **互動行為**: 點擊時段確認預約。
- **相依性**: 後端提供時間表數據 API。

### 2.5 學生評價
- **用途**: 顯示學生對講師的評價。
- **包含元素**: 評分、評論數量、詳細評論、評分分佈。
- **數據需求**: 
  - 評分、評論數量、詳細評論 (動態數據)。
- **互動行為**: 點擊"更多"按鈕展開完整評價。
- **相依性**: 後端提供評價 API。

### 2.6 推薦講師
- **用途**: 推薦其他講師，方便用戶探索更多可能性。
- **包含元素**: 講師名稱、專長、每小時收費。
- **數據需求**: 
  - 講師名稱、專長、價格 (動態數據)。
  - 圖片 URL。
- **互動行為**: 點擊講師卡片跳轉至該講師頁面。
- **相依性**: 後端提供推薦講師 API。

---

## 3. API 規格

### 3.1 獲取講師資訊
```json
{
  "name": "GetTutorInfo",
  "endpoint": "/api/v1/tutors/{id}",
  "method": "GET",
  "description": "取得講師詳細資訊",
  "request": {
    "headers": {
      "Authorization": "Bearer {token}"
    },
    "params": {
      "id": "string"
    },
    "query": {},
    "body": {}
  },
  "response": {
    "data": {
      "id": "string",
      "name": "string",
      "description": "string",
      "skills": ["string"],
      "profileImageUrl": "string"
    },
    "message": "string"
  },
  "relatedBlocks": ["講師個人資訊"],
  "errorResponses": [
    {
      "status": 404,
      "message": "Tutor not found",
      "description": "無法找到對應的講師資料"
    },
    {
      "status": 401,
      "message": "Unauthorized",
      "description": "未授權的請求"
    }
  ]
}
```

### 3.2 獲取時間表
```json
{
  "name": "GetSchedule",
  "endpoint": "/api/v1/tutors/{id}/schedule",
  "method": "GET",
  "description": "取得講師可預約時間表",
  "request": {
    "headers": {
      "Authorization": "Bearer {token}"
    },
    "params": {
      "id": "string"
    },
    "query": {
      "startDate": "YYYY-MM-DD",
      "endDate": "YYYY-MM-DD"
    },
    "body": {}
  },
  "response": {
    "data": [
      {
        "date": "YYYY-MM-DD",
        "availableTimes": ["HH:mm"]
      }
    ],
    "message": "string"
  },
  "relatedBlocks": ["時間表"],
  "errorResponses": [
    {
      "status": 400,
      "message": "Invalid date range",
      "description": "日期範圍格式不正確"
    },
    {
      "status": 404,
      "message": "Schedule not found",
      "description": "無法找到對應的時間表"
    }
  ]
}
```

---

## 4. Mock 數據結構
### 4.1 獲取講師資訊
```json
{
  "/api/v1/tutors/123": {
    "mockData": {
      "id": "123",
      "name": "卡斯伯 Casper",
      "description": "10年經驗的前端工程師",
      "skills": ["HTML/CSS", "React", "網頁動畫"],
      "profileImageUrl": "/Coding-bit/assets/user-1-f526f231.png"
    }
  }
}
```

### 4.2 獲取時間表
```json
{
  "/api/v1/tutors/123/schedule": {
    "mockData": [
      {
        "date": "2024-08-01",
        "availableTimes": ["09:00", "11:00", "12:00", "13:00"]
      },
      {
        "date": "2024-08-02",
        "availableTimes": ["16:00", "17:00", "18:00"]
      }
    ]
  }
}
```

---

## 5. 注意事項
- **API 安全性考量**: 
  - 使用 JWT 驗證確保用戶身份。
  - 實現角色權限控制，避免未授權用戶訪問敏感數據。
- **效能優化建議**: 
  - 使用快取機制 (如 Redis) 儲存常用的講師資訊和時間表。
  - 前端圖片資源壓縮以加速頁面載入。
- **錯誤處理建議**: 
  - 提供詳細的錯誤訊息方便用戶理解錯誤原因。
  - 錯誤訊息需避免暴露內部系統細節。
- **快取策略建議**: 
  - 講師資訊與推薦講師的資料更新頻率低，適合使用短期快取。
  - 時間表資料應根據使用頻率動態設定快取時效。
