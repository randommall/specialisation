export default function getBudgetForCurrentYear(income, gdp, capita) {
  const year = new Date().getFullYear();

  const budget = {
    [`income-${year}`]: income,
    [`gdp-${year}`]: gdp,
    [`capita-${year}`]: capita,
  };

  return budget;
}
