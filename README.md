# PDF_Downloader

PDF Downloader is a small tool to download pdf files from the URLs in CSV Files.
The Example CSV file is attached in the GIthub folder.

Along with CSV,Readme there are also 3 more files attcahed.
The Tool has three programming files,
1. pythonimports.py(where all the package to be imported are written)
2. utils.py(where all python function are written)
3. main.py(when run the tool rns)

Requirements for the tool to run.
1. Install python from https://www.python.org/downloads/
2. Install VScode(optional). https://code.visualstudio.com/download
3. Download the files from github.
5. The CSV file should be in the same folder as the programming files.
6. The csv file should have 3 columns (id,URl1, URl2)


**Execution in VS code**


First you need to run requirements.txt file as given below in vscode .
--- pip install -r requirements.txt

<img width="423" alt="Screenshot 2025-05-23 140943" src="https://github.com/user-attachments/assets/c15c7970-ae73-4ea5-91f6-b66527bc91c9" />


After all the requirements are installed you need to run main file for tool to work

1. The user must run a main.py file
  
eg: c:/Niharika/PDF_downloader_automatic/main.py 

<img width="767" alt="image" src="https://github.com/user-attachments/assets/1fec449e-8528-4e8a-9cb2-9642ee208899" />

2. Now user needs to enter the csv file name

   <img width="772" alt="image" src="https://github.com/user-attachments/assets/2c0cfdca-a631-443a-8791-2e0e34dc4172" />

3. After successful completion the the  excel file and folder for pdf will be downloaded.

<img width="731" alt="image" src="https://github.com/user-attachments/assets/c5d0dcbf-fb79-4f5a-860a-ad4710099fd4" />
   
OR


** Execution in cmd prompt :**
1. cd  your folder where the files are saved.(cd Niharika)

2. pip install -r requirements.txt
   
   <img width="650" alt="image" src="https://github.com/user-attachments/assets/358e2955-1e19-48b6-9a8b-3761083cbba3" />

3. python main.py

<img width="434" alt="image" src="https://github.com/user-attachments/assets/0dc8870e-82e7-40cb-a2fa-a8a7114d314d" />

4. next step you need to enter your csv file name (eg GRI_2017_2020.csv)

<img width="539" alt="image" src="https://github.com/user-attachments/assets/f846b73b-36fb-49d6-8312-366a10c886e0" />


If the csv is in correct format you will have and excel file with status and filepaths and folder containing pdfs.

