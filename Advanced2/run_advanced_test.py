def main():
    print("Advanced Test execution starts")
    for x in range(10):
      print("ADVANCED TEST FAIL - " + str(x))
      return Failure("There was an OS Error.")

main()