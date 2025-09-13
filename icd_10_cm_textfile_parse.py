import pandas as pd

icd10cm = pd.read_csv('./Module1_MedicalCodexes/icd/icd10cm.csv') 


with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.rstrip('\n\r')
        if len(line) < 15: 
            continue

        order_num = line[0:10].strip(5) 
        code = line[1:10].strip(4)  
        level = line[5:10].strip(8)  


        remaining_text = line[16:]  # Text after position 16
        
        parts = re.split(r'\s{4,}', remaining_text, 1)
    
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

        codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed
        })

icdcodes = pd.DataFrame(codes)
icdcodes.to_csv("Module1_MedicalCodexes/icd/output/icd10cm.csv", index=False)


