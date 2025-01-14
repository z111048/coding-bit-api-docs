import os
from pathlib import Path

def clean_markdown_files(directory_path):
    """清理指定目錄下所有 Markdown 文件的首尾 ```markdown 標記"""
    directory = Path(directory_path)
    
    # 找出所有 .md 文件
    md_files = list(directory.glob('**/*.md'))
    
    for file_path in md_files:
        print(f"處理文件: {file_path}")
        
        try:
            # 讀取文件內容
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 檢查並移除首尾的 ```markdown 標記
            if lines and '```markdown' in lines[0]:
                lines = lines[1:]
            if lines and '```' in lines[-1]:
                lines = lines[:-1]
            
            # 寫回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
                
            print(f"成功處理: {file_path}")
            
        except Exception as e:
            print(f"處理文件時發生錯誤 {file_path}: {str(e)}")

def main():
    # 輸入目錄路徑
    directory_path = input("請輸入包含 Markdown 文件的目錄路徑: ") or "analysis_results"
    
    # 確認目錄存在
    if not os.path.exists(directory_path):
        print("指定的目錄不存在！")
        return
    
    # 執行清理
    clean_markdown_files(directory_path)
    print("\n處理完成！")

if __name__ == "__main__":
    main()