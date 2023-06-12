import os
# import wget
import zipfile



# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

# # Download the zipped dataset
# url = 'https://drive.google.com/file/d/1X-3JTnv5ssGqLu4rum8Bchm6i2WLjhSU/view?usp=share_link'
zip_name = "data.zip"
# wget.download(url, zip_name)

# Unzip it and standardize the .csv filename
with zipfile.ZipFile(zip_name, "r") as zip_ref:
	zip_ref.extractall()

os.remove(zip_name)
print('\nAll files are being extracted.')
