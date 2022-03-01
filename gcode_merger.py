import re

def gcode_to_dict(filename):
    p = re.compile('G1\sZ', re.IGNORECASE)
    file_dict = dict()
    section = "start_gcode"
    gcode_block = ""
    with open(filename, "r") as f:
        for line in f:
            if not p.match(line):
                gcode_block += line
            else:
                file_dict[section] = gcode_block
                none ,section, none = line.split(" ")
                section = float(section[1:])
                gcode_block = line
        file_dict[section] = gcode_block
    return file_dict

def dict_merge(dict_list):
    merged_dict = dict()
    merged_dict['start_gcode']= dict_list[0].pop('start_gcode')
    for key in dict_list[0]:
        merged_dict[key] = ''.join([dic[key] for dic in dict_list])
    return merged_dict


def dict_to_gcode(merged_dict):
    with open("./merged.gcode", "w") as f:
        for key in merged_dict.keys():
            f.write(merged_dict[key])

file1_dict = gcode_to_dict("./Shape-Box_0.3mm_FLEX_MK3_30m.gcode")
file2_dict = gcode_to_dict("./Shape-Box_2_0.3mm_FLEX_MK3_30m.gcode")

merged_dict = dict_merge([file1_dict, file2_dict])

dict_to_gcode(merged_dict)

              
