import json
import time
import os
from kafka import KafkaConsumer
from api_client import get_feedback_from_openai
from mongodb import MongoDBConnection


# Initialize MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
mongo_conn = MongoDBConnection(MONGO_URI, "local")
db = mongo_conn.get_database()


# Retry de conexão com Kafka
def wait_for_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                'feedback',
                bootstrap_servers=[KAFKA_BROKER],
                auto_offset_reset='earliest',
                enable_auto_commit=False,
                group_id='feedback_process',
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
            print("Kafka conectado.")
            return consumer
        except Exception as e:
            print(f"Aguardando Kafka... {e}")
            time.sleep(3)


def main():
    # Configurando o consumer para o tópico 'feedback' com auto commit desabilitado
    consumer = wait_for_kafka()

    print("Kafka Consumer iniciado e escutando o tópico 'feedback'...")

    # Loop infinito para processamento contínuo das mensagens
    for message in consumer:
        try:
            # A mensagem já foi convertida para dict pelo deserializer
            msg_dict = message.value
            print(f"Mensagem recebida: {msg_dict}")

            response = get_feedback_from_openai(msg_dict['comment'], msg_dict['rating'])

            response_dict = {
                "comment": msg_dict["comment"],
                "rating": msg_dict["rating"]
            }

            response_dict.update(response)
            
            # Save response to MongoDB
            feedback_collection = db["feedback"]
            feedback_collection.insert_one(response_dict)

            # Commit manual após processar a mensagem
            consumer.commit()
        except Exception as e:
            print(f"Erro ao processar a mensagem: {e}")

        time.sleep(0.1)  # Pequena pausa para evitar loop intenso


if __name__ == '__main__':
    main()