import zipfile

from constants import PDF_PATH, PNG_PATH, ZIP_PATH


def zip_response():
    zipped = zipfile.ZipFile( "/" + ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
    print(f"Created ZIP file at {zipped.pwd}")
    zipped.write(PDF_PATH)
    zipped.write(PNG_PATH)

    zipped.close()