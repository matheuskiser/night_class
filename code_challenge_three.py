#####################################################################################################
# Write a function to decode the following.

str = "Yms bgb gr! Cmlepyrsjyrgmlq! Dgb wms sqc qrpgle.kyicrpylq? Id wms bgbl'r wms qfmsjb npmzyzjw em afcai gr msr. Ir kyicq rfgq ksaf cyqgcp."

# A hint for the 3.
# a = c
# z = b
# m = o

test = list(str)
alphabet = list('abcdefghijklmnopqrstuvwxyz')
correct_string = ''

for key in test:
    for key in alphabet:
        correct_string += alphabet[(alphabet.index(key)+2)]

print correct_string
