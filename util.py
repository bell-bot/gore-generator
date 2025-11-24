import zipfile

from constants import PDF_PATH, PNG_PATH, ZIP_PATH

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='utils.log', encoding='utf-8', level=logging.DEBUG)

def zip_response():
    zipped = zipfile.ZipFile( ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
    logger.debug(f"Created ZIP file at {zipped.pwd}")
    zipped.write(PDF_PATH)
    zipped.write(PNG_PATH)

    zipped.close()