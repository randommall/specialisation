export default function iterateThroughObject(reportWithIterator) {
  const employees = [...reportWithIterator]; // Convert the generator to an array
  return employees.join(' | ');
}
