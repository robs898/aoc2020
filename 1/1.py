def calculate_fuel(mass):
    mass2 = int(mass / 3)
    return mass2 - 2

mass_list = [line.rstrip('\n') for line in open('1/1.txt')]

fuel_list = [calculate_fuel(int(mass)) for mass in mass_list]

print(sum(fuel_list))