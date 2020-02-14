import os 
import json
import pytest
import tiptapy


def scan_json_datadir():
    """Returns a dict for data/json directory"""
    store = {}
    json_dir = 'data/json/'
    json_files = os.listdir(json_dir)
    for file in json_files:
        f = open(json_dir + f'{file}')
        data = f.read()
        store[file.split('.json')[0]] = json.loads(data)
    return store


def scan_html_datadir():
    """Returns a dict for data/html directory"""
    files = {}
    html_dir= 'data/html/'
    html_files = os.listdir(html_dir)
    for file in html_files:
        f = open(html_dir + f'{file}')
        data = f.read()
        files[file.split('.html')[0]] = data
    return files


json_dir_data = scan_json_datadir()
html_dir_data = scan_html_datadir()


def test_to_html():
    """Test to check to_html() function"""
    input_data = json.dumps(json_dir_data['simple'])
    expected_html = html_dir_data['simple']
    assert tiptapy.to_html(input_data) == expected_html


def test_blockquote():
    """Test to check BlockQuote"""
    blockquote = json.dumps(json_dir_data['blockquote'])
    expected_html = html_dir_data['blockquote']
    assert tiptapy.to_html(blockquote) == expected_html


def test_bulletlist():
    """Test to check BulletList"""
    bulletlist = json.dumps(json_dir_data['bulletlist'])
    expected_html = html_dir_data['bulletlist']
    assert tiptapy.to_html(bulletlist) == expected_html


def test_text():
    """Test to check mark_tags bold,italic,link"""
    mark_tags = json.dumps(json_dir_data['mark_tags'])
    expected_html = html_dir_data['mark_tags']
    assert tiptapy.to_html(mark_tags) == expected_html
