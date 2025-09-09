# DP 2nd calculator
inp1 = input("Input one number to be calculated: ")
inp2 = input("Input a second number: ")

add = float(inp1) + float(inp2)
sub = float(inp1) - float(inp2)
mult = float(inp1) * float(inp2)
div = float(inp1) / float(inp2)
intdiv = float(inp1) // float(inp2)
mod = float(inp1) % float(inp2)
exp = float(inp1) ** float(inp2)

print(f"Addition result: {round(add, 2)}")
print(f"Subtraction result: {round(sub, 2)}")
print(f"Multiplication result: {round(mult, 2)}")
print(f"Division result: {round(div, 2)}")
print(f"Integer Division result: {round(intdiv, 2)}")
print(f"Modulus result: {round(mod, 2)}")
print(f"Exponent result: {round(exp, 2)}")
