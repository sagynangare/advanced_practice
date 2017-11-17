"""Write a code to find string after $5 from string
"i have $2 in my pockets and $5 in wallet and i need $3 more"""

str1 = "i have $2 in my pockets and $5 in wallet and i need $3 more"
print(str1.split("$5", 1)[1])
