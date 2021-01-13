import csv
from io import StringIO


def csv_read_as_list(csv_data: str, **kwargs):
    """Read the csv_data (which can be a URL, file path, or raw CSV) as a list."""
    yield from csv.reader(StringIO(csv_data), **kwargs)


def csv_read_as_dict(csv_data: str, **kwargs):
    """Read the csv_data (which can be a URL, file path, or raw CSV) as a dict."""
    # TODO: should I do something to detect failures and try with a different delimiter?

    reader = csv.DictReader(StringIO(csv_data), **kwargs)
    yield from reader
