#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="fido", breed="Mastiff"):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "fido"  # Default value if invalid

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds or value == "Mastiff":
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mastiff"  # Default value if invalid
