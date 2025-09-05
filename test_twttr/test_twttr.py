import pytest
from twttr import shorten

def main():
      test_uppercase()
      test_numbers()
      test_punc()
      test_novowels()

#Tests uppercase and lowercase letters
def test_uppercase():
     assert shorten("TWITTER") == "TWTTR"
     assert shorten("twitter") == "twttr"
     assert shorten("AeIoU") == ""

#Tests numbers
def test_numbers():
      assert shorten("123") == "123"

#Tests punctuation
def test_punc():
      assert shorten("wh@aat?") == "wh@t?"

#Tests texts with no vowels
def test_novowels():
      assert shorten("twttr") == "twttr"

if __name__ == "__main__":
    main()