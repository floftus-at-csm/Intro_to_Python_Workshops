# Creating an empty array
empty_array = []

empty_array.append(100) # adding a value to that array
print(empty_array)

# empty_array[3] = 1 # this will give an error because the third position does not exist
# print(empty_array)

empty_array = empty_array * 3 # making the array longer
print(empty_array)

genres = ["rock", "hip hop", "dance"]
print(genres[0])
genres[2] = "classical"
print(genres[2])

del genres[0]
print(genres)
genres.append("heavy metal")
genres.remove("classical")
print(genres)