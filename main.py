# Description: Python Dictionary
# Author: Preisler András

#region function
#Létrehozunk egy egy előre definiált könyvtárat
def genMap1():
    #Könyvtár nem változó tipus hű, ez azt jelenti hogy lehet egy key nek STRING értéke még egy másiknak INT
    map = {
        #map[körte] = 1
        "körte": 1,
        #map[alma] = 2
        "alma": 2,
        #map[szilva] = 3
        "szilva": 3,
        #map[barack] = 4
        "barack": 5,
        #map[eper] = nincs
        "eper": "nincs"
        }

    #KIÍRATÁS    
    #Kiírjuk a teljes könyvtárat
    print(map)
    #Végig megyünk a könyvtárban és kiírjuk a kulcsokat és értékeket
    for key in map:
        print(f'{key} : {map[key]}')

#létre hozunk egy könyvtárat, ami a key-ét és értékét a function paramétérben kap meg  
def genMap2(key, value):
    map = {key: value}

    #KIÍRATÁS
    #Kiírjuk a teljes könyvtárat
    print(map)
    print(map[key])    

#Ez a function vissza adja a lista azon 2elemének az indexét amiknek az összege egyenlő a target értékévek
def algorithm(lista: list, target: int):
    IndexMap = dict() #Ez ugyan olyan mintha egy üres Könyvtárat hoztunk létre IndexMap = {}
    for i in range(len(lista)):
        if target - lista[i] in IndexMap:
            return [IndexMap[target - lista[i]], i]
        IndexMap[lista[i]] = i
    return []
#endregion
#region main
def main():
    genMap1()

    genMap2("test", 2)

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 10
    print(algorithm(lista, target))

main()
#endregion
