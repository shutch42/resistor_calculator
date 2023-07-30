import csv


def parse_csv(filename):
    resistors = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            for cell in row:
                if 'k' in cell:
                    resistors[float(cell[:-1]) * 1000] = cell
                elif 'M' in cell:
                    resistors[float(cell[:-1]) * 1000000] = cell
                else:
                    resistors[float(cell)] = cell

    return resistors


def calc_amplifier(v_in, v_out, resistors):
    ratio = v_out/v_in - 1
    r_in = list(resistors.keys())[0]
    r_out = list(resistors.keys())[0]
    best_error = ratio - 1
    for resistor_1 in resistors:
        for resistor_2 in resistors:
            curr_error = abs(resistor_2/resistor_1 - ratio)
            if curr_error < best_error:
                r_in = resistor_1
                r_out = resistor_2
                best_error = curr_error

    print(f"Use a {resistors[r_in]} ohm input resistor, and a {resistors[r_out]} ohm output resistor")
    print(f"This will give an output voltage of exactly {(1 + r_out/r_in) * v_in}V")
    print(f"This meets the desired output of {v_out}V with an error of {best_error * 100}%")


def calc_divider(v_in, v_out, resistors):
    ratio = v_out/v_in
    r1 = list(resistors.keys())[0]
    r2 = list(resistors.keys())[0]
    best_error = abs(ratio - 1/2)
    for resistor_1 in resistors:
        for resistor_2 in resistors:
            curr_error = abs(resistor_2/(resistor_1 + resistor_2) - ratio)
            if curr_error < best_error:
                r1 = resistor_1
                r2 = resistor_2
                best_error = curr_error

    print(f"Use a {resistors[r1]} ohm resistor, and a {resistors[r2]} ohm resistor to ground")
    print(f"This will give an output voltage of exactly {(r2/(r1 + r2)) * v_in}V")
    print(f"This meets the desired output of {v_out}V with an error of {best_error * 100}%")


def make_circuit(v_in, v_out):
    if v_in == v_out:
        print("Just use the input voltage lol")
    else:
        resistors = parse_csv("resistors.csv")
        if v_in < v_out:
            print("Non-inverting amplifier:")
            calc_amplifier(v_in, v_out, resistors)
        else:
            print("Voltage divider:")
            calc_divider(v_in, v_out, resistors)


voltage_in = float(input("Enter input voltage: "))
voltage_out = float(input("Enter desired output voltage: "))
print()
make_circuit(voltage_in, voltage_out)
