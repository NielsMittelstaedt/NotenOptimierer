import os
import string
import random
import json

def store_cpp_format(parsed_json):
    file_name = "backend/data/"+''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".data"
    f = open(file_name, "w+")

    #load major grade-model
    json_file = open("assets/informatik.json")
    model = json.load(json_file)
    maxDelCredits = model["maxDelCredits"]

    #first line: maximum credits deletable
    f.write(str(maxDelCredits)+"\n")
    sections = model["sections"]

    for section in sections:
        if "id" in section:
            section_id = str(section["id"])
            if(section_id in parsed_json and not parsed_json[section_id] == {}):
                section_grades = parsed_json[section_id]
                subject_ids = section_grades.keys()
                grade_credits = dict((sub["id"], sub["credits"]) for sub in section["subjects"])
                f.write(";".join([str(section_grades[sid])+","+str(grade_credits[sid])+","+str(sid) for sid in subject_ids]))
                f.write("\n")
            elif(section_id == "appl"):
                minors = section["categories"]
                for minor in minors:
                    minor_id = minor["id"]
                    if(minor_id in parsed_json and not parsed_json[minor_id] == {}):
                        minor_grades = parsed_json[minor_id]
                        subject_ids = minor_grades.keys()
                        grade_credits = dict((sub["id"], sub["credits"]) for sub in minor["subjects"])
                        f.write(";".join([str(minor_grades[sid])+","+str(grade_credits[sid])+","+str(sid) for sid in subject_ids]))
                        break

    return file_name

def solve_cpp(parsed_json):
    file_name = store_cpp_format(parsed_json)
    stream = os.popen("./backend/solve " + file_name)
    console_output = stream.read()
    if console_output:
        return {"error": console_output}
    output = []
    with open(file_name) as f:
        output = f.read().splitlines()
    os.remove(file_name)
    return {"grade": float(output[0]), "deletions": output[1:]}