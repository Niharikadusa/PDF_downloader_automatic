from pythonimports import *

def check_file(filepath):
    return os.path.isfile(filepath)

def fileDataToDataframe(filename):
    _, ext = os.path.splitext(filename.lower())

    if ext == '.csv':
        df = pd.read_csv(filename)
    elif ext in ['.xls', '.xlsx']:
        df = pd.read_excel(filename)
    else:
        raise ValueError("Unsupported file type. Only .csv, .xls, and .xlsx supported.")

    if df.shape[1] < 3:
        raise ValueError("Input file must have at least 3 columns: ID, PDF URL 1, PDF URL 2")
    df = df.rename(columns={
        df.columns[0]: 'id',
        df.columns[1]: 'pdf_url_1',
        df.columns[2]: 'pdf_url_2'
    })
    url_cols = ['pdf_url_1', 'pdf_url_2']
    has_valid_url = False
    for col in url_cols:
        valid_urls = df[col].dropna().map(lambda x: str(x).strip().lower().startswith('http'))
        if valid_urls.any():
            has_valid_url = True
            break
    if not has_valid_url:
        raise ValueError("Neither URL column contains valid URLs. This is not the correct file.")
    return df

def download_pdf(row, output_folder,column_names):
    id=column_names[0]
    pdf_url_1=column_names[1]
    pdf_url_2=column_names[2]
    for url in [row.get(pdf_url_1), row.get(pdf_url_2)]:
        if pd.isna(url) or not str(url).strip():
            continue
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and 'pdf' in r.headers.get('Content-Type', '').lower():
                content = r.content

                if not content or len(content) < 100 or not content.startswith(b'%PDF'):
                    continue

                os.makedirs(output_folder, exist_ok=True)
                filename = url.split('/')[-1].split('?')[0]
                base, ext = os.path.splitext(filename)
                if not ext or ext.lower() != '.pdf':
                    filename = f"{row['id']}_{base}.pdf"
                else:
                    filename = f"{row['id']}_{base}{ext}"
                filepath = os.path.join(output_folder, filename)
                with open(filepath, 'wb') as f:
                    f.write(r.content)
                return (row.name, "Downloaded Successfully", filepath)
        except Exception as e:
            continue
    return (row.name, "Unable to download", "")

def check_Link(df):
    column_names=list(df.columns)
    df['status'] = ""
    df['filepath'] = ""
    df['downloded_date']=""
    output_folder = os.path.join(os.getcwd(), "Pdfs_" + date.today().strftime("%Y%m%d"))
    with ThreadPoolExecutor(max_workers=15) as executor:
        results = executor.map(lambda row: download_pdf(row, output_folder,column_names), [row for _, row in df.iterrows()])
    for idx, status, filepath in results:
        df.at[idx, 'status'] = status
        df.at[idx, 'filepath'] = filepath
        df.at[idx,'downloaded_date']=date.today()
    return df

def update_master(csv_file,MASTER_FILE):
    # Load master if exists
    if check_file(MASTER_FILE):
        df_master = pd.read_excel(MASTER_FILE)
    else:
        df_master = pd.DataFrame()

    df_new = fileDataToDataframe(csv_file)

    if not df_master.empty:
        downloaded_urls = set()
        for col in ['pdf_url_1', 'pdf_url_2']:
            downloaded_urls.update(df_master[df_master['status'] == 'Downloaded Successfully'][col].dropna().tolist())
        df_to_download = df_new[
            (~df_new['pdf_url_1'].isin(downloaded_urls)) &
            (~df_new['pdf_url_2'].isin(downloaded_urls))
        ].copy()
    else:
        df_to_download = df_new.copy()

    if df_to_download.empty:
        print("No new files to download.")
        return df_master

    df_downloaded = check_Link(df_to_download)

    if not df_master.empty:
        df_master_downloaded = df_master[df_master['status'] == 'Downloaded Successfully']
        df_combined = pd.concat([df_master_downloaded, df_downloaded], ignore_index=True)
    else:
        df_combined = df_downloaded
    df_combined = df_combined.drop_duplicates(subset='id')
    df_combined=df_combined.sort_values(by='id',ascending=True).reset_index(drop=True)
    df_combined.to_excel(MASTER_FILE, index=False)

    print(f"Master Excel updated: {MASTER_FILE}")
    return df_combined