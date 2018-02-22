import unittest
from tempfile import NamedTemporaryFile
from tika import unpack


class CreateTest(unittest.TestCase):
    "Test different encodings"
    text_utf8 = "Hello, world!! 😎 👽"
    text_ascii = "Hello, world!!"

    def test_utf8(self):
        with NamedTemporaryFile("w+t", prefix='tika-python', suffix='.txt', dir='/tmp', encoding="utf8") as f:
            f.write(self.text_utf8)
            f.flush()
            f.seek(0)
            parsed = unpack.from_file(f.name)
            self.assertEqual(parsed["content"].strip(), self.text_utf8)

    def test_ascii(self):
        with NamedTemporaryFile("w+t", prefix='tika-python', suffix='.txt', dir='/tmp', encoding="utf8") as f:
            f.write(self.text_ascii)
            f.flush()
            f.seek(0)
            parsed = unpack.from_file(f.name)
            self.assertEqual(parsed["content"].strip(), self.text_ascii)


if __name__ == '__main__':
    unittest.main()
