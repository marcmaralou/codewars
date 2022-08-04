// Return the number (count) of vowels in the given string.

// We will consider a, e, i, o, u as vowels for this Kata (but not y).

// The input string will only consist of lower case letters and/or spaces.

function getCount(str) {
  let vowelCount = 0;
  let splitString = str.split('');
  for (i = 0; i < splitString.length; i++) {
    if (splitString[i] == "a" || splitString[i] == "e" || splitString[i] == "i" || splitString[i] == "o" || splitString[i] == "u") {
      vowelCount++;
    }
  }
  return vowelCount;
}
