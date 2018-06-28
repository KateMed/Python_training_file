import functools
import json
def to_json(func):
    @functools.wraps(func)
    def new_func():
        a = func()
        b = json.dumps(a)
        return print(b)
    return new_func

@to_json
def get_data():
    a = {'data': 42}
    return a

get_data()
# вернёт '{"data": 42}'