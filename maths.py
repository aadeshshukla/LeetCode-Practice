# lets write code for maths formulas 
# code to find the area of a circle
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# code to find the circumference of a circle
def circumference_of_circle(radius):
    return 2 * math.pi * radius

# code to find the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# code to find the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# code to find the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# code to find the perimeter of a triangle
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

# code to find the area of a square
def area_of_square(side):
    return side ** 2

# code to find the perimeter of a square
def perimeter_of_square(side):
    return 4 * side

# code to find the area of a parallelogram
def area_of_parallelogram(base, height):
    return base * height

# code to find the perimeter of a parallelogram
def perimeter_of_parallelogram(side1, side2):
    return 2 * (side1 + side2)

# area of triangle using heron's formula
def area_of_triangle_heron(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# lcm
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# hcf
def hcf(a, b):
    return math.gcd(a, b)

# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# power
def power(base, exponent):
    return base ** exponent

# code to solve quadratic equation
def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return "No real roots"
    elif d == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1, root2

# code to find the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# code to find the midpoint between two points
def midpoint_between_points(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

# code to find the slope of a line
def slope_of_line(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Undefined"
    else:
        return (y2 - y1) / (x2 - x1)
    
# code to find factors of a number
def factors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

# code to find prime factors of a number
def prime_factors(n):
    result = []
    for i in range(2, n + 1):
        while n % i == 0:
            result.append(i)
            n //= i
    return result

# code to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# code to find the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# code to find the product of digits of a number
def product_of_digits(n):
    product = 1
    for digit in str(n):
        product *= int(digit)
    return product

# code to find the reverse of a number
def reverse_number(n):
    return int(str(n)[::-1])

# code to check if a number is palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# code to find the gcd of two numbers
def gcd(a, b):
    return math.gcd(a, b)

# code to find determinant of a 2x2 matrix
def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Matrix must be 2x2")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# code to find determinant of a 3x3 matrix
def determinant_3x3(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        raise ValueError("Matrix must be 3x3")
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

# code to find the inverse of a 2x2 matrix
def inverse_2x2(matrix):
    det = determinant_2x2(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    return [[matrix[1][1] / det, -matrix[0][1] / det],
            [-matrix[1][0] / det, matrix[0][0] / det]]

# code to find the inverse of a 3x3 matrix
def inverse_3x3(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    inv = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    inv[0][0] = (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) / det
    inv[0][1] = (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) / det
    inv[0][2] = (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) / det
    inv[1][0] = (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) / det
    inv[1][1] = (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) / det
    inv[1][2] = (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) / det
    inv[2][0] = (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) / det
    inv[2][1] = (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) / det
    inv[2][2] = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) / det
    return inv

# code to find the transpose of a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# code to find logarithm of a number
def logarithm(value, base=math.e):
    if value <= 0:
        raise ValueError("Logarithm is undefined for non-positive values")
    return math.log(value, base)

print(logarithm(100, 10))  # Output: 2.0
m=[[1, 2, 3], [0, 1, 4], [5, 6, 0]]
print(inverse_3x3(m))


# code to find bitwise AND of two numbers
def bitwise_and(a, b):
    return a & b

# code to find bitwise OR of two numbers
def bitwise_or(a, b):
    return a | b

def percentage(value ,total):
    return (value / total) * 100

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time, n=1):
    return principal * (1 + rate / (100 * n)) ** (n * time) - principal

def interest(principal, rate, time, n=1, compound=False):
    if compound:
        return compound_interest(principal, rate, time, n)
    else:
        return simple_interest(principal, rate, time)
    
def mass_to_weight(mass, gravity=9.81):
    return mass * gravity

def weight_to_mass(weight, gravity=9.81):
    return weight / gravity

def distance(speed, time):
    return speed * time

def speed(distance, time):
    return distance / time

def time(distance, speed):
    return distance / speed

def acceleration(force, mass):
    return force / mass

def force(mass, acceleration):
    return mass * acceleration

def mass(force, acceleration):
    return force / acceleration

def work(force, distance):
    return force * distance

def velocity(displacement, time):
    return displacement / time

def displacement(velocity, time):
    return velocity * time

def power_work(work, time):
    return work / time

def power_energy(energy, time):
    return energy / time

def energy_power(power, time):
    return power * time

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def potential_energy(mass, gravity, height):
    return mass * gravity * height

def momentum(mass, velocity):
    return mass * velocity

def impulse(force, time):
    return force * time
def pressure(force, area):
    return force / area

def density(mass, volume):
    return mass / volume

def buoyant_force(density_fluid, volume_displaced, gravity=9.81):
    return density_fluid * volume_displaced * gravity

def specific_heat(heat, mass, temperature_change):
    return heat / (mass * temperature_change)

def thermal_conductivity(heat_transfer, area, temperature_difference, thickness):
    return (heat_transfer * thickness) / (area * temperature_difference)

def ohms_law(voltage, current):
    return voltage / current

def resistance(voltage, current):
    return voltage / current

def current(voltage, resistance):
    return voltage / resistance

def voltage(current, resistance):
    return current * resistance

def capacitance(charge, voltage):
    return charge / voltage

def charge(capacitance, voltage):
    return capacitance * voltage

def voltage_from_charge(capacitance, charge):
    return charge / capacitance

def inductance(voltage, current, time):
    return (voltage * time) / current

def magnetic_flux(density, area):
    return density * area

def faradays_law(inductance, current_change, time):
    return inductance * (current_change / time)

def coulombs_law(charge1, charge2, distance):
    k = 8.9875517873681764e9  # Coulomb's constant in N·m²/C²
    return k * (charge1 * charge2) / (distance ** 2)

def gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11  # Gravitational constant in m³/kg/s²
    return G * (mass1 * mass2) / (distance ** 2)

def escape_velocity(mass, radius):
    G = 6.67430e-11  # Gravitational constant in m³/kg/s²
    return math.sqrt((2 * G * mass) / radius)

def orbital_period(radius, mass):
    G = 6.67430e-11  # Gravitational constant in m³/kg/s²
    return 2 * math.pi * math.sqrt((radius ** 3) / (G * mass))

def centripetal_force(mass, velocity, radius):
    return (mass * velocity ** 2) / radius

def centripetal_acceleration(velocity, radius):
    return (velocity ** 2) / radius

def angular_velocity(angular_displacement, time):
    return angular_displacement / time

def angular_acceleration(angular_velocity_change, time):
    return angular_velocity_change / time

def torque(force, lever_arm):
    return force * lever_arm

def moment_of_inertia(mass, radius):
    return mass * (radius ** 2)

def angular_momentum(moment_of_inertia, angular_velocity):
    return moment_of_inertia * angular_velocity

def work_done(force, displacement, angle):
    return force * displacement * math.cos(math.radians(angle))

def power(force, velocity, angle):
    return force * velocity * math.cos(math.radians(angle))

def efficiency(output_energy, input_energy):
    return (output_energy / input_energy) * 100

def mechanical_advantage(output_force, input_force):
    return output_force / input_force

def velocity_from_momentum(momentum, mass):
    return momentum / mass

def momentum_from_velocity(mass, velocity):
    return mass * velocity

def kinetic_energy_from_momentum(momentum, mass):
    return (momentum ** 2) / (2 * mass)

def momentum_from_kinetic_energy(kinetic_energy, mass):
    return math.sqrt(2 * kinetic_energy * mass)

def work_from_power(power, time):
    return power * time

def power_from_work(work, time):
    return work / time  

def gravitational_potential_energy(mass, gravity, height):
    return mass * gravity * height

def spring_constant(force, displacement):
    return force / displacement

def frequency(wavelength, speed):
    return speed / wavelength

def wavelength(frequency, speed):
    return speed / frequency

def wave_speed(frequency, wavelength):
    return frequency * wavelength

def doppler_effect(frequency_source, velocity_source, velocity_observer, speed_of_sound):
    return frequency_source * ((speed_of_sound + velocity_observer) / (speed_of_sound - velocity_source))

def refractive_index(speed_of_light, speed_in_medium):
    return speed_of_light / speed_in_medium

def snells_law(angle_of_incidence, refractive_index1, refractive_index2):
    return math.asin((refractive_index1 / refractive_index2) * math.sin(math.radians(angle_of_incidence)))

def lens_formula(focal_length, object_distance, image_distance):
    return (1 / focal_length) == (1 / object_distance) + (1 / image_distance)

def magnification(image_height, object_height):
    return image_height / object_height

def focal_length_from_lens_formula(object_distance, image_distance):
    return 1 / ((1 / object_distance) + (1 / image_distance))

def image_distance_from_lens_formula(focal_length, object_distance):
    return 1 / ((1 / focal_length) - (1 / object_distance))     

def object_distance_from_lens_formula(focal_length, image_distance):
    return 1 / ((1 / focal_length) - (1 / image_distance))

def critical_angle(refractive_index1, refractive_index2):
    if refractive_index1 <= refractive_index2:
        raise ValueError("Refractive index of the first medium must be greater than that of the second medium")
    return math.degrees(math.asin(refractive_index2 / refractive_index1))

def total_resistance_series(*resistances):
    return sum(resistances)

def total_resistance_parallel(*resistances):
    return 1 / (1 / sum(resistances))

def total_capacitance_series(*capacitances):
    return 1 / (1 / sum(capacitances))

def total_capacitance_parallel(*capacitances):
    return sum(capacitances)

def total_inductance_series(*inductances):
    return sum(inductances)

def total_inductance_parallel(*inductances):
    return 1 / (1 / sum(inductances))

def wave_number(wavelength):
    return 2 * math.pi / wavelength

def angular_frequency(frequency):
    return 2 * math.pi * frequency

def phase_difference(time_difference, period):
    return (time_difference / period) * 360

def time_period(frequency):
    return 1 / frequency

def frequency_from_time_period(time_period):
    return 1 / time_period

def amplitude_from_energy(energy, mass):
    return math.sqrt((2 * energy) / mass)

def energy_from_amplitude(amplitude, mass):
    return 0.5 * mass * (amplitude ** 2)

def wave_velocity(wavelength, frequency):
    return wavelength * frequency

def sound_intensity(power, area):
    return power / area

def sound_level(intensity, reference_intensity=1e-12):
    return 10 * math.log10(intensity / reference_intensity)

def decibel_change(initial_intensity, final_intensity):
    return 10 * math.log10(final_intensity / initial_intensity)

def power_from_intensity(intensity, area):
    return intensity * area

def intensity_from_power(power, area):
    return power / area

def sound_speed(temperature):
    return 331.3 + (0.606 * temperature)  # Speed of sound in m/s at given temperature in Celsius

def doppler_shifted_frequency(frequency_source, velocity_source, velocity_observer, speed_of_sound):
    return frequency_source * ((speed_of_sound + velocity_observer) / (speed_of_sound - velocity_source))

def sound_wavelength(frequency, speed_of_sound):
    return speed_of_sound / frequency

def sound_frequency(wavelength, speed_of_sound):
    return speed_of_sound / wavelength

def sound_period(frequency):
    return 1 / frequency

def sound_amplitude_from_intensity(intensity, density, speed_of_sound):
    return math.sqrt((2 * intensity) / (density * speed_of_sound))

def sound_intensity_from_amplitude(amplitude, density, speed_of_sound):
    return 0.5 * density * speed_of_sound * (amplitude ** 2)

def sound_pressure_from_intensity(intensity, density, speed_of_sound):
    return math.sqrt(intensity * density * speed_of_sound)

def sound_intensity_from_pressure(pressure, density, speed_of_sound):
    return (pressure ** 2) / (density * speed_of_sound)

def sound_level_from_pressure(pressure, reference_pressure=20e-6):
    return 20 * math.log10(pressure / reference_pressure)

def pressure_from_sound_level(sound_level, reference_pressure=20e-6):
    return reference_pressure * (10 ** (sound_level / 20))

def sound_level_change(initial_pressure, final_pressure):
    return 20 * math.log10(final_pressure / initial_pressure)

def sound_intensity_change(initial_pressure, final_pressure, density, speed_of_sound):
    initial_intensity = sound_intensity_from_pressure(initial_pressure, density, speed_of_sound)
    final_intensity = sound_intensity_from_pressure(final_pressure, density, speed_of_sound)
    return 10 * math.log10(final_intensity / initial_intensity)

def sound_power_from_intensity(intensity, area):
    return intensity * area

def sound_intensity_from_power(power, area):
    return power / area

# chemistry formulas

def moles(mass, molar_mass):
    return mass / molar_mass

def molar_mass(mass, moles):
    return mass / moles

def mass(moles, molar_mass):
    return moles * molar_mass

def concentration(moles, volume):
    return moles / volume

def volume(moles, concentration):
    return moles / concentration

def ideal_gas_law(pressure, volume, moles, temperature):
    R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
    return (pressure * volume) / (moles * R * temperature)

def pressure_from_ideal_gas_law(moles, temperature, volume):
    R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
    return (moles * R * temperature) / volume

def volume_from_ideal_gas_law(moles, temperature, pressure):
    R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
    return (moles * R * temperature) / pressure

def temperature_from_ideal_gas_law(moles, pressure, volume):
    R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
    return (pressure * volume) / (moles * R)

def density_from_ideal_gas_law(moles, molar_mass, volume):
    return (moles * molar_mass) / volume

def molar_mass_from_ideal_gas_law(moles, density, volume):
    return (moles * density) / volume

def stoichiometry(moles_reactant, moles_product, coefficient_reactant, coefficient_product):
    return (moles_reactant * coefficient_product) / coefficient_reactant

def coefficient_from_stoichiometry(moles_reactant, moles_product, coefficient_reactant):
    return (moles_product * coefficient_reactant) / moles_reactant

def limiting_reactant(moles_reactant1, moles_reactant2, coefficient_reactant1, coefficient_reactant2):
    ratio1 = moles_reactant1 / coefficient_reactant1
    ratio2 = moles_reactant2 / coefficient_reactant2
    if ratio1 < ratio2:
        return "Reactant 1 is the limiting reactant"
    elif ratio2 < ratio1:
        return "Reactant 2 is the limiting reactant"
    else:
        return "Both reactants are in stoichiometric proportion"
    
def percent_yield(actual_yield, theoretical_yield):
    return (actual_yield / theoretical_yield) * 100


def empirical_formula(moles_elements):
    total_moles = sum(moles_elements)
    return [mole / total_moles for mole in moles_elements]

def molecular_formula(empirical_formula, molar_mass_empirical, molar_mass_molecular):
    ratio = molar_mass_molecular / molar_mass_empirical
    return [int(round(coef * ratio)) for coef in empirical_formula]

def dilution(concentration_initial, volume_initial, concentration_final):
    return (concentration_initial * volume_initial) / concentration_final

def percent_composition(mass_element, mass_compound):
    return (mass_element / mass_compound) * 100

def molarity(moles_solute, volume_solution):
    return moles_solute / volume_solution

def molality(moles_solute, mass_solvent):
    return moles_solute / mass_solvent

def normality(equivalents_solute, volume_solution):
    return equivalents_solute / volume_solution

def equivalents(moles_solute, valence):
    return moles_solute * valence

def valence(equivalents, moles_solute):
    return equivalents / moles_solute

def osmolarity(moles_solute, volume_solution):
    return moles_solute / volume_solution

def osmotic_pressure(molarity, temperature):
    R = 0.0821  # Ideal gas constant in L·atm/(K·mol)
    return molarity * R * temperature

def freezing_point_depression(kf, molality):
    return kf * molality

def boiling_point_elevation(kb, molality):
    return kb * molality

def raoult_law(mole_fraction_solvent, vapor_pressure_solvent):
    return mole_fraction_solvent * vapor_pressure_solvent   

def henrys_law(henrys_constant, concentration):
    return henrys_constant * concentration

def rate_of_reaction(concentration_initial, concentration_final, time):
    return (concentration_final - concentration_initial) / time

# 
# 
# 