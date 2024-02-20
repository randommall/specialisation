export default function* createIteratorObject(report) {
  const { allEmployees } = report; // Use object destructuring

  for (const department in allEmployees) {
    if (Object.prototype.hasOwnProperty.call(allEmployees, department)) {
      const employeesInDepartment = allEmployees[department];
      for (const employee of employeesInDepartment) {
        yield employee;
      }
    }
  }
}
