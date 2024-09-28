from pathlib import Path
import unittest
import os
import matplotlib.pyplot as plt

from generate import save_outputs

class SaveOutputsTestCase(unittest.TestCase):

    def testCreatesCorrectOutputFiles(self):

        self.delete_tmp_dir_contents()

        fig, ax = plt.subplots()

        save_outputs(fig, ax)

        self.assert_files_created(["tmp/tmp.pdf", "tmp/tmp.png"])


    def delete_tmp_dir_contents(self):
        for file in os.listdir('tmp'):
            if file == "__init__.py":
                continue
            os.remove("tmp/" + file)

    def assert_files_created(self, files):
        for file in files:
            self.assertTrue(Path(file).is_file())