import zipfile

from constants import PDF_PATH, PNG_PATH, ZIP_PATH


def zip_response(uuid: str):
    zip_path = ZIP_PATH(uuid)
    pdf_path = PDF_PATH(uuid=uuid)
    png_path = PNG_PATH(uuid=uuid)
    zipped = zipfile.ZipFile( zip_path, 'w', zipfile.ZIP_DEFLATED)
    print(f"Created ZIP file at {zipped.pwd}")
    zipped.write(pdf_path)
    zipped.write(png_path)

    zipped.close()