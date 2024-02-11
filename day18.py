def count_substring(string, sub_string):
  # Initialize the count variable
  count = 0

# Loop through the indices of the string
  for i in range(len(string)):
    # Check if the substring starts at the current index
    if string[i:].startswith(sub_string):
        # Increment the count
      count += 1
  return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
