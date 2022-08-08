// Simple, given a string of words, return the length of the shortest word(s).

// String will never be empty and you do not need to account for different data types.

function findShort(s) {
  let l = 69
  let array = s.split(" ")
  for (i = 0; i < array.length; i++) {
    if (array[i].length < l) {
      l = array[i].length
    } 
  }
  return l
