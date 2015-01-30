#####################################################################################################
# Write a function to decode the following.

str = "Yms bgb gr! Cmlepyrsjyrgmlq! Dgb wms sqc qrpgle.kyicrpylq? Id wms bgbl'r wms qfmsjb npmzyzjw em afcai gr msr. Ir kyicq rfgq ksaf cyqgcp."

# A hint for the 3.
# a = c
# z = b
# m = o

shift   = 2
letters = list(str)
cipher  = ''

ceasar = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in letters:
    if letter in ceasar:
        oldindex = ceasar.index(letter)
        newindex = (oldindex + shift) % len(ceasar)
        newletter = ceasar[newindex]
    else:
        newletter = letter

    print(letter)