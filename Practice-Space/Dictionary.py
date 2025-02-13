#Dictionary or Hashmap

# Frequently used for counting occurences of elements

# template to add elements and their count from input array to the dict

hash_map[element] = 1 + count.get(element, 0) # type: ignore
 #count.get(element, 0) looks up the value of element in the dictionary count. If the element is found, it returns its current frequency; if it's not found, it defaults to 0 (the second argument to get()).