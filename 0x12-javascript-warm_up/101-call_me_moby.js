#!/usr/bin/node
exports.executeXtimes = function (x, theFunction) {
for (let i = 0; i < x; i++)
theFunction();
}
