import os

def get_cats_info(path_to_file:str)->[]:
    ret = []
    try:
        with open(file = path_to_file, encoding="UTF-8") as f:
            for line in f:
                res = line.split(",")
                if len(res)!=3:
                    continue
                ret.append({"id":res[0],"name":res[1],"age":res[2]})
    except FileNotFoundError:
        pass
    finally:    
        return ret

print(get_cats_info("files/cats_file.txt"))
