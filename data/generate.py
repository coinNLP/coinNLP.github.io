import json, sys

# this file generates leaderboard javascript files from the json output of codalab

def generateJavaScriptForElement1(el, idx):
	js = 'var tr = document.createElement("tr");\nvar td1 = document.createElement("td");\nvar td2 = document.createElement("td");\nvar td3 = document.createElement("td");\ntr.appendChild(td1);\ntr.appendChild(td2);\ntr.appendChild(td3);\ntab.appendChild(tr)'
	js += '\ntd1.innerHTML = "' + str(idx) + '";'
	js += '\ntd2.innerHTML = "' + el[1] + '";'
	js += '\ntd3.innerHTML = "' + str(round(el[0], 3)) + '";\n'
	return js

def generateJavaScriptForElement2(el, idx):
	js = 'var tr = document.createElement("tr");\nvar td1 = document.createElement("td");\nvar td2 = document.createElement("td");\nvar td3 = document.createElement("td");\nvar td4 = document.createElement("td");\ntr.appendChild(td1);\ntr.appendChild(td2);\ntr.appendChild(td3);\ntr.appendChild(td4);\ntab.appendChild(tr)'
	js += '\ntd1.innerHTML = "' + str(idx) + '";'
	js += '\ntd2.innerHTML = "' + el[2] + '";'
	js += '\ntd3.innerHTML = "' + str(round(el[0], 2)) + '";\n'
	js += '\ntd4.innerHTML = "' + str(round(el[1], 2)) + '";\n'
	return js

def task1():
	fi = 'leaderboards/task1.json'
	fo = 'leaderboards/leaderboard1.js'
	with open(fi, "r") as json_file:  
		data = json.load(json_file)
		elements = [(float(el["scores"]["score"]), el["submission"]["description"]) for el in data["leaderboard"]]
		sorted(elements, key=lambda x: x[0], reverse=True)
		javascript = 'var tab = document.getElementById("task1-leaderboard");\n' + "\n".join([generateJavaScriptForElement1(el, idx + 1) for idx, el in enumerate(elements)])	
		with open(fo, "w") as fo:
			fo.write(javascript)

def task2():
	fi = 'leaderboards/task2.json'
	fo = 'leaderboards/leaderboard2.js'
	with open(fi, "r") as json_file:  
		data = json.load(json_file)
		elements = [(float(el["scores"]["exact_match"]), float(el["scores"]["f1"]), el["submission"]["description"]) for el in data["leaderboard"]]
		sorted(elements, key=lambda x: x[0] + x[1], reverse=True)
		javascript = 'var tab = document.getElementById("task2-leaderboard");\n' + "\n".join([generateJavaScriptForElement2(el, idx + 1) for idx, el in enumerate(elements)])	
		with open(fo, "w") as fo:
			fo.write(javascript)

def main():
	if len(sys.argv) != 2:
		print("Wrong number of arguments. Specifiy '1' or '2' to generate data for one of the shared tasks")
		sys.exit(-1)
	
	if sys.argv[1] == "1":
		task1()
	elif sys.argv[1] == "2":
		task2()
	
	

if __name__ == "__main__":
	main()
