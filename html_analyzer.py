import os
import json
from pathlib import Path
import time
from typing import Dict, List, Optional
from openai import OpenAI
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

class HTMLAnalyzer:
    def __init__(self, api_key: str, input_dir: str = "scraped_pages", output_dir: str = "analysis_results"):
        self.client = OpenAI(api_key=api_key)
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.system_prompt = '''You are an experienced full-stack developer specializing in web development and API design. Analyze the provided HTML content and generate a comprehensive analysis report following these aspects:

1. Page Information
2. Block Analysis
3. API Specifications
4. Mock Data Structure

Focus on:
- Identifying all dynamic data requirements
- Data relationships and dependencies
- RESTful API design patterns
- Practical mock data examples
- Error handling mechanisms
- Performance considerations
- Security concerns

When analyzing components:
- Identify reusable components
- Note data dependencies
- Consider user interactions
- Evaluate loading states
- Account for error states

For API design:
- Follow RESTful principles
- Include proper error responses
- Consider rate limiting
- Plan for scalability
- Include authentication requirements

Please provide the analysis in Traditional Chinese (zh-tw) using the following markdown format:

```markdown
# {頁面名稱} 分析報告

## 1. 頁面基本資訊
- **頁面 URL**: {url}
- **頁面用途**: {description}
- **主要功能**: {main functions}

## 2. 區塊分析

### 2.1 {區塊名稱}
- **用途**: {purpose}
- **包含元素**: {elements}
- **數據需求**: {data requirements}
- **互動行為**: {interactions}
- **相依性**: {dependencies}

## 3. API 規格

### 3.1 {API 名稱}
```json
{
  "name": "API名稱",
  "endpoint": "/api/v1/...",
  "method": "GET/POST/PUT/DELETE",
  "description": "API用途說明",
  "request": {
    "headers": {},
    "params": {},
    "query": {},
    "body": {}
  },
  "response": {
    "data": {},
    "message": "string"
  },
  "relatedBlocks": ["區塊ID"],
  "errorResponses": [
    {
      "status": "number",
      "message": "string",
      "description": "string"
    }
  ]
}
```

## 4. Mock 數據結構
```json
{
  "apiEndpoint": {
    "mockData": {}
  }
}
```

## 5. 注意事項
- API 安全性考量
- 效能優化建議
- 錯誤處理建議
- 快取策略建議
```

Analyze the following HTML content and provide a detailed report:
'''

    def setup_directories(self):
        """建立必要的目錄"""
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def read_html_file(self, file_path: Path) -> Optional[str]:
        """讀取 HTML 檔案內容"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
            return None

    def analyze_html(self, html_content: str, page_name: str) -> Optional[str]:
        """使用 OpenAI GPT-4 分析 HTML 內容"""
        try:
            response = self.client.chat.completions.create(
                model="chatgpt-4o-latest",
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": html_content
                    }
                ],
                temperature=0.7,
                max_tokens=16384
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error analyzing {page_name}: {str(e)}")
            return None

    def save_analysis(self, analysis: str, page_name: str):
        """儲存分析結果"""
        try:
            output_file = self.output_dir / f"{page_name}_analysis.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(analysis)
            print(f"Analysis saved: {output_file}")
        except Exception as e:
            print(f"Error saving analysis for {page_name}: {str(e)}")

    def analyze_all_pages(self):
        """分析所有 HTML 頁面"""
        self.setup_directories()
        
        # 取得所有 HTML 檔案
        html_files = list(self.input_dir.glob('*.html'))
        total_files = len(html_files)
        
        print(f"Found {total_files} HTML files to analyze")
        
        for i, html_file in enumerate(html_files, 1):
            print(f"\nProcessing {i}/{total_files}: {html_file.name}")
            
            # 讀取 HTML 內容
            html_content = self.read_html_file(html_file)
            if not html_content:
                continue
                
            # 分析 HTML
            print("Analyzing...")
            analysis = self.analyze_html(html_content, html_file.stem)
            if not analysis:
                continue
                
            # 儲存分析結果
            self.save_analysis(analysis, html_file.stem)
            
            # API 請求限制處理
            if i < total_files:
                print("Waiting 20 seconds before next analysis...")
                time.sleep(20)

def main():
    # 設定 OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("請在 .env 文件中設定 OPENAI_API_KEY")
    
    # 設定輸入輸出目錄
    input_dir = input("請輸入HTML檔案目錄 (預設: scraped_pages): ") or "scraped_pages"
    output_dir = input("請輸入分析結果輸出目錄 (預設: analysis_results): ") or "analysis_results"
    
    # 建立分析器實例
    analyzer = HTMLAnalyzer(api_key, input_dir, output_dir)
    
    # 執行分析
    print("\n開始分析...")
    analyzer.analyze_all_pages()
    print("\n分析完成！請查看輸出目錄中的結果。")

if __name__ == "__main__":
    main()