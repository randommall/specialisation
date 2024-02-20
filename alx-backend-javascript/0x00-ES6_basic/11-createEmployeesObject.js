export default function createEmployeesObject(departmentName, employees) {
  const departmentObject = {
    [departmentName]: employees,
  };

  return departmentObject;
}
