# Multilayer Perceptron em Python

Este repositório contém uma implementação de um Multilayer Perceptron em Python. O código é capaz de treinar e testar o MLP para várias portas lógicas, como AND, OR e XOR, usando retropropagação.

## Instruções de Uso

Para usar este Multilayer Perceptron, siga os passos abaixo:

1. Clone o repositório em seu ambiente local:
```git clone https://github.com/VitorCarvalho67/Multilayer-perceptron.git```

2. Navegue até o diretório do projeto:
```cd seu-repositorio```

3. Execute o script Python:
```python main.py```

4. Siga as instruções fornecidas no console para selecionar a porta lógica e treinar o modelo.

5. Após o treinamento, você pode testar o modelo com entradas personalizadas.

## função de ativação:

$f'(x) = \frac{e^{-x}}{(1 + e^{-x})^2}$.

1. **Camada Oculta (Hidden Layer)**:

   A entrada da camada oculta é calculada como:

$\text{entrada\_oculta} = X \cdot w_1$.


   Aqui, \(X\) é a matriz de entradas com dimensões \((n_{\text{amostras}}, N)\).

   Em seguida, aplicamos a função de ativação sigmóide elemento por elemento:

   $$
\text{saida\_oculta} = \sigma(\text{entrada\_oculta})
$$


3. **Camada de Saída (Output Layer)**:

   A entrada da camada de saída é calculada como:

  $$
\text{entrada\_saida} = \text{saida\_oculta} \cdot w_2
$$


   Aqui, \(\text{saida\_oculta}\) é a matriz de saída da camada oculta com dimensões \((n_{\text{amostras}}, M)\).

   Mais uma vez, aplicamos a função de ativação sigmóide elemento por elemento:

   $$
\text{saida\_saida} = \sigma(\text{entrada\_saida})
$$

