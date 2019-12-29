import os
import json
import _jsonnet
import time


    
if __name__ == "__main__":
    print('Hello world!')
    print(os.environ.get('db_username'))
    jsonnet_str = '''
    {
    person1: {
        name: "Alice",
        welcome: "Hello " + self.name + "!",
    },
    person2: self.person1 {
        name: std.extVar("OTHER_NAME"),
    },
    }
    '''
    json_str = _jsonnet.evaluate_snippet(
        "snippet", jsonnet_str,
        ext_vars={'OTHER_NAME': 'Bob'})
    json_obj = json.loads(json_str)
    for person_id, person in json_obj.items():
        print('{} is {}, greeted by "{}'.format(
            person_id,
            person['name'],
            person['welcome'])
            )
    while True:
        time.sleep(10)