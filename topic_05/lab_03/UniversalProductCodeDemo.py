from UniversalProductCode import UniversalProductCode

upc = UniversalProductCode("012345678905")
print(upc.is_valid())

upc = UniversalProductCode("OneTwoThree")
print(upc.is_valid())

upc = UniversalProductCode()
print(upc.is_valid())

upc = UniversalProductCode("Test")
print(upc.is_valid())
