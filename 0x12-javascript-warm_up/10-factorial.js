#!/usr/bin/node
function factorial (n) {
  return !n ? 1 : factorial(n - 1) * n;
}

console.log(factorial(+process.argv[2]));
