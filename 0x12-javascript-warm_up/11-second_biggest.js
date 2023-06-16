#!/usr/bin/node
function secondBiggest(n){
	if (n[1]){
		return 0
	}else if (n.length === 3){
		return 0
	}else{
		return Math.max(...n)
	}	
}

console.log(secondBiggest(process.argv))
