def transform_str_to_string(input_str):
    final_list=[]
    #pre_list=list(input_str.strip("[]").replace(",",""))
    pre_list=input_str.strip("[]")
    final_list=list(pre_list.split(","))
    #for i in pre_list:
    #    if ' ' in pre_list:
    #        pre_list.remove(' ')
    #for i in pre_list:
    #    final_list.append(i)
    #return final_list
    return final_list

source_data="[10,2  ]"
chkPart=transform_str_to_string(source_data)
print(chkPart)
print(type(chkPart))