doctorsWho={
"Pierwszy": "William Hartnell",
"2": "Patrick Troughton",
"3": "Jon Pertwee",
"4": "Tom Baker",
"5": "Peter Davison",
"6": "Colin Baker",
"7": "Sylvester McCoy",
"8": "Paul McGann",
"9": "Christopher Eccleston",
10: "David Tennant",
"11": "Matt Smith",
"12": "Peter Capaldi",
"Trzynasta": "Jodie Whittaker"}
print ("Kowalski" in doctorsWho) # False (niestety!)
for key in doctorsWho:
    print(f" {key} - {doctorsWho[key]}")

print(doctorsWho[10]) # Wypisze: David Tennant
print(doctorsWho["Trzynasta"])

print ("Kowalski" in doctorsWho)# wypisze False.
del doctorsWho["Pierwszy"]
#doctorsWho.pop("Pierwszy") # Lub: del doctorsWho["Pierwszy"].
Movies={
    "One" : "Lord Of the rings",
    "Two" : "Harry potter",
    "Three": "Matrix"
}
Movies.update({"Four": "Godfather"})

print(Movies)
Movies.update({"One": "Saw"})
print(Movies)
Movies.clear()
print(Movies)
Movies={
    "One" : "Lord Of the rings",
    "Two" : "Harry potter",
    "Three": "Matrix"
}
print(Movies.get("One"))

print(Movies.keys())

