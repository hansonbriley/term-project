# Initialize dictionary with random husky players
huskies = { 
        3: 'Molden', 
        9: 'Morris', 
        2: 'Gordon', 
        5: 'McGrew', 
        6: 'Newton', 
        8: 'Spiker'};

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
    print("Number:", key, "Name:", value);
print();

# Search for value
print(huskies.get(5));
print();

# Dictionary length
print("Dictionary length:", len(huskies));
print();

print(huskies);
print();

# Using non-unique key
huskies[5] = "Bowman";
print("Using non-unique key with huskies[5] = 'Bowman'");
print(huskies);
print();

# Adding new values to dictionary
huskies[4] = 'Sirmon';
print("Adding new value to dictionary with: huskies[4] = 'Sirmon'");
print();

print("Dictionary length:", len(huskies));
print();

print(huskies);
print();

# Delete value
del huskies[5];
print("Delete values using 'del huskies[key]'");
print();
print("Dictionary length:", len(huskies));
