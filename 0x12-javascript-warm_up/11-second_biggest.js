#!/usr/bin/node
function findSecondLargest (arr) {
  if (arr.length === 0) {
    console.log(0);
    return;
  }
  if (arr.length === 1) {
    console.log(0);
    return;
  }
  const array = arr.map((item) => Number(item));
  for (let i = 0; i < array.length - 1; i++) {
    for (let j = 0; j < array.length - 1; j++) {
      if (array[j] > array[j + 1]) {
        const k = array[j];
        array[j] = array[j + 1];
        array[j + 1] = k;
      }
    }
  }
  console.log(array[array.length - 2]);
}
findSecondLargest(process.argv.slice(2));
