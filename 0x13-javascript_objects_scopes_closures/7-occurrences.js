#!/usr/bin/node
exports.nbOccurences = function (list, searchElement)
return list.reduce ((accumulator, currentValue) => currentValue === searchElement ? accumulator + 1 : accumulator, 0);
