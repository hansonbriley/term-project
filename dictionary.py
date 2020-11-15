# Initialize dictionary with random husky players
huskies = { 
        'Molden': 3, 
        'Morris': 9, 
        'Bowman': 55, 
        'Gordan': 2, 
        'McGrew': 5, 
        'Newton': 6, 
        'Spiker': 8};

# Print type of huskies
print("Type:", type(huskies));
print();

# Print values and keys 
print("All values:", huskies);
print();

# Print only keys
print("Keys:", list(huskies));
print();

# Print only keys sorted
print("Keys sorted:", sorted(huskies));
print();

# Iterate through dictionary
for key, value in huskies.items():
    print("Name:", key, "Number:", value);
print();

# Checking if a value is in the dictionary
if 'Bowman' in huskies:
    print("Bowman found in dictionary");
print();

# Dictionary length
print("Dictionary length:", len(huskies));

# Adding new values to dictionary


huskies["Sirmon"] = 4;
print('Adding new value to dictionary with: huskies["Sirmon"] = 4');

print(huskies);
