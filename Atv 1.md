
1) Observe o trecho de código abaixo:

```
int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça {
	K = K + 1;
	SOMA = SOMA + K;
}

imprimir(SOMA);
```

Ao final do processamento, qual será o valor da variável SOMA?
``91``

Resposta:
|-----|--|----|
|passo|K |SOMA|
|0 	  |1 |1   |
|1 	  |2 |3   |
|2 	  |3 |6   |
|3 	  |4 |10  |
|4 	  |5 |15  |
|5 	  |6 |21  |
|6 	  |7 |28  |
|7 	  |8 |36  |
|8 	  |9 |45  |
|9 	  |10|55  |
|10   |11|66  |
|11   |12|78  |
|12   |13|91  |