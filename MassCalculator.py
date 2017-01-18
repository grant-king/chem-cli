__author__ = 'Grant King'

"""
The following sketch is the culmination of several weeks of building up a basic application while
working through a beginner's programming class.
Class: CIS122 Spring '16 
Lab 6 Description:
This is a calculator which accepts two inputs from the user and calculates the weight in grams of X moles 
of the provided molecule or element.

Input List:     
    string full_formula
    real mol_count

Output List:    
    string welcome_message
    string help_message
    int atomic_number
    string atomic_name
    string chemical_formula
    float subtotal
    float total
    string goodbye_message

Function/Module/Method List:
    Module main()
    Module welcome(string user_name)
    Module help_me()
    Module goodbye(string user_name)
    Module input_again(string invalid_input)
    Function string accept_user_input(string prompt, string in_type)    
    Function array parse_formula(string full_formula)
    Function real calculate_subtotal(array parsed_formula)    
    Function Boolean verify_help_input(string help_input)  
    Function int atom_quantity(string name)
    Function real mol_count(string formula)  
    Function real calculate_product(real num1, real num2)
    Function string generate_formula(string partial_formula, string atomic_symbol, quantity)
For Class ElementData:
    Module string get_symbols()
    Method string get_name(int atomic_number)
    Method real get_mass(int atomic_number)
For Class Verify:
    Method Boolean verify_symbol_input(string symbol_input)
    Method Boolean verify_qty_input(string atm_quantity_input)
    Method Boolean verify_mol_input(string mol_input)
    Method Boolean verify_formula_input(array parsed_formula)
"""

"""
class ElementData:
Set Private string array _name_data[119] = #all the element names in order
Set Private float array _mass_data[119] = #the atomic mass of each element in order
Set Private string array _symbol_data[119] = #the atomic symbol for each element in order

Public Method get_symbols(self):
        symbols = _symbol_data
        return symbols

Public Method string get_name(self, int atomic_number)
    Declare string list name_data
    Declare string name
    Set name = name_data[atomic_number]
    Return name
End Function

Public Method string get_number(self, string atomic_symbol)
    Declare string list symbol_data
    if atomic_symbol is found in symbol_data:
        return the index where it was found in symbol_data
    else:
        Display debugging message
    End if
End Function

Public Method real get_mass(self, int atomic_number)
    Declare real list mass_data
    Declare real mass
    Set mass = mass_data[atomic_number]
    return mass
End Function

"""
class ElementData:
    _name_data = [
    "Null", "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorous", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radon", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium" "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Ununtrium", "Flerovium", "Ununpentium", "Livermorium", "Ununseptium", "Ununoctium"]
    _mass_data = [
    0.0, 1.007, 4.002, 6.938, 9.012, 10.806, 12.0096, 14.006, 15.999, 18.998, 20.1797, 22.989, 24.304, 26.981, 28.084, 30.973, 32.059, 35.446, 39.948, 39.0983, 40.078, 44.955, 47.867, 50.9415, 51.9961, 54.938, 55.845, 58.933, 58.6934, 63.546, 65.38, 69.723, 72.630, 74.921, 78.971, 79.901, 83.798, 85.4678, 87.62, 88.905, 91.224, 92.906, 95.95, 98.0, 101.07, 102.905, 106.42, 107.8682, 112.414, 114.818, 118.710, 121.760, 127.60, 126.904, 131.293, 132.905, 137.327, 138.905, 140.116, 140.907, 144.242, 145, 150.36, 151.964, 157.25, 158.925, 162.500, 164.930, 167.259, 168.934, 173.054, 174.9668, 178.49, 180.947, 183.84, 186.207, 190.23, 192.217, 195.084, 196.966, 200.592, 204.382, 207.2, 208.980, 209, 210, 222, 223, 226, 227, 232.037, 231.035, 238.028, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 262, 267, 268, 271, 272, 270, 276, 281, 280, 285, 284, 289, 288, 293, 294, 294]
    
    _symbol_data = ["done", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr","Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Uut", "Fl", "Uup", "Lv", "Uus", "Uuo"]

    def get_symbols(self):
        symbols = _symbol_data
        return symbols

    def get_name(self, atomic_number):
        name = self._name_data[atomic_number]
        return name

    def get_number(self, atomic_symbol):
        if atomic_symbol in self._symbol_data:
            return self._symbol_data.index(atomic_symbol)

    def get_mass(self, atomic_number):
        mass = self._mass_data[atomic_number]
        return mass
    
"""
class Verify(ElementData):

    Public Method boolean verify_formula
        Declare boolean isValid_atm
        Declare boolean isValid_qty
        Declare string component
        Declare Integer parsed_length
        Declare Integer parsed_length_revised

        Set parsed_length = len(parsed_formula)
        Set parsed_length_revised = len(parsed_formula)
        While True:
            Counter-controlled loop from indicies 0 to end of parsed_formula array, stepping by 2:
                Set isValid_atm = False
                Set isValid_qty = False
                Set component = parsed_formula[counter]
                if component == '0':
                    return False
                else if component is alpha:
                    Set isValid_atm = verify_symbol_input(component)
                    if len(parsed_formula) == counter+1 or parsed_formula[x+1].isalpha():
                        Set parsed_formula.insert(counter+1, '1')
                        Set parsed_length_revised = parsed_length_revised + 1
                    end if
                    Set isValid_qty = verify_qty_input(parsed_formula[x+1])
                else:
                    return False
                end if
            end loop
            if parsed_length != len(parsed_formula):
                Set parsed_length = parsed_length_revised
            else:
                break
        End While
        
        if isValid_qty == False or isValid_atm == False:
            return False
        else:
            return True
        end if    

    Public Method boolean verify_symbol_input(string symbol_input)
        Declare string list symbol_data
        if symbol_input is found in _symbol_data:
            return True
        else:    
            return False
        End if
    End Method

    Method boolean verify_qty_input(int atm_quantity_input):
        Declare int int_val
        try to catch an exception:
            set int_val = int(atm_quantity_input)
            if int_val == 0:
                Display "atom removed"
            End if
            if int_val >= 0:
                return True
            else:
                Display "You may not have a negative atom quantity"
                return False
            End if
        if a ValueError exception is caught:
            return False
        End try
    End Method

    Method boolean verify_mol_input(float mol_input):
        Declare float_val
        try to catch an exception:
            Set float_val = float(mol_input)
            if float_val < = 0:
                return False
            End if
            return True
        if a ValueError is caught:
            return False
        End try
    End Method
"""
class Verify(ElementData):
    
    def verify_formula_input(self, compound):
        isValid_atm = False
        isValid_qty = False
        parsed_length = 0
        parsed_length_revised = 0
        component = '0'

        parsed_length = len(compound)
        parsed_length_revised = len(compound)
        while True:
            for x in range(0, parsed_length, 2):
                isValid_atm = False
                isValid_qty = False
                component = compound[x]
                if component == '0':
                    return False
                elif component.isalpha():
                    isValid_atm = self.verify_symbol_input(component)
                    if len(compound) == x+1 or compound[x+1].isalpha():
                        compound.insert(x+1, '1')
                        parsed_length_revised += 1
                    isValid_qty = self.verify_qty_input(compound[x+1])
                else:
                    return False
            if parsed_length != len(compound):
                parsed_length = parsed_length_revised
            else:
                break

        if isValid_qty == False or isValid_atm == False:
            return False
        else:
            return True

    def verify_symbol_input(self, symbol_input):
        if symbol_input in self._symbol_data:
            return True
        else:
            return False

    def verify_qty_input(self, atm_quantity_input):
        int_val = 0
        try:
            int_val = int(atm_quantity_input)
            if int_val == 0:
                print("atom removed")
            if int_val >= 0:
                return True
            else:
                print("You may not have a negative atom quantity ")
                return False
        except ValueError:
            return False

    def verify_mol_input(self, mol_input):
        float_val = 0.0
        try:
            float_val = float(mol_input)
            if float_val <= 0:
                return False
            return True
        except ValueError:
            return False

"""
Module welcome(string user_name)
    Declare string welcome_message
    Display welcome_message
    Verify input accept_user_input(welcome_message, 'help')
End Module
"""
def welcome(user_name):
    welcome_message = 'Welcome to the Molar Mass Calculator! If this is your first visit, '
    welcome_message += 'Please type \'help\' to view the instructions.  Otherwise, press ENTER to start! '

    print("Hey there " + user_name + "!")
    accept_user_input(welcome_message, 'help')

"""
Module help()
    Declare string help_message
    Display help_message
End Module
"""
def help_me():
    help_message = 'This program calculates the mass in grams for a given molarity of a substance or pure element. \n'
    help_message += 'Provide the input box with a molecular formula with each item separated by a \'.\' or the \n'
    help_message += 'atomic symbol for a single atom and press ENTER to be prompted for the desired molarity. \n \n'
    help_message += 'For example, if you want to enter the formula for sand, type \'Si.O.2\' or try \'C.6.H.12.O.6\' \n'
    help_message += 'for glucose. Pure elements such as Gold can be entered by only typing the element\'s symbol, \'Au\' \n' 
    help_message += 'in this case, and pressing ENTER.\n'
    print(help_message)

"""
Module goodbye(string user_name)
    Declare string goodbye_message
    Display goodbye_message
"""
def goodbye(user_name):
    goodbye_message = "Goodbye "
    print(goodbye_message, user_name, "!", sep="")

"""
Function string accept_user_input(string prompt, string in_type)
    Declare string temp_input
    Declare boolean isValid
    Declare string temp_input
    Set thisFormula = New Verify()

    Set isValid = False 
    while(not isValid)   
        Set temp_input = input(prompt)
        if temp_input == 'cancel':
            exit(0)
        End if
        if in_type == 'formula':
            set parsed_formula = parse_formula(temp_input)
            set isValid = thisFormula.verify_formula_input(parsed_formula)
        else if in_type == 'symbol':
            isValid = thisFormula.verify_symbol_input(temp_input)            
        else if in_type == 'atm_count':
            isValid = thisFormula.verify_qty_input(temp_input)            
        else if in_type == 'mol_count':
            isValid = thisFormula.verify_mol_input(temp_input)            
        else if in_type == 'help':
            isValid = verify_help_input(temp_input)
        End if
        if isValid == False:
            input_again(temp_input)
        End if
    End while

    if in_type == 'formula':
        return parsed_formula
    end if
    return str(temp_input)
End Function
"""
def accept_user_input(prompt, in_type):
    temp_input = ""
    isValid = False
    thisFormula = Verify()
    
    while(not isValid):
        temp_input = input(prompt)
        if temp_input == 'cancel':
            exit(0)
        if in_type == 'formula':
            parsed_formula = parse_formula(temp_input)
            isValid = thisFormula.verify_formula_input(parsed_formula)            
        elif in_type == 'atm_count':
            isValid = thisFormula.verify_qty_input(temp_input)            
        elif in_type == 'mol_count':
            isValid = thisFormula.verify_mol_input(temp_input)            
        elif in_type == 'help':
            isValid = verify_help_input(temp_input)
        if isValid == False:
            input_again(temp_input)

    if in_type == 'formula':
        return parsed_formula
    return str(temp_input)

"""
Function array parse_formula(string full_formula)
    Set array parsed_formula = array whose elements are determined by splitting the string at the special character '.'
    return parsed_formula
"""
def parse_formula(full_formula):
    parsed_formula = full_formula.split(".")
    return parsed_formula

"""
Function real calculate_subtotal(array parsed_formula)
    Declare subtotal 
    Declare mass
    Declare quantity 
    Declare list_length
    Declare component
    Declare atomic_number
    Declare ElementData this_element
    Set thisElement = New ElementData()

    Set list_length = len(parsed_formula)
    Counter-controlled loop from indicies 0 to end of parsed_formula array, stepping by 2:
        Set component = parsed_formula[counter]
        Set atomic_number = thisElement.get_number(component)
        Set mass = thisElement.get_mass(atomic_number)
        Set quantity = parsed_formula[counter+1]
        Set subtotal += calculate_product(mass, quantity)
    end loop
    return subtotal
"""
def calculate_subtotal(parsed_formula):
    subtotal = 0.00
    mass = 0.00
    quantity = 0
    list_length = 0
    component = '0'
    atomic_number = 0
    thisElement = ElementData()

    list_length = len(parsed_formula)
    for x in range(0, list_length, 2):
        component = parsed_formula[x]
        atomic_number = thisElement.get_number(component)
        mass = thisElement.get_mass(atomic_number)
        quantity = parsed_formula[x+1]
        subtotal += calculate_product(mass, quantity)
    return subtotal

"""
Function boolean verify_help_input(string help_input):
    if help_input == ''
        return True
    else if help_input == 'help' or help_input == 'Help':
        help_me()
        return True
    else:
        return False
    End if
End Function
"""
def verify_help_input(help_input):
    if help_input == '':
        return True
    elif help_input == 'help' or help_input == 'Help':
        help_me()
        return True
    else:
        return False

"""
Function input_again(invalid_input):
    Display invalid_input + "is not a valid input.  Please try again or type \'cancel\' to exit this application"
End Function
"""
def input_again(invalid_input):
   print("\'" + invalid_input + "\' is not a valid input.  Please try again or type \'cancel\' to exit this application")

"""
Function array get_formula:
    Set parsed_formula = accept_user_input("Please provide an atom or molecular formula: ", 'formula')
    return parsed_formula
"""
def get_formula():
    parsed_formula = accept_user_input("Please Provide an atom or molecular formula: ", 'formula')
    return parsed_formula

"""
Function real get_mol_count(string formula )
    Declare real moles
    Set moles = accept_user_input("How many moles of" + formula + "would you like to calculate the mass for?", 'mol_count')
    Return float(moles)
End Function
"""
def get_mol_count(formula):
    moles = 0.0
    moles = accept_user_input(("How many moles of " + formula + " would you like to calculate the mass for? "), 'mol_count')
    return float(moles)

""" 
Function float calculate_product(real num1, real num2)
    Declare real product
    Set product = num1 * num2
    Return product
End Function
"""
def calculate_product(num1, num2):
    product = 0.0
    product = float(num1) * float(num2)
    return product

"""
Function string generate_formula(string partial_formula, string atomic_symbol, int quantity):
    Declare string chemical_formula
    Set chemical_formula = partial_formula
    if quantity is not = 0:
        Set chemical_formula = chemical_formula + atomic_symbol
    End if
    if quantity > 1:
        Set chemical_formula = chemical_formula + string(quantity)
    End if
End Function
"""
def generate_formula(parsed_formula):
    chemical_formula = ''
    for x in range (len(parsed_formula)):
        if parsed_formula[x] != '1':
            chemical_formula += parsed_formula[x]
    return chemical_formula

"""
Module main()
    Declare real subtotal
    Declare real total
    Declare string user_name
    Declare chemical_formula
    Declare list parsed_formula

    Set user_name = "User"
    Call welcome(user_name)
    Set parsed_formula = get_formula()
    Set subtotal = calculate_subtotal(parsed_formula)
    if len(parsed_formula) == 2:
        Set New Element = ElementData()
        atomic_number = Element.lookup_atom_number(parsed_formula[0])
        chemical_formula = Element.lookup_atom_name(atomic_number)
    else:
        chemical_formula = generate_formula(parsed_formula)
    end if
    Set mol_count = get_mol_count(chemical_formula)
    Set total = calculate_product(subtotal, mol_count)
    Display mol_count, "mol of", chemical_formula, "weighs approximately", total, "grams"
    Call goodbye(user_name)
End Module
"""
def main():
    subtotal = 0.0
    total = 0.0
    user_name = "User"
    chemical_formula = ""
    parsed_formula = ['']

    welcome(user_name)
    parsed_formula = get_formula()
    subtotal = calculate_subtotal(parsed_formula)
    if len(parsed_formula) == 2:
        Element = ElementData()
        atomic_number = Element.get_number(parsed_formula[0])
        chemical_formula = Element.get_name(atomic_number)
    else:
        chemical_formula = generate_formula(parsed_formula)
    mol_count = get_mol_count(chemical_formula)
    total = calculate_product(subtotal, mol_count)
    print(mol_count, "mol of", chemical_formula, "weighs approximately", '%.3f' % total, "grams")
    goodbye(user_name)
    
main()
