from os import listdir
from os.path import isfile, join, splitext
from pathlib import Path
import os
import shutil

#Path to Download folder
downloads_path = "C:/Users/sondr/Downloads"

#Declaration of folder names and content for the folder
folder_names = {"Audio": {'aif','cda','mid','midi','mp3','mpa','ogg','wav','wma'},
                "Compressed":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'},
                'Code':{'js','jsp','html','ipynb','py','java','css'},
                'Documents':{'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub'},
                'Images':{'bmp','gif .ico','jpeg','jpg','png','jfif','svg','tif','tiff'},
                'Softwares':{'apk','bat','bin', 'exe','jar','msi','py'},
                'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
                'Others': {'NONE'}}
#Gets files in download folder to be moved
onlyfiles = [os.path.join(downloads_path, file)
    for file in os.listdir(downloads_path)
        if os.path.isfile(os.path.join(downloads_path, file))]
#Gets folders in Downloads to be moved
onlyfolders = [os.path.join(downloads_path, file)
               for file in os.listdir(downloads_path)
                    if not os.path.isfile(os.path.join(downloads_path, file))]
#Maps
extension_filetype_map = {extension: fileType 
                          for fileType, extensions in folder_names.items()
                            for extension in extensions }
folder_paths = [os.path.join(downloads_path, folder_name)
                for folder_name in folder_names.keys()]
[os.mkdir(folderPath)
    for folderPath in folder_paths if not
 os.path.exists(folderPath)]

def new_path(old_path):
        extension = str(old_path).split('.')[-1]
        amplified_folder = extension_filetype_map[extension] if extension in extension_filetype_map.keys() else 'Others'
        final_path = os.path.join(downloads_path, amplified_folder, str(old_path).split('\\')[-1])
        return final_path

[Path(eachfile).rename(new_path(eachfile)) for eachfile in onlyfiles]
[Path(onlyfolder).rename(os.path.join(downloads_path,'Others', str(onlyfolder).split('\\')[-1])) 
        for onlyfolder in onlyfolders 
                if str(onlyfolder).split('\\')[-1] not in folder_names.keys()]
