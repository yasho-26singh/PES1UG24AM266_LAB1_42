"""Regression checks for contact behavior and safer backup handling."""
import contextlib
import csv
import hashlib
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import address_book as book


class AddressBookTests(unittest.TestCase):
    """Exercise normal behavior, error paths, exports and backup safety."""

    def setUp(self):
        book.contacts.clear()
        self.directory = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def test_phone_validation(self):
        for phone in ('12345', 'abcdefghij', '12345678901', '987654321\n'):
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertFalse(book.add_contact('Invalid', phone))
        self.assertEqual(book.contacts, {})
        self.assertTrue(book.add_contact('Valid', '0123456789'))

    def test_replace_and_defaults(self):
        book.add_contact('Neha', '9876543210')
        self.assertEqual(book.contacts['Neha']['city'], 'Unknown')
        book.add_contact('Neha', '9123456780', city='Chennai')
        self.assertEqual(len(book.contacts), 1)
        self.assertEqual(book.contacts['Neha']['phone'], '9123456780')

    def test_search(self):
        book.add_contact('Neha Sharma', '9876543210')
        self.assertEqual(book.search_contacts('SHARMA'), ['Neha Sharma'])
        self.assertEqual(book.search_contacts('7654'), ['Neha Sharma'])
        self.assertEqual(book.search_contacts('absent'), [])

    def test_city_update_and_grouping(self):
        book.add_contact('Neha', '9876543210', city='Bengaluru')
        self.assertTrue(book.update_city('Neha', 'Chennai'))
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertFalse(book.update_city('Missing', 'Delhi'))
        self.assertEqual(book.contacts_by_city(), {'Chennai': ['Neha']})

    def test_unexpected_errors_propagate(self):
        book.contacts['Broken'] = None
        with self.assertRaises(TypeError):
            book.update_city('Broken', 'Delhi')

    def test_sorted_directory(self):
        book.add_contact('Zoya', '9876543210')
        book.add_contact('Anu', '9123456780')
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            book.print_directory()
        self.assertEqual(output.getvalue().splitlines(),
                         ['1 Anu 9123456780', '2 Zoya 9876543210'])

    def test_csv_unicode_and_quoting(self):
        book.add_contact('Neha, Sharma', '9876543210', city='Bengaluru – 東京')
        path = self.root / 'contacts.csv'
        book.export_csv(path)
        with path.open(encoding='utf-8', newline='') as stream:
            self.assertEqual(list(csv.reader(stream)),
                             [['Neha, Sharma', '9876543210', '',
                               'Bengaluru – 東京']])

    def test_json_round_trip_and_restore_semantics(self):
        book.add_contact('Neha', '9876543210', city='Mysuru')
        path = self.root / 'contacts.bak'
        book.backup_book(path)
        self.assertEqual(json.loads(path.read_text(encoding='utf-8')),
                         book.contacts)
        saved = dict(book.contacts)
        book.contacts.clear()
        self.assertEqual(book.restore_book(path), saved)
        self.assertEqual(book.contacts, {})

    def test_invalid_or_missing_backup(self):
        path = self.root / 'contacts.bak'
        with self.assertRaises(FileNotFoundError):
            book.restore_book(path)
        path.write_bytes(b'not a JSON backup')
        with self.assertRaises(json.JSONDecodeError):
            book.restore_book(path)

    def test_display_id(self):
        expected = hashlib.sha256(b'Neha Sharma').hexdigest()[:6]
        self.assertEqual(book.contact_id('Neha Sharma'), expected)

    def test_import_has_no_demo_side_effects(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            importlib.reload(book)
        self.assertEqual(output.getvalue(), '')
        self.assertEqual(list(self.root.iterdir()), [])

    def test_demo_matches_baseline_except_hash(self):
        source = Path(book.__file__).resolve()
        result = subprocess.run([sys.executable, str(source)], cwd=self.root,
                                capture_output=True, text=True, check=True)
        baseline = (source.parent / 'original/demo_output.txt').read_text()
        expected = baseline.replace('Id for Neha: ecc177',
                                    'Id for Neha: ' + book.contact_id('Neha Sharma'))
        self.assertEqual(result.stdout, expected)
        self.assertTrue((self.root / 'contacts.csv').is_file())
        self.assertTrue((self.root / 'contacts.bak').is_file())


if __name__ == '__main__':
    unittest.main()
