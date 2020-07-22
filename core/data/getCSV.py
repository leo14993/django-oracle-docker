from csv import DictReader
# from core.functions.suport import Functions

from datetime import datetime

list_of_dict = list(DictReader(open('core/data/My_project_file.csv', 'r'), delimiter=';'))
List_file=[dict(i) for i in list_of_dict]

# List_file = [{'Nome': 'azul', 'Data': '2020-01-15T10:30:02Z', 'Valor': '22.4'}, 
#             {'Nome': 'verde ', 'Data': '2020-01-20T10:40:02Z', 'Valor': '45.8'}, 
#             {'Nome': 'laranja', 'Data': '2020-01-25T10:00:20Z', 'Valor': '12.0'}]

print (List_file)
def convertDT(date_in):
    if type(date_in)==str:
        x = date_in.replace("T"," ") 
        x = x.replace("Z","")
        date_time = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
        return date_time
    else:
        return date_in


def csv_files():
      
    dict_list = []
    for value in List_file: 
        dict_project ={}
        dict_project["Cor"]= value["Nome"]
        dict_project["Data_hora"] = convertDT(value["Data"])
        dict_list.append(dict_project)
    return dict_list

# csv_files = [{'Cor': 'azul', 'Data_hora': datetime.datetime(2020, 1, 15, 10, 30, 2)}, 
#             {'Cor': 'verde ', 'Data_hora': datetime.datetime(2020, 1, 20, 10, 40, 2)}, 
#             {'Cor': 'laranja', 'Data_hora': datetime.datetime(2020, 1, 25, 10, 0, 20)}]