import os
import string
import random
import json

def store_cpp_format(parsed_json):
    file_name = "backend/data/"+''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".data"
    f = open(file_name, "w+")
    print(parsed_json)
    json_file = open("assets/informatik.json")
    model = json.load(json_file)
    maxDelCredits = model["maxDelCredits"]
    f.write(str(maxDelCredits)+"\n")
    sections = model["sections"]
    for section in sections:
        if "id" in section:
            section_id = str(section["id"])
            if(section_id in parsed_json):
                section_grades = parsed_json[section_id]
                subject_ids = section_grades.keys()
                credits = dict((sub["id"], sub["credits"]) for sub in section["subjects"])
                f.write(";".join([str(section_grades[sid])+","+str(credits[sid]) for sid in subject_ids]))
                f.write("\n")

    return file_name

def solve_cpp(parsed_json):
    file_name = store_cpp_format(parsed_json)
    stream = os.popen("./backend/solve " + file_name)
    output = stream.read()
    print(output)
    os.remove(file_name)
    return {"ausgabe": output}