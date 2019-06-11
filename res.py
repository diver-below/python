import json
import re
import jsonschema

# Функция для валидации первого файла в jsonschema
def if_valid_file1 (file_name):
    with open (file_name, 'r') as readnew:
        data1 = json.load(readnew)
    schema1 = {
            "type" : "object",
            "properties" : {
                    "logs" : {
                            "type" : "array",
                            "items" : [
                                        {
                                            "type" : "object",
                                            "properties" : {
                                                    "time" : {
                                                            "type" : "string"
                                                        },
                                                    "test" : {
                                                            "type" : "string"
                                                        },
                                                    "output" : {
                                                            "type" : "string"
                                                        }
                                                }
                                        }
                                ]
                        }
                }
    }
    try:
        jsonschema.validate(data1, schema1)
#        print ("file #1 is valid")
        return (1)
    except :
#        print ("error in file #1")
        return (0)
               
# Функция для валидации третьего файла в jsonschema
def if_valid_file2 (file_name):
    with open (file_name, 'r') as readnew:
        data2 = json.load(readnew)
    schema2 = {
            "type": "object",
            "properties" : {
                    "suites" : {
                            "type" : "array",
                            "items" : [
                                    {
                                            "type" : "object",
                                            "properties" : {
                                                    "name" : {
                                                            "type" : "string"
                                                        },
                                                    "tests" : {
                                                            "type" : "number"
                                                        },
                                                    "cases" : {
                                                            "type" : "array",
                                                            "items" : [
                                                                    {
                                                                            "type" : "object",
                                                                            "properties" : {
                                                                                    "name" : {
                                                                                            "type" : "string"
                                                                                        },
                                                                                    "errors" : {
                                                                                            "type" : "number"
                                                                                        },
                                                                                    "time" : {
                                                                                            "type" : "string"
                                                                                        }
                                                                                }
                                                                    }
                                                                ]
                                                        }
                                                }
                                    }
                                ]
                        }
                }
    }
    try:
        jsonschema.validate(data2, schema2)
#        print ("file #2 is valid")
        return (1)
    except :
#        print ("error in file #2")
        return (0)

# Функция для валидации третьего файла в jsonschema
def if_valid_file3 (file_name):
    with open (file_name, 'r') as readnew:
        data3 = json.load(readnew)
    schema3 = { 
        "type" : "object",
        "properties":{
                "captures": { 
                        "type" : "array",
                        "items":[
                                    {
                                        "type" : "object",
                                        "properties":{
                                                "expected": {"type" : "string"},
                                                "actual": {"type" : "string"},
                                                "time": {"type" : "string"}
                                                }
                                 },
                                {
                                        "type" : "object",
                                        "properties":{
                                                "expected": {"type" : "string"},
                                                "actual": {"type" : "string"},
                                                "time": {"type" : "string"}
                                                }
                                }
                            ]
                    }
            }
    }
    try:
        jsonschema.validate(data3, schema3)
#        print ("file #3 is valid")
        return (1)
    except :
#        print ("error in file #3")
        return (0)
               
# Функция для проверки всех трех файлов, используя jsonschema
def if_valid_files (if_valid_file1, if_valid_file2, if_valid_file3):
    a = if_valid_file1
    b = if_valid_file2
    c = if_valid_file3
    if a+b+c == 3:
        print ('ALL FILES ARE VALID')
    else:
        print ('SOME FILES ARE NOT VALID!!!')

# функция для работы с первым файлом
def file1 (file_name):
    with open (file_name, "r") as read_file:
        logs1 = json.load(read_file)
        list_logs = logs1['logs']
        logs = list_logs[0]
        name1 = logs['test']
        status1 = logs['output']
        i1 = name1[len(name1)-1]
        return (name1, status1, i1)
 

# функция для работы со вторым файлом       
def file2 (file_name):
    with open (file_name, "r") as read_file:
        logs2 = json.load(read_file)
        lsuites = logs2['suites']
        suites = lsuites[0]
        list_suite1 = suites['cases']
        suite1 = list_suite1[0]
        name2 = suite1['name']
        errors2 = suite1['errors']
        i2 = name2[len(name2)-1] 
        return (name2, errors2, i2)
    
# Данные для третьего файла из тестового задания, скопированные в форме строки
_file3 = """
{
    "captures": [
        {
            "expected": "B"
            "actual": "B",
            "time": "2000-01-01T00:00:20+00:00"
        },
        {
            "expected": "A"
            "actual": "B",
            "time": "2000-01-01T00:00:10+00:00"
        }
    ]
}
"""

# функция проверки поставновки запятых в третьем файле и запись третьего файла
def check (string_of_file3):
    pieces = re.split(r'"', string_of_file3)
    comma = ","
    for i in pieces:
        if re.search(r'^\n            *$',i)!= None:
            ok_str = comma + i
            pieces[pieces.index(i)] = ok_str
    ok_file = '"'.join(pieces)
    ok_file = ok_file[1:len(ok_file)-1:]
    ok_file = eval(ok_file)        
    return (ok_file)
    with open ("file_3.json", "w") as new:
        json.dump(ok_file, new)

    
# функция для работы с третьим файлом
def file3 (file_name):
    with open (file_name, "r") as read_file:
        allcaptures = json.load(read_file)
        lcaptures = allcaptures['captures']
        exp_act_dict = {}
        expact = {}
        ea = []
        k = 1
        for i in lcaptures:
            exp = i['expected']
            expact['expected'] = exp
            act = i['actual']
            expact['actual'] = act
            ea.append(expact)
            exp_act_dict[k] =ea
            k = k+1
            ea = []
            expact = {}
        return (exp_act_dict)
    
# функция для записи в результирующий файл
def result_file (file1, file2, file3):
    file1 = list(file1)
    file2 = list(file2)
    res =  {}
    list_res = []
    for i in file3:
        lmed = file3[i]
        med = lmed[0]
        for m in lmed: 
            if file1[2] == m['expected']:
                r = {}
                r['name'] = file1[0]
                r['status'] = file1[1]
                r.update(m)
                list_res.append(r)
            if file2[2] == m['expected']:
                list_res = []
                r = {}
                r['name'] = file2[0]
                r['errors'] = file2[1]
                r.update(m)
                list_res.append(r)
    res['results'] = list_res
    with open ('result_file.json', 'w') as add_res:
        json.dump(res, add_res)
    

check(_file3)
if_valid_files (if_valid_file1("file_1.json"), if_valid_file2("file_2.json"), if_valid_file3("file_3.json"))
result_file(file1 ("file_1.json"),file2 ("file_2.json"),file3('file_3.json'))
