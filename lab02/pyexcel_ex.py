import pyexcel
list_1 = [{'name1' :"lien"},
{"name2" : "ngoc Anh"}]
pyexcel.save_as(records = list_1 ,dest_file_name = "iexcel.xlsx")