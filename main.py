import os
from weread2notion import sync  # 根据实际模块名调整

def main():
    # 获取环境变量
    wr_token = os.getenv('WR_TOKEN')
    notion_token = os.getenv('NOTION_TOKEN')
    database_id = os.getenv('DATABASE_ID')
    
    if not all([wr_token, notion_token, database_id]):
        print("❌ 缺少必要的环境变量")
        return
    
    print("🚀 开始同步微信读书到 Notion...")
    
    try:
        # 调用同步函数
        sync.sync_books(wr_token, notion_token, database_id)
        print("✅ 同步完成")
    except Exception as e:
        print(f"❌ 同步失败: {str(e)}")
        raise

if __name__ == "__main__":
    main()
