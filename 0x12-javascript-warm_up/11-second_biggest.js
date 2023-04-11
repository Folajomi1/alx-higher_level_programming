#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
}
