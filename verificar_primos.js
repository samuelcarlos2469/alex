let n = prompt("Digite o número a ser verificado");
let bool = false;
for (verificador = 2; verificador < n; verificador++) {
  //2 é o único par, pra saber se é primo tem q ir verificando se tem mais de um divisor ou não
  if (n % verificador === 0) {
    bool = true;
  }
}
if (bool !== true) {
  console.log("Esse número é primo");
} else {
  console.log("Esse numero não é primo");
}
