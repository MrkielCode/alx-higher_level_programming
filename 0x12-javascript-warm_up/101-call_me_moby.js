#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
	const exeTimes = (i) => {
		if (i > 0)
		{
			theFunction();
			exeTimes(i - 1);
		}
	};
	exeTimes(x);
}
