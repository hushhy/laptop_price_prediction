import json
import re
import pickle
import numpy as np
columns = None
model =None
all = {}
def get_full_names():
    return all

def estimated_price(company, inches, screen, cpu, ram,memory, gpu, weight):
    op = {}
    for c in [company, screen, cpu, memory, gpu]:
        try:
            col_name = [col for col in columns if c.lower() in col][0]
            index = columns.index(col_name)
        except:
            index = -1
        op[c] = index
        
    
    
    x = np.zeros(len(columns))
    x[0] = inches
    x[1] = ram
    x[2] = weight
    for key in op:
        if op[key] >=0:
            x[op[key]] = 1
    return round(model.predict([x])[0], 2)
def load_artifacts():
    global columns
    global model
    global all

    with open ("./artifacts/columns.json" , 'r') as f:
        columns =    json.load(f)['data_columns']
        for c in ['company', 'screenresolution', 'cpu', 'memory', 'gpu']:
            all[c] = [col.replace(f'{c}_', '', 1) for col in columns if re.search(c, col)]

    with open("./artifacts/laptop_prices_model.pickle", 'rb') as f:
        model= pickle.load(f)
    print("doneeeee")
    

if __name__ == "__main__":
    load_artifacts()
    print (estimated_price('apple',13.2,'IPS Panel Retina Display 2560x1600','Intel Core i7 2.7GHz',8,'128GB Flash Storage', 'Intel Iris Plus Graphics 650', 1.54))
    #for i in ['company', 'screenresolution', 'cpu', 'memory', 'gpu']:
        
    print(get_full_names())