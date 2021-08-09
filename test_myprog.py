import pytest
import newProg
from io import StringIO

def test_sum(monkeypatch):
  input = StringIO('abcd123')
  monkeypatch.setattr('sys.stdin', input)	
  assert newProg.sum() == 6

def test_hexnumbers(monkeypatch):
  input = StringIO('abc123')
  monkeypatch.setattr('sys.stdin', input)
  assert newProg.hexnumbers() == 39

def test_file_sum():
  assert newProg.file_sum('file.tmp') == 6
