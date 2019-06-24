var tab = document.getElementById("task1-leaderboard");
var tr = document.createElement("tr");
var td1 = document.createElement("td");
var td2 = document.createElement("td");
var td3 = document.createElement("td");
tr.appendChild(td1);
tr.appendChild(td2);
tr.appendChild(td3);
tab.appendChild(tr)
td1.innerHTML = "1";
td2.innerHTML = "dmn (single model) (SJTU)";
td3.innerHTML = "0.888";

var tr = document.createElement("tr");
var td1 = document.createElement("td");
var td2 = document.createElement("td");
var td3 = document.createElement("td");
tr.appendChild(td1);
tr.appendChild(td2);
tr.appendChild(td3);
tab.appendChild(tr)
td1.innerHTML = "2";
td2.innerHTML = "Multi-Finetune BERT (single model) (Beijing Language and Culture University) https://github.com/liuchunhuahua/Commonsense-Reading-Comprehension/blob/master/README.md";
td3.innerHTML = "0.866";

var tr = document.createElement("tr");
var td1 = document.createElement("td");
var td2 = document.createElement("td");
var td3 = document.createElement("td");
tr.appendChild(td1);
tr.appendChild(td2);
tr.appendChild(td3);
tab.appendChild(tr)
td1.innerHTML = "3";
td2.innerHTML = "ATTENTIVE READER BASELINE (single model)";
td3.innerHTML = "0.692";
