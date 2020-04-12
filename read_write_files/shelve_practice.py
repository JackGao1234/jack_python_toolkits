import shelve


foo = [1, 2, 3, 4, 8]
bar = 'hi'

with shelve.open('shelve_repo', 'c') as shelf:
    shelf['foo'] = foo
    shelf['bar'] = bar


# foo_from_shelf = None
# bar_from_shelf = None
with shelve.open('shelve_repo', 'r') as shelf:
    foo_from_shelf = shelf['foo']
    bar_from_shelf = shelf['bar']

print(foo_from_shelf)
print(bar_from_shelf)
