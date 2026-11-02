# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)
Tuplex=("gold", "food", "shoes", 3,2,1)
print (Tuplex)
Tuplex1=(6,7,4,3,9,1)
print (Tuplex1)
Tuplex1=Tuplex1+(9,)
print(Tuplex1)
Tuplex2=(50,40,50,30,20,50,50,50)
print(Tuplex2.count(50))
Slice=Tuplex2[3:5]
print(Slice)
Slice1=Tuplex2[:8]
print(Slice1)

# 7) Slice from the beginning when the start index is not provided:

# a) Use `tuplex[:6]` to get elements from index 0 up to index 5.

# b) Store it in `_slice` and print it.