/* eslint-disable linebreak-style */
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    const data = 'data';
    setTimeout(() => {
      if (data) {
        resolve(data);
      } else {
        reject(new Error('Data not found'));
      }
    }, 1000);
  });
}

if (require.main === module) {
  const response = getResponseFromAPI();
  console.log(response instanceof Promise);
}
