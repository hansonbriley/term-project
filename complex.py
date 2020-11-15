import cmath;

c = 1 + 2j;
print("Type:", type(c));
print("Real:", c.real);
print("Imaginary:", c.imag);
print("Phase:" , cmath.phase(c));
print("Polar coordinates:", cmath.polar(c));
