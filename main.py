from pythonimports import *
from utils import *


MASTER_FILE = 'C:/Niharika/PDF_downloader_automatic/PDF_downloads_Master_status.xlsx'

def main():
    try:
        csv_file = input("Enter the path to your CSV file with PDF link: ").strip()
        if not check_file(csv_file):
            print(f"File not found: {csv_file}")
            return
        update_master(csv_file,MASTER_FILE)
    except Exception as e:
        print("please see the error : " ,e)

if __name__ == "__main__":
    main()
