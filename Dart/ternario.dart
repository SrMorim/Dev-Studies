void main() {
  double nota = 5;
  String boletim = nota >= 7 ? 'Aprovado' : "Reprovado!";
  print(boletim);

  while(nota < 10){
    print(nota);
    nota++;
  }
  
/*  int n = 10;
  bool r = n==10;
  if (r == false) {
    print('deu red');
  } else {
    print('deu green');
  }*/
}