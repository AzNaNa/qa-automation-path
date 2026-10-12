from logs import count_levels

def test_empty_list():
    assert count_levels([]) == {}

def test_empty_line():
    assert count_levels([""]) == {}    

def test_two_words():
    assert count_levels(["a b"]) == {}

def test_two_words():
    assert count_levels(["a b"]) == {}

def test_words_lower_upper():
    assert count_levels(["2026-10-12 14:00:00 info x", "2026-10-12 14:00:01 INFO y"]) == {'INFO': 2}


def test_words_lower_upper():
    assert count_levels(["2026-10-12 14:03:55 ERROR Connection timeout",
        "2026-10-12 14:04:01 INFO User logged in",
        "2026-10-12 14:04:12 ERROR Disk full"]) == {'ERROR': 2, 'INFO': 1}
