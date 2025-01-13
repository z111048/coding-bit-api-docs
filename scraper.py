import requests
import os
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time

class CodingBitScraper:
    def __init__(self, base_url="https://ahmomoz.github.io/Coding-bit/"):
        self.base_url = base_url
        self.pages = [
            "index.html",
            "course-list.html",
            "course-list_customLearning.html",
            "course-list_freeTipShorts.html",
            "course-list_topicSeries.html",
            "custom-course.html",
            "forgot-password.html",
            "help-center.html",
            "login.html",
            "reset-password.html",
            "sign-up.html",
            "subscription-booking-normal.html",
            "subscription-booking-premium.html",
            "subscription-booking-success-normal.html",
            "subscription-booking-success-premium.html",
            "subscription-info-normal.html",
            "subscription-info-premium.html",
            "subscription.html",
            "test.html",
            "tutor-booking-payment-step1-1on1.html",
            "tutor-booking-payment-step1-code-review.html",
            "tutor-booking-payment-step2-1on1.html",
            "tutor-booking-payment-step2-code-review.html",
            "tutor-booking-payment-success-1on1.html",
            "tutor-booking-payment-success-code-review.html",
            "tutor-booking.html",
            "tutor-info.html",
            "tutor-list.html",
            "video-details.html"
        ]
        self.session = requests.Session()
        self.results = {}
        
    def get_page(self, page):
        """抓取單一頁面的HTML內容"""
        url = urljoin(self.base_url, page)
        try:
            response = self.session.get(url)
            response.raise_for_status()
            
            # 使用 BeautifulSoup 格式化 HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            formatted_html = soup.prettify()
            
            return {
                'url': url,
                'html': formatted_html,
                'status': response.status_code
            }
        except requests.RequestException as e:
            print(f"Error fetching {url}: {str(e)}")
            return {
                'url': url,
                'html': None,
                'status': getattr(e.response, 'status_code', None),
                'error': str(e)
            }

    def save_results(self, output_dir="scraped_pages"):
        """儲存抓取結果"""
        # 建立輸出目錄
        os.makedirs(output_dir, exist_ok=True)
        
        # 儲存每個頁面的HTML
        for page, result in self.results.items():
            if result['html']:
                # 儲存HTML檔案
                html_filename = os.path.join(output_dir, page)
                with open(html_filename, 'w', encoding='utf-8') as f:
                    f.write(result['html'])
        
        # 儲存抓取摘要
        summary = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'total_pages': len(self.pages),
            'successful_pages': sum(1 for r in self.results.values() if r['html']),
            'failed_pages': sum(1 for r in self.results.values() if not r['html']),
            'results': {
                page: {
                    'url': result['url'],
                    'status': result['status'],
                    'error': result.get('error')
                }
                for page, result in self.results.items()
            }
        }
        
        with open(os.path.join(output_dir, 'scraping_summary.json'), 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

    def scrape_all(self, max_workers=5):
        """使用多執行緒抓取所有頁面"""
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有頁面的抓取任務
            future_to_page = {
                executor.submit(self.get_page, page): page 
                for page in self.pages
            }
            
            # 收集結果
            for future in future_to_page:
                page = future_to_page[future]
                try:
                    self.results[page] = future.result()
                except Exception as e:
                    print(f"Error processing {page}: {str(e)}")
                    self.results[page] = {
                        'url': urljoin(self.base_url, page),
                        'html': None,
                        'status': None,
                        'error': str(e)
                    }

def main():
    # 建立爬蟲實例
    scraper = CodingBitScraper()
    
    # 執行爬蟲
    print("開始抓取網頁...")
    scraper.scrape_all()
    
    # 儲存結果
    print("儲存結果...")
    scraper.save_results()
    
    print("完成！檢查 scraped_pages 目錄查看結果。")

if __name__ == "__main__":
    main()