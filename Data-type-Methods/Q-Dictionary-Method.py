                # Python Dictionary Practice Questions

                # Question NO 01
# Ek dictionary d = {"a": 1, "b": 2} me key "c" ka value safely check karne ke liye kaunsa method use karoge?
# d = {"a": 1, "b": 2}


                # Question NO 02
# Dictionary d = {"name": "Ali", "age": 20} me sirf keys ka list kaise nikaaloge?
# d = {"name": "Ali", "age": 20}
# print(d.keys())


                # Question NO 03
# Dictionary ke saare values ka list kaise nikaaloge?
# d = {"name": "Ali", "age": 20}
# print(d.items())


                # Question NO 04
# Dictionary me key-value pairs ko tuple ke form me kaise nikaaloge?
# d = {"name": "Ali", "age": 20}
# print(d.items())


                # Question NO 05
# Ek dictionary me "age" ka value remove karne ka method kaunsa hai?
# d = {"name": "Ali", "age": 20}
# print(d.pop("age"))


                # Question NO 06
# Last inserted key-value pair ko remove + return karne ka method kaunsa hai?
# d = {"name": "Ali", "age": 20}
# ret = d.popitem()
# print(d)
# print(ret)


                # Question NO 07
# Ek dictionary ko empty karne ke liye kaunsa method use hota hai?
# d = {"name": "Ali", "age": 20}
# d.clear()
# print(d)


                # Question NO 08
# Dictionary d = {"x": 10} me new key "y" add karne ka method kaunsa hai?
# d = {"x": 10}
# d.update("y" , 20)
# print(d)


                # Question NO 09
# Ek dictionary ko dusri dictionary ke saath merge karne ka method kaunsa hai?
# d = {"name": "Ali", "age": 20}
# e = {"x": 10}
# d.update(e)
# print(d)


                # Question NO 10
# Dictionary ki shallow copy banane ke liye kaunsa method use hota hai?
# d = {"name": "Ali", "age": 20}
# d.copy()
# print(d)


                # Question NO 11
# Agar dictionary me key exist nahi karti to uske liye default value set karne ka method kaunsa hai?
# d = {"x": 10}
# d.setdefault("y" , 20)
# print(d)


                # Question NO 12
# Ek dictionary me kitne key-value pairs hain kaise check karoge?
# d = {"name": "Ali", "age": 20}
# d.items()
# print(d)


                # Question NO 13
# Dictionary me kisi key ke existence ko check karne ke liye kaunsa operator use hota hai?
d = {"name": "Ali", "age": 20}
e = d["age"]
print(e)


                # Question NO 14
# Dictionary d = {"a": 1, "b": 2} me "b" key ka value update kaise karoge?
# d = {"a": 1, "b": 2}
# d["b"] = 4
# print(d)
