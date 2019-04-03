#! /usr/bin/python3

import pprint

elements = {"elements":[{"name":"Hydrogen","symbol":"H","number":1,"phase":"Gas","atomic_mass":1.008,"pos_row":1,"pos_col":1},{"name":"Helium","symbol":"He","number":2,"phase":"Gas","atomic_mass":4.0026022,"pos_row":1,"pos_col":18},{"name":"Lithium","symbol":"Li","number":3,"phase":"Solid","atomic_mass":6.94,"pos_row":2,"pos_col":1},{"name":"Beryllium","symbol":"Be","number":4,"phase":"Solid","atomic_mass":9.01218315,"pos_row":2,"pos_col":2},{"name":"Boron","symbol":"B","number":5,"phase":"Solid","atomic_mass":10.81,"pos_row":2,"pos_col":13},{"name":"Carbon","symbol":"C","number":6,"phase":"Solid","atomic_mass":12.011,"pos_row":2,"pos_col":14},{"name":"Nitrogen","symbol":"N","number":7,"phase":"Gas","atomic_mass":14.007,"pos_row":2,"pos_col":15},{"name":"Oxygen","symbol":"O","number":8,"phase":"Gas","atomic_mass":15.999,"pos_row":2,"pos_col":16},{"name":"Fluorine","symbol":"F","number":9,"phase":"Gas","atomic_mass":18.9984031636,"pos_row":2,"pos_col":17},{"name":"Neon","symbol":"Ne","number":10,"phase":"Gas","atomic_mass":20.17976,"pos_row":2,"pos_col":18},{"name":"Sodium","symbol":"Na","number":11,"phase":"Solid","atomic_mass":22.989769282,"pos_row":3,"pos_col":1},{"name":"Magnesium","symbol":"Mg","number":12,"phase":"Solid","atomic_mass":24.305,"pos_row":3,"pos_col":2},{"name":"Aluminium","symbol":"Al","number":13,"phase":"Solid","atomic_mass":26.98153857,"pos_row":3,"pos_col":13},{"name":"Silicon","symbol":"Si","number":14,"phase":"Solid","atomic_mass":28.085,"pos_row":3,"pos_col":14},{"name":"Phosphorus","symbol":"P","number":15,"phase":"Solid","atomic_mass":30.9737619985,"pos_row":3,"pos_col":15},{"name":"Sulfur","symbol":"S","number":16,"phase":"Solid","atomic_mass":32.06,"pos_row":3,"pos_col":16},{"name":"Chlorine","symbol":"Cl","number":17,"phase":"Gas","atomic_mass":35.45,"pos_row":3,"pos_col":17},{"name":"Argon","symbol":"Ar","number":18,"phase":"Gas","atomic_mass":39.9481,"pos_row":3,"pos_col":18},{"name":"Potassium","symbol":"K","number":19,"phase":"Solid","atomic_mass":39.09831,"pos_row":4,"pos_col":1},{"name":"Calcium","symbol":"Ca","number":20,"phase":"Solid","atomic_mass":40.0784,"pos_row":4,"pos_col":2},{"name":"Scandium","symbol":"Sc","number":21,"phase":"Solid","atomic_mass":44.9559085,"pos_row":4,"pos_col":3},{"name":"Titanium","symbol":"Ti","number":22,"phase":"Solid","atomic_mass":47.8671,"pos_row":4,"pos_col":4},{"name":"Vanadium","symbol":"V","number":23,"phase":"Solid","atomic_mass":50.94151,"pos_row":4,"pos_col":5},{"name":"Chromium","symbol":"Cr","number":24,"phase":"Solid","atomic_mass":51.99616,"pos_row":4,"pos_col":6},{"name":"Manganese","symbol":"Mn","number":25,"phase":"Solid","atomic_mass":54.9380443,"pos_row":4,"pos_col":7},{"name":"Iron","symbol":"Fe","number":26,"phase":"Solid","atomic_mass":55.8452,"pos_row":4,"pos_col":8},{"name":"Cobalt","symbol":"Co","number":27,"phase":"Solid","atomic_mass":58.9331944,"pos_row":4,"pos_col":9},{"name":"Nickel","symbol":"Ni","number":28,"phase":"Solid","atomic_mass":58.69344,"pos_row":4,"pos_col":10},{"name":"Copper","symbol":"Cu","number":29,"phase":"Solid","atomic_mass":63.5463,"pos_row":4,"pos_col":11},{"name":"Zinc","symbol":"Zn","number":30,"phase":"Solid","atomic_mass":65.382,"pos_row":4,"pos_col":12},{"name":"Gallium","symbol":"Ga","number":31,"phase":"Solid","atomic_mass":69.7231,"pos_row":4,"pos_col":13},{"name":"Germanium","symbol":"Ge","number":32,"phase":"Solid","atomic_mass":72.6308,"pos_row":4,"pos_col":14},{"name":"Arsenic","symbol":"As","number":33,"phase":"Solid","atomic_mass":74.9215956,"pos_row":4,"pos_col":15},{"name":"Selenium","symbol":"Se","number":34,"phase":"Solid","atomic_mass":78.9718,"pos_row":4,"pos_col":16},{"name":"Bromine","symbol":"Br","number":35,"phase":"Liquid","atomic_mass":79.904,"pos_row":4,"pos_col":17},{"name":"Krypton","symbol":"Kr","number":36,"phase":"Gas","atomic_mass":83.7982,"pos_row":4,"pos_col":18},{"name":"Rubidium","symbol":"Rb","number":37,"phase":"Solid","atomic_mass":85.46783,"pos_row":5,"pos_col":1},{"name":"Strontium","symbol":"Sr","number":38,"phase":"Solid","atomic_mass":87.621,"pos_row":5,"pos_col":2},{"name":"Yttrium","symbol":"Y","number":39,"phase":"Solid","atomic_mass":88.905842,"pos_row":5,"pos_col":3},{"name":"Zirconium","symbol":"Zr","number":40,"phase":"Solid","atomic_mass":91.2242,"pos_row":5,"pos_col":4},{"name":"Niobium","symbol":"Nb","number":41,"phase":"Solid","atomic_mass":92.906372,"pos_row":5,"pos_col":5},{"name":"Molybdenum","symbol":"Mo","number":42,"phase":"Solid","atomic_mass":95.951,"pos_row":5,"pos_col":6},{"name":"Technetium","symbol":"Tc","number":43,"phase":"Solid","atomic_mass":98,"pos_row":5,"pos_col":7},{"name":"Ruthenium","symbol":"Ru","number":44,"phase":"Solid","atomic_mass":101.072,"pos_row":5,"pos_col":8},{"name":"Rhodium","symbol":"Rh","number":45,"phase":"Solid","atomic_mass":102.905502,"pos_row":5,"pos_col":9},{"name":"Palladium","symbol":"Pd","number":46,"phase":"Solid","atomic_mass":106.421,"pos_row":5,"pos_col":10},{"name":"Silver","symbol":"Ag","number":47,"phase":"Solid","atomic_mass":107.86822,"pos_row":5,"pos_col":11},{"name":"Cadmium","symbol":"Cd","number":48,"phase":"Solid","atomic_mass":112.4144,"pos_row":5,"pos_col":12},{"name":"Indium","symbol":"In","number":49,"phase":"Solid","atomic_mass":114.8181,"pos_row":5,"pos_col":13},{"name":"Tin","symbol":"Sn","number":50,"phase":"Solid","atomic_mass":118.7107,"pos_row":5,"pos_col":14},{"name":"Antimony","symbol":"Sb","number":51,"phase":"Solid","atomic_mass":121.7601,"pos_row":5,"pos_col":15},{"name":"Tellurium","symbol":"Te","number":52,"phase":"Solid","atomic_mass":127.603,"pos_row":5,"pos_col":16},{"name":"Iodine","symbol":"I","number":53,"phase":"Solid","atomic_mass":126.904473,"pos_row":5,"pos_col":17},{"name":"Xenon","symbol":"Xe","number":54,"phase":"Gas","atomic_mass":131.2936,"pos_row":5,"pos_col":18},{"name":"Cesium","symbol":"Cs","number":55,"phase":"Solid","atomic_mass":132.905451966,"pos_row":6,"pos_col":1},{"name":"Barium","symbol":"Ba","number":56,"phase":"Solid","atomic_mass":137.3277,"pos_row":6,"pos_col":2},{"name":"Lanthanum","symbol":"La","number":57,"phase":"Solid","atomic_mass":138.905477,"pos_row":9,"pos_col":3},{"name":"Cerium","symbol":"Ce","number":58,"phase":"Solid","atomic_mass":140.1161,"pos_row":9,"pos_col":4},{"name":"Praseodymium","symbol":"Pr","number":59,"phase":"Solid","atomic_mass":140.907662,"pos_row":9,"pos_col":5},{"name":"Neodymium","symbol":"Nd","number":60,"phase":"Solid","atomic_mass":144.2423,"pos_row":9,"pos_col":6},{"name":"Promethium","symbol":"Pm","number":61,"phase":"Solid","atomic_mass":145,"pos_row":9,"pos_col":7},{"name":"Samarium","symbol":"Sm","number":62,"phase":"Solid","atomic_mass":150.362,"pos_row":9,"pos_col":8},{"name":"Europium","symbol":"Eu","number":63,"phase":"Solid","atomic_mass":151.9641,"pos_row":9,"pos_col":9},{"name":"Gadolinium","symbol":"Gd","number":64,"phase":"Solid","atomic_mass":157.253,"pos_row":9,"pos_col":10},{"name":"Terbium","symbol":"Tb","number":65,"phase":"Solid","atomic_mass":158.925352,"pos_row":9,"pos_col":11},{"name":"Dysprosium","symbol":"Dy","number":66,"phase":"Solid","atomic_mass":162.5001,"pos_row":9,"pos_col":12},{"name":"Holmium","symbol":"Ho","number":67,"phase":"Solid","atomic_mass":164.930332,"pos_row":9,"pos_col":13},{"name":"Erbium","symbol":"Er","number":68,"phase":"Solid","atomic_mass":167.2593,"pos_row":9,"pos_col":14},{"name":"Thulium","symbol":"Tm","number":69,"phase":"Solid","atomic_mass":168.934222,"pos_row":9,"pos_col":15},{"name":"Ytterbium","symbol":"Yb","number":70,"phase":"Solid","atomic_mass":173.0451,"pos_row":9,"pos_col":16},{"name":"Lutetium","symbol":"Lu","number":71,"phase":"Solid","atomic_mass":174.96681,"pos_row":9,"pos_col":17},{"name":"Hafnium","symbol":"Hf","number":72,"phase":"Solid","atomic_mass":178.492,"pos_row":6,"pos_col":4},{"name":"Tantalum","symbol":"Ta","number":73,"phase":"Solid","atomic_mass":180.947882,"pos_row":6,"pos_col":5},{"name":"Tungsten","symbol":"W","number":74,"phase":"Solid","atomic_mass":183.841,"pos_row":6,"pos_col":6},{"name":"Rhenium","symbol":"Re","number":75,"phase":"Solid","atomic_mass":186.2071,"pos_row":6,"pos_col":7},{"name":"Osmium","symbol":"Os","number":76,"phase":"Solid","atomic_mass":190.233,"pos_row":6,"pos_col":8},{"name":"Iridium","symbol":"Ir","number":77,"phase":"Solid","atomic_mass":192.2173,"pos_row":6,"pos_col":9},{"name":"Platinum","symbol":"Pt","number":78,"phase":"Solid","atomic_mass":195.0849,"pos_row":6,"pos_col":10},{"name":"Gold","symbol":"Au","number":79,"phase":"Solid","atomic_mass":196.9665695,"pos_row":6,"pos_col":11},{"name":"Mercury","symbol":"Hg","number":80,"phase":"Liquid","atomic_mass":200.5923,"pos_row":6,"pos_col":12},{"name":"Thallium","symbol":"Tl","number":81,"phase":"Solid","atomic_mass":204.38,"pos_row":6,"pos_col":13},{"name":"Lead","symbol":"Pb","number":82,"phase":"Solid","atomic_mass":207.21,"pos_row":6,"pos_col":14},{"name":"Bismuth","symbol":"Bi","number":83,"phase":"Solid","atomic_mass":208.980401,"pos_row":6,"pos_col":15},{"name":"Polonium","symbol":"Po","number":84,"phase":"Solid","atomic_mass":209,"pos_row":6,"pos_col":16},{"name":"Astatine","symbol":"At","number":85,"phase":"Solid","atomic_mass":210,"pos_row":6,"pos_col":17},{"name":"Radon","symbol":"Rn","number":86,"phase":"Gas","atomic_mass":222,"pos_row":6,"pos_col":18},{"name":"Francium","symbol":"Fr","number":87,"phase":"Solid","atomic_mass":223,"pos_row":7,"pos_col":1},{"name":"Radium","symbol":"Ra","number":88,"phase":"Solid","atomic_mass":226,"pos_row":7,"pos_col":2},{"name":"Actinium","symbol":"Ac","number":89,"phase":"Solid","atomic_mass":227,"pos_row":10,"pos_col":3},{"name":"Thorium","symbol":"Th","number":90,"phase":"Solid","atomic_mass":232.03774,"pos_row":10,"pos_col":4},{"name":"Protactinium","symbol":"Pa","number":91,"phase":"Solid","atomic_mass":231.035882,"pos_row":10,"pos_col":5},{"name":"Uranium","symbol":"U","number":92,"phase":"Solid","atomic_mass":238.028913,"pos_row":10,"pos_col":6},{"name":"Neptunium","symbol":"Np","number":93,"phase":"Solid","atomic_mass":237,"pos_row":10,"pos_col":7},{"name":"Plutonium","symbol":"Pu","number":94,"phase":"Solid","atomic_mass":244,"pos_row":10,"pos_col":8},{"name":"Americium","symbol":"Am","number":95,"phase":"Solid","atomic_mass":243,"pos_row":10,"pos_col":9},{"name":"Curium","symbol":"Cm","number":96,"phase":"Solid","atomic_mass":247,"pos_row":10,"pos_col":10},{"name":"Berkelium","symbol":"Bk","number":97,"phase":"Solid","atomic_mass":247,"pos_row":10,"pos_col":11},{"name":"Californium","symbol":"Cf","number":98,"phase":"Solid","atomic_mass":251,"pos_row":10,"pos_col":12},{"name":"Einsteinium","symbol":"Es","number":99,"phase":"Solid","atomic_mass":252,"pos_row":10,"pos_col":13},{"name":"Fermium","symbol":"Fm","number":100,"phase":"Solid","atomic_mass":257,"pos_row":10,"pos_col":14},{"name":"Mendelevium","symbol":"Md","number":101,"phase":"Solid","atomic_mass":258,"pos_row":10,"pos_col":15},{"name":"Nobelium","symbol":"No","number":102,"phase":"Solid","atomic_mass":259,"pos_row":10,"pos_col":16},{"name":"Lawrencium","symbol":"Lr","number":103,"phase":"Solid","atomic_mass":266,"pos_row":10,"pos_col":17},{"name":"Rutherfordium","symbol":"Rf","number":104,"phase":"Solid","atomic_mass":267,"pos_row":7,"pos_col":4},{"name":"Dubnium","symbol":"Db","number":105,"phase":"Solid","atomic_mass":268,"pos_row":7,"pos_col":5},{"name":"Seaborgium","symbol":"Sg","number":106,"phase":"Solid","atomic_mass":269,"pos_row":7,"pos_col":6},{"name":"Bohrium","symbol":"Bh","number":107,"phase":"Solid","atomic_mass":270,"pos_row":7,"pos_col":7},{"name":"Hassium","symbol":"Hs","number":108,"phase":"Solid","atomic_mass":269,"pos_row":7,"pos_col":8},{"name":"Meitnerium","symbol":"Mt","number":109,"phase":"Solid","atomic_mass":278,"pos_row":7,"pos_col":9},{"name":"Darmstadtium","symbol":"Ds","number":110,"phase":"Solid","atomic_mass":281,"pos_row":7,"pos_col":10},{"name":"Roentgenium","symbol":"Rg","number":111,"phase":"Solid","atomic_mass":282,"pos_row":7,"pos_col":11},{"name":"Copernicium","symbol":"Cn","number":112,"phase":"Gas","atomic_mass":285,"pos_row":7,"pos_col":12},{"name":"Nihonium","symbol":"Nh","number":113,"phase":"Solid","atomic_mass":286,"pos_row":7,"pos_col":13},{"name":"Flerovium","symbol":"Fl","number":114,"phase":"Solid","atomic_mass":289,"pos_row":7,"pos_col":14},{"name":"Moscovium","symbol":"Mc","number":115,"phase":"Solid","atomic_mass":289,"pos_row":7,"pos_col":15},{"name":"Livermorium","symbol":"Lv","number":116,"phase":"Solid","atomic_mass":293,"pos_row":7,"pos_col":16},{"name":"Tennessine","symbol":"Ts","number":117,"phase":"Solid","atomic_mass":294,"pos_row":7,"pos_col":17},{"name":"Oganesson","symbol":"Og","number":118,"phase":"Solid","atomic_mass":294,"pos_row":7,"pos_col":18},{"name":"Ununennium","symbol":"Uue","number":119,"phase":"Solid","atomic_mass":315,"pos_row":8,"pos_col":1}]}

symbols = []
for i in range(len(elements["elements"])):
    symbols.append(elements["elements"][i]["symbol"])

properties = ["name", "symbol", "number", "phase", "atomic_mass", "pos_row", "pos_col"]

table = '''  -----                                                               -----
1 | H |                                                               |He |
  |---+----                                       --------------------+---|
2 |Li |Be |                                       | B | C | N | O | F |Ne |
  |---+---|                                       |---+---+---+---+---+---|
3 |Na |Mg |3B  4B  5B  6B  7B |    8B     |1B  2B |Al |Si | P | S |Cl |Ar |
  |---+---+---------------------------------------+---+---+---+---+---+---|
4 | K |Ca |Sc |Ti | V |Cr |Mn |Fe |Co |Ni |Cu |Zn |Ga |Ge |As |Se |Br |Kr |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
5 |Rb |Sr | Y |Zr |Nb |Mo |Tc |Ru |Rh |Pd |Ag |Cd |In |Sn |Sb |Te | I |Xe |
  |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
6 |Cs |Ba |LAN|Hf |Ta | W |Re |Os |Ir |Pt |Au |Hg |Tl |Pb |Bi |Po |At |Rn |
  |---+---+---+------------------------------------------------------------
7 |Fr |Ra |ACT|
  -------------
              -------------------------------------------------------------
   Lanthanide |La |Ce |Pr |Nd |Pm |Sm |Eu |Gd |Tb |Dy |Ho |Er |Tm |Yb |Lu |
              |---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|
   Actinide   |Ac |Th |Pa | U |Np |Pu |Am |Cm |Bk |Cf |Es |Fm |Md |No |Lw |
              -------------------------------------------------------------'''


"""
Provide a menu of options for users to:
• See all the information that is stored about any element, by entering that element's symbol.
• Choose a property, and see that property for each element in the table.
"""

print("""
+------------------------------------------------+
|{introText:^48s}|
+------------------------------------------------+
""".format(introText="Welcome to periodic table application!"))

def showWholeTable():
    print(table)

def showElementInfo(symbol):
    if symbol not in symbols:
        print("Element doesn't exist in table, try again\n")
    else:
        for i in range(len(elements["elements"])):
            for k,v in elements["elements"][i].items():
                if v == symbol:
                    elName = elements["elements"][i]["name"]
                    elSymbol = elements["elements"][i]["symbol"]
                    elNumber = elements["elements"][i]["number"]
                    elPhase = elements["elements"][i]["phase"]
                    elMass = elements["elements"][i]["atomic_mass"]
                    elRow = elements["elements"][i]["pos_row"]
                    elCol = elements["elements"][i]["pos_col"]
                    print(
"""
+-------------------------------------------------------------------+
|   Element    | Symbol | Number | Atomic Mass | Phase  | Row | Col |
+-------------------------------------------------------------------+
|{elName:^14s}|{elSymbol:^8s}|{elNumber:^8d}|{elMass:^13f}|{elPhase:^8s}|{elRow:^5d}|{elCol:^5d}|
+-------------------------------------------------------------------+
""".format(elName=elName, elSymbol=elSymbol, elNumber=elNumber, elMass=elMass, elPhase=elPhase, elRow=elRow, elCol=elCol))

def elementsByProp(prop):
    if prop not in properties:
        print("Property doesn't exist, try again\n")
    else:
        for i in range(len(elements["elements"])):
            if prop == "name":
                print(elements["elements"][i]["name"])
            else:
                elName = elements["elements"][i]["name"]
                elProp = elements["elements"][i][prop]
                print(
"""
+--------------+--------------+
|   Element    |{propName:^14}|
+--------------+--------------+
|{elName:^14s}|{elProp:^14}|
+--------------+--------------+""".format(elName=elName, elProp=elProp, propName=prop))

def perTable():
    print("Choose an option and press enter: \n")
    print("[1] Show an element info by it's symbol: ")
    print("[2] Information about all elements by property")
    print("[3] Show the whole table")
    print("[4] Show the whole table (JSON)")
    option = input()
    
    if option == '1':
        print("Type desired element's symbol")
        el = input()
        showElementInfo(el)
        perTable()
    elif option == '2':
        print("Type desired property (available properties: name, symbol, number, phase, atomic_mass, pos_row, pos_col)")
        prop = input()
        elementsByProp(prop)
        perTable()
    elif option == '3':
        showWholeTable()
        perTable()
    elif option == '4':
        pprint.pprint(elements)
        perTable()
    else:
        print("Invalid option, try again")
        perTable()

perTable()
