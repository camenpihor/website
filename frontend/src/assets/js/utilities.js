function groupBy(xs, key) {
  // https://stackoverflow.com/a/38575908
  let grouped = xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});

  let ordered = {};
  Object.keys(grouped).sort().forEach(function (key) {
    ordered[key] = grouped[key];
  });
  return ordered;
}

function compare(key) {
  return function innerSort(a, b) {
    const valueA = (typeof a[key] === 'string')
      ? a[key].toUpperCase() : a[key];
    const valueB = (typeof b[key] === 'string')
      ? b[key].toUpperCase() : b[key];

    let comparison = 0;
    if (valueA > valueB) {
      comparison = 1;
    } else if (valueA < valueB) {
      comparison = -1;
    }
    return comparison
  };
}

export { compare, groupBy }
