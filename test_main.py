from unittest import TestCase
import main


class TestProject(TestCase):

    def test_get_file_list(self):
        """
        Should return a dictionary related by file and its size.
        """
        root_dir = "/Users/eunyoungcho/Pictures/2019/example"
        result = main.get_file_list(root_dir)

        expected_value = {
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0201.JPG': 1190906, '/Users/eunyoungcho/Pictures/2019/example/IMG_0210.JPG': 1190906,
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0207.JPG': 1928182, '/Users/eunyoungcho/Pictures/2019/example/IMG_0401.JPG': 1830585,
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0400.JPG': 1844840, '/Users/eunyoungcho/Pictures/2019/example/IMG_0301.JPG': 1830585,
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0300.JPG': 1844840, '/Users/eunyoungcho/Pictures/2019/example/IMG_0208.JPG': 2023441,
            '/Users/eunyoungcho/Pictures/2019/example/IMG_0209.JPG': 2000484, '/Users/eunyoungcho/Pictures/2019/example/a/IMG_0207.JPG': 1928182
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_value)

    def test_reverse_index_file_list(self):
        """
        Should return a dictionary where the key is the files's size
        and its values are the file's names.
        """
        root_dir = "/Users/eunyoungcho/Pictures/2019/example"
        result = main.reverse_index_file_list(root_dir)

        expected_value = {
            1844840: {'IMG_0300.JPG', 'IMG_0400.JPG'},
            1830585: {'IMG_0401.JPG', 'IMG_0301.JPG'},
            1190906: {'IMG_0201.JPG', 'IMG_0210.JPG'},
            1928182: {'IMG_0207.JPG'}, 2023441: {'IMG_0208.JPG'},
            2000484: {'IMG_0209.JPG'}
        }

        self.assertIsInstance(result, dict)
        self.assertEqual(result, expected_value)

    def test_ignore_hidden_files(self):
        """
        Should return all files except those start with a dot.
        """
        files = ['archivo.jps', 'file.png', '.oculto']
        result = main.ignore_hidden_files(files)

        expected_value = ['archivo.jps', 'file.png']

        self.assertEqual(expected_value, result)
