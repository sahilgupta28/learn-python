# customer = {
#     "name" : "sahil",
#     "age" : 25,
#     "is_verified" : True
# }
#
# print(customer.get('name'))

numbers = {
    '0' : 'Zero',
    '1' : 'One',
}
input = input('Enter a number ')
output = ""
for i in input:
    output += numbers.get(i, "")

print(output)