def find_mean(arr: list):
  arr.sort()
  size = len(arr)
  size_is_pair = size % 2 == 0
  middle = int(size / 2)

  if size_is_pair:
    return (arr[middle - 1] + arr[middle]) / 2
  else:
    return arr[middle]


def main():
  arr = [1, 2, 3, 4, 5]
  print(find_mean(arr))

  arr = [1, 2, 3, 4, 5, 6]
  print(find_mean(arr))


main()
