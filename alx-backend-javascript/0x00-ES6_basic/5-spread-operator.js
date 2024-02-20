export default function concatArrays(array1, array2, string) {
  const newArray = [...array1, ...array2, ...string];
  return newArray;
}
