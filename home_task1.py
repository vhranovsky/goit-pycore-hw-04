import os

def total_salay(path_to_file:str)->():
    all_salary = 0
    average_salary = 0
    counter = 0 
    try:
        with open(file = path_to_file, encoding="UTF-8") as f:
            for line in f:
                res = line.split(",")
                if len(res)!=2:
                    continue
                try:
                    all_salary += float(res[1])
                    counter += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        pass
    finally:    
        if counter>0 :
            average_salary = int(all_salary / counter)
        return (all_salary,average_salary)

        
res = total_salay("files/salary_file.txt")
print(f"Загальна сума заробітної плати: {res[0]}, Середня заробітна плата: {res[1]}")