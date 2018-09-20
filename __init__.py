from re import match

var1 = '/606'
var = match(r'/\d{3}', var1).group(0)
print(var)
