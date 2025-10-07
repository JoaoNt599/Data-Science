import os 
import json
from confluent_kafka import Producer, KafkaException
from confluent_kafka.admin import AdminClient, NewTopic


DEFAULT_BROKEN = os.getenv("KAFKA_BROKER", "localhost:9092")
TOPIC = "feedback"


class KafkaFeedbackProducer:

    def __init__(self, broker=DEFAULT_BROKEN, topic=TOPIC):
        self.broker = broker
        self.topic = topic
        self.producer_config = {
            "bootstrap.servers": self.broker,
        }
        self.admin_config = {
            "bootstrap.servers": self.broker,
        }
        self.producer = Producer(self.producer_config)
        self.admin_client = AdminClient(self.admin_config)
        self.ensure_topic_exists()

    
    def delivery_report(self, err, msg):
        """Callback para reportar o resultado do envio"""
        if err is not None:
            print(f"Falha ao entregar mensagem: {err}")
        else:
            print(f"Mensagem entregue: {msg.topic()} [{msg.partition()}]")
    

    def ensure_topic_exists(self):
        """Verifica se o tópico existe e o cria caso não exista"""
        new_topic = NewTopic(self.topic, num_partitions=1, replication_factor=1)
        fs = self.admin_client.create_topics([new_topic])
        # topics = self.admin_client.create_topics([new_topic])
        for topic, f in fs.items():
            try:
                f.result() # aguarda a criação
                print(f"Tópico '{topic}' criado com sucesso.")
            except Exception as e:
                print(f"Tópico '{topic}' pode já existir ou houve erro: {e}")
    

    def produce_feedback(self, feedback_data: dict):
        """Produz a mensagem convertida em JSON para o tópico feedback"""
        try:
            message = json.dumps(feedback_data)
            self.producer.produce(self.topic, value=message, callback=self.delivery_report)
            # Poll para processar o callback
            self.producer.poll(0)
            self.producer.flush() # Garante o envio
        except KafkaException as e:
            print(f"Erro ao produzir mensagem: {e}")
    