from unittest import TestCase, mock
import main
import os


class TestProject(TestCase):

    def test_get_file_list(self):
        """
        Should return a dictionary related by file and its size.
        """
        root_dir = "/Users/eunyoungcho/Pictures/2019/example"
        result = main.get_hash_by_file(root_dir)

        expected_value = {
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0201.JPG': '1587fd830af0e02c6a0f6c0d4f21f2af4827989b',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0210.JPG': '1587fd830af0e02c6a0f6c0d4f21f2af4827989b',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0207.JPG': '39332041f67ef96a37fa4dc0ba4e97d4d3a97ce3',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0401.JPG': '87a4cfcfebde26b547695204c95b75ea101e25ea',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0400.JPG': 'ce1b35c4cb181fcbd7968f1706207254714e6eb1',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0301.JPG': '87a4cfcfebde26b547695204c95b75ea101e25ea',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0300.JPG': 'ce1b35c4cb181fcbd7968f1706207254714e6eb1',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0208.JPG': '2990eaa4cbbfeb5d8c1d5d7b2da73f118a247652',
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0209.JPG': '3f647bbc7bb1911a41ace5291772fccc422e13df',
            '/Users/eunyoungcho/Pictures/2019/example/a/IMG_0207.JPG': '39332041f67ef96a37fa4dc0ba4e97d4d3a97ce3'
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_value)

    def test_reverse_index_file_list(self):
        """
        Should return a dictionary where the key is the files's size
        and its values are the file's names.
        """
        map = {
            'IMG_0201.JPG': '234s',
            'IMG_0210.JPG': '234s',
            'IMG_0207.JPG': 'hy345',
            'IMG_0401.JPG': '75rt',
            'IMG_0400.JPG': '1234',
            'IMG_0301.JPG': '75rt',
            'IMG_0300.JPG': '1234',
            'IMG_0208.JPG': '3ge43',
            'IMG_0209.JPG': 'c2g4'
        }
        result = main.get_reverse_index(map)

        expected_value = {
            '1234': {'IMG_0300.JPG', 'IMG_0400.JPG'},
            '75rt': {'IMG_0401.JPG', 'IMG_0301.JPG'},
            '234s': {'IMG_0201.JPG', 'IMG_0210.JPG'},
            'hy345': {'IMG_0207.JPG'},
            '3ge43': {'IMG_0208.JPG'},
            'c2g4': {'IMG_0209.JPG'}
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_value)

    def test_format_file_by_hash_dict(self):
        map = {
            '1234': ('IMG_0300.JPG', 'IMG_0400.JPG'),
            '75rt': ('IMG_0401.JPG', 'IMG_0301.JPG'),
            '234s': ('IMG_0201.JPG', 'IMG_0210.JPG'),
            'hy345': ('IMG_0207.JPG',),
            '3ge43': ('IMG_0208.JPG',),
            'c2g4': ('IMG_0209.JPG',)
        }

        expected_value = [
            ('IMG_0300.JPG', ['IMG_0400.JPG']),
            ('IMG_0401.JPG', ['IMG_0301.JPG']),
            ('IMG_0201.JPG', ['IMG_0210.JPG'])
        ]

        result = main.format_file_by_hash_dict(map)
        self.assertIsInstance(result, list)
        self.assertEqual(result, expected_value)

    def test_ignore_hidden_files(self):
        """
        Should return all files except those start with a dot.
        """
        files = ['archivo.jps', 'file.png', '.oculto']
        result = main.ignore_hidden_files(files)

        expected_value = ['archivo.jps', 'file.png']

        self.assertEqual(expected_value, result)

    def test_sha1_hasher(self):
        """
        Should return the sha1 hash of a file
        """
        moduledirpath = os.path.dirname(__file__)
        filepath = os.path.join(moduledirpath, "test_file.txt")
        result = main.hash_file(filepath)

        expected_value = "50a79820e404c67ebbeb3f79ad96596cf1716be2"
        self.assertEqual(expected_value, result)
