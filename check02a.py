def prompt_user():
  positiveNum = int(input("Enter a positive number: "))
  while positiveNum < 0:
    print("Invalid entry. The number must be positive.")
    positiveNum = int(input("Enter a positive number: "))
  return positiveNum
  
def compute_sum(x, y, z):
  return (x + y + z)
  
def main():
  aNum = prompt_user()
  bNum = prompt_user()
  cNum = prompt_user()
  soma = compute_sum(aNum, bNum, cNum)
  print("\nThe sum is: {}.".format(soma))

if __name__ == "__main__":
  main()