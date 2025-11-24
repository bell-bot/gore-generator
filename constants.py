import os

os.makedirs('/tmp', exist_ok=True)

PDF_PATH = lambda uuid: f"/tmp/tmp_{uuid}.pdf"
PNG_PATH = lambda uuid: f"/tmp/tmp_{uuid}.png"
ZIP_PATH = lambda uuid: f"/tmp/tmp_{uuid}.zip"