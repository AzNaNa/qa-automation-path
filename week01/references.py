def add_tag(tags):
    tags_copy = tags.copy()
    tags_copy.append("smoke")
    return tags_copy

base = ["regression"]
result = add_tag(base)
print(base)
print(result)
print(base is result)



def make_test_data(items=None):
    if items is None:
        items = []
    items.append("x")
    return items

print(make_test_data())
print(make_test_data())
print(make_test_data())
print(make_test_data(["a"]))