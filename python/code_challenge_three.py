#####################################################################################################
# Write a function to decode the following.
# A hint for the 3.
# a = c
# z = b
# m = o

# Used tip to use string.maketrans() from instructor

from string import maketrans   # Required to call maketrans function.

str = "Yms bgb gr! Cmlepyrsjyrgmlq! Dgb wms sqc qrpgle.kyicrpylq? Id wms bgbl'r wms qfmsjb npmzyzjw em afcai gr msr. Ir kyicq rfgq ksaf cyqgcp."

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print str.translate(trantab);