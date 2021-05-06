import os

class cInternalControl:
    idControl=7
    timeout=70
    heroku=True
    pdfOn=False
    download_dir='Download_tfja_Daily'
    hfolder='apptfj_daily_2'   
    rutaHeroku='/app/'+hfolder
    rutaLocal=os.getcwd()+'\\'+hfolder+'\\'
    
    