#!/usr/bin/node
exports.esrever = function (list) {
  const tmpList = [];
  let i = 0;
  do {
    tmpList.unshift(list[i]);
	i++;
  } while (i < list.length);
  return tmpList;
};
