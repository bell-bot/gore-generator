from pathlib import Path
import unittest
from unittest.mock import patch
import os
import matplotlib.pyplot as plt

from generate import save_outputs

class SaveOutputsTestCase(unittest.TestCase):

    @patch('generate.PDF_PATH', lambda uuid : f'tmp/test_{uuid}.pdf')
    @patch('generate.PNG_PATH', lambda uuid: f'tmp/test_{uuid}.png')
    def testCreatesCorrectOutputFiles(self):

        self.delete_tmp_dir_contents()

        fig, ax = plt.subplots()
        save_outputs(fig, ax, uuid = "1")

        self.assert_files_created(["tmp/test_1.pdf", "tmp/test_1.png"])
        self.delete_tmp_dir_contents()

    def delete_tmp_dir_contents(self):
        for file in os.listdir('tmp'):
            if file == "__init__.py":
                continue
            os.remove("tmp/" + file)

    def assert_files_created(self, files):
        for file in files:
            self.assertTrue(Path(file).is_file())