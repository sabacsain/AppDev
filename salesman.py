import json, os


def funcComputeTotal(data):

    for i in data:
        Q1 = i['Q1']
        Q2 = i['Q2']
        Q3 = i['Q3']
        Q4 = i['Q4']
        total = Q1+Q2+Q3+Q4
        placeholder = {"Q1": Q1, "Q2": Q2, "Q3": Q3, "Q4": Q4, "Total":total}
        i.update(placeholder) 
    
    return data


def funcComputeCommission(data):
    commission = 0.0
    
    for i in data:
        if (i['Total'] <= 5000):
            commission = i['Total']*0.15
        elif (i['Total'] <= 10000 and i['Total'] > 5000):
            commission = i['Total']*0.20
        elif (i['Total'] <= 15000 and i['Total'] > 10000):
            commission = i['Total']*0.25
        elif (i['Total'] <= 20000 and i['Total'] > 15000):
            commission = i['Total']*0.30
        elif (i['Total'] <= 25000 and i['Total'] > 20000):
            commission = i['Total']*0.35
        elif (i['Total'] > 25000):
            if (i['Total'] >= 30000):
                commission = 30000
            else:
                commission = i['Total']*0.50

        commission = round(commission, 2)
        placeholder = {"Commission":commission}
        i.update(placeholder)

    return data
   

def funcWriteToFile(data, dirPath):
    
    os.remove(dirPath)
    
    with open(dirPath, 'a') as outfile:
        json.dump(data, outfile, indent=2)
        outfile.close()

    return



if __name__ == '__main__':
    
    dirPath = os.path.dirname(os.path.realpath(__file__))
    dirPath = dirPath + '/salesman.json'

    rawData = open(dirPath)
    data = json.load(rawData)
    rawData.close()

    varTotal = funcComputeTotal(data)
    varCommission = funcComputeCommission(data)
    funcWriteToFile(data, dirPath)
    print("Process done...")




