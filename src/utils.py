import os
import zipfile
import config

def zipfolder(folder_path, zipname):
	# crawling through directory and subdirectories
    file_paths = []
    for root, directories, files in os.walk(folder_path):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # writing files to a zipfile
    with zipfile.ZipFile(zipname,'w') as zip:
        # writing each file one by one
        for sfile in file_paths:
            zip.write(sfile, sfile.replace(config.Bot_path, ''))

def unzip_folder(upfile, path):
    # unzip folder and save it into path
    with zipfile.ZipFile(upfile, 'r') as zip_ref:
        zip_ref.extractall(path)