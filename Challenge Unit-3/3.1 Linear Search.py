def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


# Example usage:
products = ["maths", "computer science", "english", "social", "computer science", "tamil"]
print(products)
target = str(input("Enter the target from the list: "))
result = linearSearchProduct(products, target)
print(result)