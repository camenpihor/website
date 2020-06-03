function groupBy(xs, key) {
  // https://stackoverflow.com/a/38575908
  return xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x);
    return rv;
  }, {});
}

export { groupBy }
