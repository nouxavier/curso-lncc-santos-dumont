import os
from datetime import datetime
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import pandas as pd

# Configurar estratégia para distribuição de treino em múltiplas GPUs
strategy = tf.distribute.MirroredStrategy()

print(f"Number of devices: {strategy.num_replicas_in_sync}")

# Definir o escopo da estratégia para a construção e compilação do modelo
with strategy.scope():
    # Carregar e pré-processar o conjunto de dados MNIST
    (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
    train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
    test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255

    # Criar o modelo CNN
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    model.summary()

    # Compilar o modelo
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

# Treinar o modelo com suporte a paralelismo
history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels),
                    batch_size=64 * strategy.num_replicas_in_sync)  # Ajuste do batch size para múltiplas GPUs

# Avaliar o modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Accuracy on test data: {test_acc:.4f}")

# Criar uma pasta com a data e hora atuais
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
save_dir = f"results_{current_time}"
os.makedirs(save_dir, exist_ok=True)

# Salvar o histórico de treinamento em um arquivo CSV usando Pandas
history_df = pd.DataFrame(history.history)
history_csv_path = os.path.join(save_dir, 'training_history.csv')
history_df.to_csv(history_csv_path, index=False)

# Salvar a avaliação do modelo em um arquivo de texto
evaluation_path = os.path.join(save_dir, 'model_evaluation.txt')
with open(evaluation_path, 'w') as f:
    f.write(f"Test Loss: {test_loss:.4f}\n")
    f.write(f"Test Accuracy: {test_acc:.4f}\n")

# Plotar a acurácia e a perda ao longo das épocas
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# Salvar o gráfico na pasta criada
plt.savefig(os.path.join(save_dir, 'accuracy_loss_plot.png'))
