#!/usr/bin/node
exports.esrever = function (list) {
  const tmpList = [];
  for (const i of list) {
    tmpList.unshift(i);
  }
  return tmpList;
};
