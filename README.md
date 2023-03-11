# DesafioTargetSistemas

Repositório com as soluções do desafio

Atualmente temos novas tecnologias em desenvolvimento que podem afetar o funcionamento do mundo como conhecemos, porém essas revoluções tecnológicas sempre aconteceram, sendo muito importante entender que cada avanço que a sociedade recebe, são criadas uma ou mais oportunidades novas, assim criando um ciclo.

A inteligência artificial tem o poder de acelerar processos manuais, automatizar tarefas complexas com precisão e reduzir os custos operacionais, de um ponto de vista macro, conseguimos perceber que as grandes áreas impactadas pela IA sendo vistas mais rapidamente pela sociedade serão as áreas de saúde onde os processos de diagnósticos estão se tornando mais rápidos pela utilização de inteligência baseada em seus históricos para exames, doenças e prescrição de medicamentos, a educação que a algum tempo já vem recebendo, evoluindo e se adequando as novas necessidades do aprendizado, a segurança que tem muito potencial para prevenção e resolução de crimes com vigilância e reconhecimento com ferramentas para segurança digital e privacidade eletrônica,  os empregos que sofreram mudanças significativas, principalmente os cargos que não necessitam de conhecimento profundo ou especialidades para a execução de suas tarefas, e por fim, a economia que é afetada diretamente pelas áreas citadas acima, pois cada uma destas frentes que movem o mundo, tem características únicas que as tecnologias tendem a aprimorar, seja com otimização ou digitalização de processos que hoje são realizados por humanos.

Com o contexto descrito acima, vemos que a IA já está presente em nosso cotidiano e tende a ficar cada vez mais comum a interação com ela no dia-a-dia, trazendo mais possibilidades de benefícios do que prejuízos para as pessoas e para a sociedade, uma revolução tecnológica está se instalando e carregando consigo novas oportunidades e desafios, com toda a responsabilidade que vem com estas escolhas, com certeza teremos mais tecnologia, com uma melhor disseminação do conhecimento, com uma saúde menos burocrática e mais eficiente, com segurança em todos os aspectos da vida e com prosperidade em toda a sociedade para a construção de um futuro com mais respeito e justiça.

<!--
## V2
A Inteligência Artificial (IA) está transformando rapidamente a forma como as empresas operam e as pessoas vivem suas vidas. No futuro próximo, acredita-se que a IA terá um impacto social significativo em áreas como a economia, o emprego, a saúde, a educação, a segurança e a privacidade.

Aqui estão algumas possíveis análises do impacto social que a IA trará para as pessoas e empresas no futuro próximo:

Economia: A IA tem o potencial de impulsionar o crescimento econômico, aumentando a eficiência e a produtividade em muitas áreas. A automação de tarefas rotineiras pode liberar trabalhadores para se concentrarem em atividades mais complexas e criativas. No entanto, a automação também pode levar à perda de empregos, especialmente em setores como a manufatura e o atendimento ao cliente.

Emprego: A IA tem o potencial de criar novos empregos em áreas como a ciência de dados, engenharia de IA e desenvolvimento de software. No entanto, a automação também pode substituir muitos empregos, especialmente aqueles que são rotineiros ou de baixa habilidade. Será importante desenvolver políticas para ajudar as pessoas a se adaptarem a essas mudanças no mercado de trabalho.

Saúde: A IA pode melhorar a precisão do diagnóstico e tratamento de doenças, permitindo uma intervenção mais rápida e eficaz. A IA também pode ajudar os médicos a identificar riscos e padrões em grandes conjuntos de dados. No entanto, a IA também pode levantar preocupações sobre privacidade e segurança dos dados de saúde.

Educação: A IA pode ser usada para personalizar a aprendizagem, fornecendo a cada aluno um caminho de aprendizagem adaptado às suas necessidades e habilidades. No entanto, a IA também pode levantar preocupações sobre a privacidade dos dados dos alunos e a responsabilidade pela tomada de decisões.

Segurança: A IA pode ser usada para identificar ameaças e prevenir crimes, melhorando a segurança pública. No entanto, a IA também pode levantar preocupações sobre a vigilância em massa e o uso indevido de informações pessoais.

Privacidade: A IA pode coletar e analisar grandes quantidades de dados pessoais, levantando preocupações sobre a privacidade e a proteção dos dados. Será importante desenvolver políticas para proteger os dados pessoais e garantir a transparência e a responsabilidade na coleta e uso de dados pela IA.

Em resumo, a IA tem o potencial de trazer muitos benefícios para as pessoas e empresas, mas também pode levantar preocupações e desafios sociais significativos. Será importante abordar essas questões de forma proativa e responsável para maximizar os benefícios da IA e minimizar seus impactos negativos.
-->



## ------------------- 1

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
|passo|K |SOMA|
|-----|--|----|
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

## ------------------- 2

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
**Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;**
```python
	def fibonacci(num):
	    a, b = 0, 1
	    while b < num:
	        a, b = b, a + b
	    if b != num:
	        return False
	    else:
	        return True
	def ehFibonacci(num):
		if num < 0:
			print('Entrada Incorreta, somente [\'num\' >= 0]')
		if fibonacci(num):
		    print(f'{num} pertence à sequência de Fibonacci.')
		else:
		    print(f'{num} não pertence à sequência de Fibonacci.')
	num = 280571172992510140037611932413038677189525 # 200
	ehFibonacci(num)
```
- Lista dos 2000 primeiros números da sequência de Fibonacci neste link
- https://oeis.org/A000045/b000045.txt


## ------------------- 3

3) Descubra a lógica e complete o próximo elemento:

Impares

a) 1, 3, 5, 7, **9**

2^x

b) 2, 4, 8, 16, 32, 64, **128**

x^2

c) 0, 1, 4, 9, 16, 25, 36, **49**

(pares)^2

d) 4, 16, 36, 64, **100**

Fibonacci

e) 1, 1, 2, 3, 5, 8, **13**

*Difícil* números que começam com D

f) 2, 10, 12, 16, 17, 18, 19, **200**


## ------------------- 4

4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?
a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.
b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)
c) Explique como chegou no resultado.

Uma breve observação/explicação por entender que quando os carros se cruzarem, obviamente estão na mesma distância da cidade, pois estão no mesmo local, mas para provar vamos aos cálculos.

Carro - Ribeirão Preto -> Franca @ 110 km/h
Velocidade média do carro 110 Km/h

Caminhão - Franca -> Ribeirão Preto 80 km/h + 2 * (5 min)
Velocidade média do caminhão é a distância dividido pela velocidade 100 km / 80km/h que é 1.25h + os 10 minutos de diferença das paradas nos pedágios (10min / 60min = 0.1667h) para ver o tempo total e daí pegar o instante que as duas se cruzam para ter o resultado.
1.25 + 0.17 = 1.4167h 
Velocidade média do caminhão 100 km / 1.4167h = 70.58 km/h

Agora temos que encontrar o ponto de encontro, igualando as equações do carro (x1/v1) e caminhão (x2-100km/-70,58km/h)
sendo ponto: x/v1 = x - 100 km / -70,58km/h

transformando a equação:
multiplicação cruzada ponto: -70,58km/hx = v1 * x - v1 * 100km 
Agora vamos manipular para evidenciar o *x* ponto: x = v1 * 100km / v1 + 70,58km/h 
Agora é só substituir ponto: x = 110km/h * 100km / 110km/h * 70,58km/h

Então o carro e o caminhão estarão na mesma distância de Ribeirão Preto quando se cruzarem e essa distância será de **60,91km**



## ------------------- 5

5) Escreva um programa que inverta os caracteres de um string.
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

```python
	# string = input("Digite uma string para ser invertida: ")
	string = 'invertendo'

	invertida = []

	# básico tamanho da string - 1,
	# posição - 1 (última),
	# com passo -1 (percorrendo de trás pra frente)
	for i in range(len(string) - 1, -1, -1):
	    invertida.append(string[i])

	# converte p/ string
	invertida = ''.join(invertida)

	print("A string invertida:", invertida)
```
