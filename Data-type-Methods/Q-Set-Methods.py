#                     Python Set Practice Questions
# 1. Ek set s = {1, 2, 3} me value 4 add karne ke liye kaunsa method use karoge?
# s = {1, 2, 3}
# s.add(4)
# print(s)


# 2. Ek set me multiple values [4, 5, 6] ek saath add karne ka method kya hai?
# s = {1, 2, 3}
# s.update([4, 5, 6])
# print(s)


# 3. Set me se element 3 delete karna hai — kaunsa method error throw karega agar element na mile?
# s = {1, 2, 3}
# s.remove(3)
# print(s)


# 4. Set me se element safely delete karna hai — jisme element na mile to error na mile — kaunsa method use hoga?
# s = {1, 2, 3, 6, 9}
# s.discard(9)
# print(s)


# 5. Ek set se random element remove + return karne ke liye kaunsa method use hota hai?
# s = {1, 2, 3, 6, 9}
# x = s.pop()
# print(x)
# print(s)


# 6. Ek set ko completely empty karne ka method kaunsa hai?
# s = {1, 2, 3, 6, 9}
# s.clear()
# print(s)


# 7. Set ki copy banane ke liye kaunsa method use hota hai?s = {1, 2, 3, 6, 9}
# s = {1, 2, 3, 6, 9}
# s.copy()
# print(s)


# 8. Do sets A = {1, 2} aur B = {2, 3} ka union kaise nikaaloge?
# A = {1, 2}
# B = {2, 3}
# print(A.union(B))


# 9. Do sets ka common elements kaise nikaaloge?
# A = {1, 2}
# B = {2, 3}
# print(A.intersection(B))


# 10. Set A = {1, 2, 3} aur B = {3, 4} me A ke wo elements kaise nikaaloge jo B me nahi hain?
# A = {1, 2, 3}
# B = {3, 4}
# print(A.difference(B))


# 11. Do sets ka symmetric difference kaun sa method dega?
# A = {1, 2, 3}
# B = {3, 4}
# print(A.symmetric_difference(B))


# 12. Check karna ho ke 5 set me exist karta hai ya nahi — kaunsa operator use hota hai?
# A = {1, 2, 3}
# print(A.discard(5))


# 13. Ek set ko reverse karna possible hai ya nahi? Agar nahi to kyun?
# A = {1, 2, 3}
# print(A.it(5))


# 14. Set me duplicate values add karne ki koshish karo to kya hota hai?
# A = {1, 2, 3}
# A.add(3)
# print(A)


# 15. Ek string ko set me convert karne se kya output milega?
# A = "Hello"
# print(type(A))
# print(type(set(A)))


# 16. Ek list ko set me convert karke duplicates remove karne ka method kya hai?
# 17. Kaise check karoge ke set A, set B ka subset hai ya nahi?
# A = {1, 2, 3}
# B = {3, 4}
# print(A.issubset(B))


# 18. Kaise check karoge ke set A, set B ka superset hai ya nahi?
# A = {1, 2, 3}
# B = {3, 4}
# c = A.issuperset(B)
# print(c)


# 19. Kaise check karoge ke do sets me koi common element nahi hai?
# A = {1, 2, 3}
# B = {3, 4}
# print(A.symmetric_difference(B))


# 20. Set ko list me convert karne ka built-in function kaunsa hai?
# A = {1, 2, 3}
# print(type(A))
# print(type(list(A)))