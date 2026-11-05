import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

class TestSite(unittest.TestCase):
    def test_build_produces_matching_revision(self):
        script = Path(__file__).resolve().parents[1] / 'build_site.py'
        with tempfile.TemporaryDirectory() as directory:
            subprocess.run([sys.executable, str(script)], cwd=directory, check=True,
                           env={**os.environ, 'GITHUB_SHA': 'lab-test-revision'})
            result = Path(directory) / 'site'
            self.assertEqual(json.loads((result / 'version.json').read_text())['commit_sha'], 'lab-test-revision')
            self.assertIn('lab-test-revision', (result / 'index.html').read_text())
