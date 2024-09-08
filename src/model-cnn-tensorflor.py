import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# Carregar e pré-processar o conjunto de dados MNIST
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Redimensionar as imagens para (28, 28, 1) e normalizar os valores dos pixels
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255

# Criar o modelo CNN
model = models.Sequential()

# Primeira camada convolucional + pooling
"""
Camadas Convolucionais: O modelo começa com uma camada convolucional de 32 filtros, 
com um kernel de 3x3 e função de ativação ReLU, que é aplicada para detectar padrões nas imagens.
"""
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Segunda camada convolucional + pooling
"""
Camadas de Pooling: Após cada camada convolucional, uma camada de pooling 2x2 é usada para reduzir 
a dimensionalidade, resumindo as features mais importantes, o que ajuda a diminuir o número de 
parâmetros e a controlar o overfitting.
"""
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Terceira camada convolucional + pooling
"""
Mais Camadas Convolucionais: Adicionamos mais camadas convolucionais para aumentar a 
capacidade do modelo de capturar características complexas.
"""
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Flatten para transformar os dados 2D em 1D
"""
Flatten: Transforma a saída das camadas convolucionais (que é 2D) em um vetor 1D para ser processado 
pelas camadas densas.
"""
model.add(layers.Flatten())

# Camada densa com 64 neurônios
"""
Camada Densa: A camada densa com 64 neurônios aplica uma função ReLU para introduzir não linearidade 
e aprender combinações complexas de features.
 Isso permite que a CNN capture e combine características sofisticadas das imagens, 
 como formas e texturas que são críticas para a tarefa de classificação ou reconhecimento visual.
"""
model.add(layers.Dense(64, activation='relu'))

# Camada de saída com 10 neurônios (um para cada dígito)
"""
Camada de Saída: A última camada tem 10 neurônios, um para cada dígito (0 a 9), 
com ativação softmax para obter as probabilidades de cada classe
"""
model.add(layers.Dense(10, activation='softmax'))

# Resumo da arquitetura do modelo
model.summary()

# Compilar o modelo
"""
Compilação: O modelo é compilado com o otimizador adam, que ajusta os pesos do modelo com base na função 
de perda sparse_categorical_crossentropy (adequada para classificação multiclass), 
e a métrica de desempenho escolhida é a acurácia.
"""
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
"""
Treinamento: O modelo é treinado por 5 épocas, onde ele ajusta seus pesos para minimizar a
perda no conjunto de treinamento e validação.
"""
history = model.fit(train_images, train_labels, epochs=5,
                    validation_data=(test_images, test_labels))

# Avaliar o modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Accuracy on test data: {test_acc:.4f}")

# Plotar a acurácia e a perda ao longo das épocas
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de Treinamento')
plt.plot(history.history['val_accuracy'], label='Acurácia de Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de Treinamento')
plt.plot(history.history['val_loss'], label='Perda de Validação')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend()

plt.show()
