import sys

def inverse(a, b):
  """Print a^-1 (mod b)"""
  if a == 1:
    return 1
  if a == 0:
    print("Inverse doesn't exist!\n")
    return 0
  return (b*(a-inverse(b%a, a))+1)/a

if __name__ == "__main__":
  a, b = int(input("write down a for a^-1(mod b)\n")), int(input("write down b for a^-1(mod b)\n"))
  print(f"The result is {inverse(a, b)}")
