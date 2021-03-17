import os

class cInternalControl:
    idControl=6
    timeout=70
    heroku=False
    pdfOn=False
    download_dir='Download_tfja_Daily'
    hfolder='apptfj_daily'   
    rutaHeroku='/app/'+hfolder
    rutaLocal=os.getcwd()+'\\'+hfolder+'\\'
    
    