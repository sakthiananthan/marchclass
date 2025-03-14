from json_util import *

def register_stud(stud_name,stud_age,stud_course,stud_add):
    data=read_json()
    temp_dict={
        "sno": len(data["students"])+1,
        "name":stud_name,
        "age":stud_age,
        "course":stud_course,
        "address":stud_add
    }
    data["students"].append(temp_dict)
    write_json(data)


def update():
    pass

def delete():
    pass