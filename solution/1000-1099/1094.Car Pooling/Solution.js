/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function (trips, capacity) {
    const d = new Array(1001).fill(0);
    for (const [x, f, t] of trips) {
        d[f] += x;
        d[t] -= x;
    }
    let s = 0;
    for (const x of d) {
        s += x;
        if (s > capacity) {
            return false;
        }
    }
    return true;
};
