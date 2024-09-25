"""
A list of antiques held by .... museum
whose insurance needs to be updated
"""


# a function to create a list of all antique items
def get_antiques_list():
    # the data is name of item, type of item, current insurance
    Flagon = ['Flagon', 'Silverware', 300]
    Onyx_cameo = ['Onyx_cameo', 'Jewelry', 200]
    Tea_urn = ['Tea_urn', 'Silverware', 900]
    Stone_axe = ['Stone_axe', 'Aboriginal', 200]
    Didjeridu = ['Didjeridu', 'Aboriginal', 500]
    Log_canoe = ['Log_canoe', 'Aboriginal', 500]
    Oak_chest = ['Oak_chest', 'Furniture', 250]
    Astrolabe = ['Astrolabe', 'Machinery', 500]
    Cream_jug = ['Cream_jug', 'Silverware', 200]
    Fire_drill = ['Fire_drill', 'Aboriginal', 900]
    Theodolite = ['Theodolite', 'Machinery', 500]
    Loving_cup = ['Loving_cup', 'Silverware', 100]
    Fish_knife = ['Fish_knife', 'Silverware', 200]
    Nailsea_jug = ['Nailsea_jug', 'Glassware', 50]
    Minton_vase = ['Minton_vase', 'Porcelain', 100]
    Wine_taster = ['Wine_taster', 'Silverware', 200]
    Carved_pipes = ['Carved_pipes', 'Aboriginal', 400]
    Tiffany_lamp = ['Tiffany_lamp', 'Glassware', 800]
    Hamburg_dish = ['Hamburg_dish', 'Porcelain', 600]
    Spear_thrower = ['Spear_thrower', 'Aboriginal', 100]
    Fishing_spear = ['Fishing_spear', 'Aboriginal', 400]
    Wooden_dishes = ['Wooden_dishes', 'Aboriginal', 600]
    Rocking_horse = ['Rocking_horse', 'Furniture', 200]

    antiques = [Flagon, Onyx_cameo, Tea_urn, Stone_axe, Didjeridu, Log_canoe, Oak_chest,
                Astrolabe, Cream_jug, Fire_drill, Theodolite, Loving_cup,
                Fish_knife, Nailsea_jug, Minton_vase, Wine_taster, Carved_pipes,
                Tiffany_lamp, Hamburg_dish, Spear_thrower, Fishing_spear, Wooden_dishes, Rocking_horse]

    return antiques


def new_insured_value(item):
    if item[1] == 'Silverware' and item[2] <= 300:
        new_insurance = item[2] * 1.2
    elif item[1] == 'Aboriginal' and item[2] < 200:
        new_insurance = item[2] * 1.2
    else:
        new_insurance = item[2] * 1.1
    return int(new_insurance)


antiques_list = get_antiques_list()

print('Item Name      Type           Old Ins   New Ins')
for antique in antiques_list:
    print_out = antique[0]
    while len(print_out) < 15: print_out += ' '
    print_out += antique[1]
    while len(print_out) < 30: print_out += ' '
    print_out += '$' + str(antique[2])
    while len(print_out) < 40: print_out += ' '
    print_out += '$' + str(new_insured_value(antique))
    print(print_out)
