import sys
from copy import deepcopy

truth_assignment = []

def remove_liter(cnf):
    literalList = []
    for i in cnf:
        if len(i)>=1:
            for j in i:
                if j<0:
                    literalList.append(abs(j))
                else:
                    literalList.append(j)
    literalList = set(literalList)
    return literalList


def preproc(input_cnf):
    literalList = []
    for i in input_cnf:
        if len(i)>=1:
            for j in i:
                if j<0:
                    literalList.append(abs(j))
                else:
                    literalList.append(j)
    literalList = set(literalList)
    return literalList,input_cnf


def dpll(cnf, liters):
    global truth_assignment
    # ------------start unit propa-----------------
    while True:
        if len(liters) == 1 and len(cnf) > 1:
            print('--------------------------------------------------')
            print(cnf)
            print(liters)
            break
        print('--------------------------------------------------')
        print('cnf',cnf)
        print('liters',liters)
        delete_list = []
        unit_clause = None

        # find unit clause and remove from the original cnf
        for i in range(len(cnf)):
            if len(cnf[i])==1:
                unit_clause = cnf[i][0]
                truth_assignment.append(unit_clause)
                del cnf[i]
                break

        print('unit_clause',unit_clause)

        #finding if negation of unit clause in cnf 
        if unit_clause:
            for literalList in cnf:
                if len(literalList)==1:
                    if(unit_clause>0 and (-unit_clause in literalList)):
                        return False
                    if(unit_clause<0 and (unit_clause in literalList)):
                        return False     

        #if unit clause is present and (!unit clause) present as literal in original clause 
            #remove the literal from the clause and update the literal list
        
        #if unit clause is present and (!unit clause) present as literal in original clause
            #remove the clause
        if(unit_clause and unit_clause>0):
            deleteArray = []
            for i in range(len(cnf)):
                deleteLiterals = []
                if -unit_clause in cnf[i]:
                    for j in range(len(cnf[i])):
                        if(cnf[i][j] == -unit_clause):
                            deleteLiterals.append((i,j))

                    def take_first(obj):
                        return obj[0]

                    if(len(deleteLiterals)>0):
                        for x,y in sorted(deleteLiterals,key = take_first):
                            del(cnf[x][y])

                elif(unit_clause in cnf[i]):
                    deleteArray.append(i)
                    
            if(len(deleteArray)>0):
                for index in sorted(deleteArray,reverse = True):
                    del cnf[index]
            print('updated cnf:',cnf)                
            liters = remove_liter(cnf)
            print('newLiteral',liters)

        #if unit clause is present and (!unit clause) present as literal in original clause 
            #remove the literal from the clause and update the literal list
       
        #if unit clause is present and (!unit clause) present as literal in original clause
            #remove the clause     
        elif(unit_clause and unit_clause<0):
            deleteArray = []
            for i in range(len(cnf)):
                deleteLiterals = []
                if -unit_clause in cnf[i]:
                    for j in range(len(cnf[i])):
                        if(cnf[i][j] == -unit_clause):
                            deleteLiterals.append((i,j))

                    def take_first(obj):
                        return obj[0]

                    if(len(deleteLiterals)>0):
                        for x,y in sorted(deleteLiterals,key = take_first):
                            del(cnf[x][y])

                elif(unit_clause in cnf[i]):
                    deleteArray.append(i)

            if(len(deleteArray)>0):
                for index in sorted(deleteArray,reverse = True):
                    del cnf[index]
            print('updated cnf:',cnf)                
            liters = remove_liter(cnf)               
            print('newLiteral',liters)                      

        else:
            break
    # --------------end unit propa----------------------

    # checking clause
    if cnf == []:
        return True
    elif len(liters) == 1 and len(cnf) > 1:
        return False

    # case-splitting
    print("before case splitting cnf:",cnf)
    value = list(liters)[0]

    if dpll(cnf+[[value]],deepcopy(liters)) or dpll(cnf+[[-value]],deepcopy(liters)):
        return True
    else:
        return False


def main():
    global truth_assignment
    with open(sys.argv[1]) as f:
        input_cnf = []
        for line in f: # read rest of lines
            input_cnf.append([int(x) for x in line.split()])
    liters, cnf = preproc(input_cnf)
    if(dpll(cnf, liters)):
        print('--------------------------------------------------')
        print('[Result] : Satisfiable')
        # print(truth_assignment)
        print()
        print("The truth value Assignment is as below:\n")
        for i in truth_assignment:
            if(i>0):
                print(" "+str(i)+":"+" True")
            else:
                print(str(i)+":"+" False")
    else:
        print('--------------------------------------------------')
        print('[Result] : UnSatisfiable')

if __name__ == '__main__':
    main()
