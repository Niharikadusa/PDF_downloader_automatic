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

<img width="423" alt="Screenshot 2025-05-23 140943" src="https://github.com/user-attachments/assets/6fec0126-5b29-47f8-a89c-c767ea7f8a62" />



After all the requirements are installed you need to run main file for tool to work

1. The user must run a main.py file
  
eg: c:/Niharika/PDF_downloader_automatic/main.py 
<img width="767" alt="Screenshot 2025-05-23 141056" src="https://github.com/user-attachments/assets/c39ee406-51c5-4734-a422-9ed9e823346e" />



2. Now user needs to enter the csv file name

 <img width="772" alt="Screenshot 2025-05-23 141220" src="https://github.com/user-attachments/assets/bdca55a8-99da-4375-9955-2afce7165847" />


3. After successful completion the the  excel file and folder for pdf will be downloaded.

<img width="731" alt="Screenshot 2025-05-23 141349" src="https://github.com/user-attachments/assets/72ef6180-7772-4d41-ac2e-9fa96d160e45" />

   
OR


** Execution in cmd prompt :**
1. cd  your folder where the files are saved.(cd Niharika)

2. pip install -r requirements.txt
   
  ![Screenshot 2025-05-23 141834](https://github.com/user-attachments/assets/6e9f0ff5-e087-432a-8525-26a7f266553d)


3. python main.py

![Screenshot 2025-05-23 141935](https://github.com/user-attachments/assets/95a32bc5-83bd-4e2f-a561-560261ba4243)


4. next step you need to enter your csv file name (eg GRI_2017_2020.csv)

![Screenshot 2025-05-23 142033](https://github.com/user-attachments/assets/1fa489af-86cb-4250-8015-2b78c0f00ad0)



If the csv is in correct format you will have and excel file with status and filepaths and folder containing pdfs.

