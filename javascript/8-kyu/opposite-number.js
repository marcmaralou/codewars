// Very simple, given an integer or a floating-point number, find its opposite.

// Examples:

// 1: -1
// 14: -14
// -34: 34

function opposite(number) {
  if (Math.sign(number) == 1) {
    return -Math.abs(number);
  }
  else {
    return Math.abs(number);
  }
}
