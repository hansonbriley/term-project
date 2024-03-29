import cmath;

# Initialize complex number com_num
com_num = 1 + 2j;

# Print the type of com_num
print("Type:", type(com_num));
print();

# Print com_num real part
print("Real:", com_num.real);
print();

# Print com_num imaginary part
print("Imaginary:", com_num.imag);
print();

# Print phase
print("Phase:" , cmath.phase(com_num));
print();

# Print polar coordinates
print("Polar coordinates:", cmath.polar(com_num));

