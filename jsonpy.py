import json


with open("data1.json") as f:
    # load() convert json string to python object 
    python_dict = json.load(f)
    print(python_dict)
    for key, value in python_dict.items():
        print(key, "is", value)

    python_dictz = {"department":"physics","hod":"albert"}
    json_str = json.dumps(python_dictz)
    print(json_str)

    with open("data.json", "w") as f:
        json.dump(python_dictz, f)
        