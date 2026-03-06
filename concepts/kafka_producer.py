"""
Kafka Producer Utility
"""

import asyncio
import json

from pydantic import BaseModel
from aiokafka import AIOKafkaProducer



KAFKA_BOOTSTRAP_SERVERS = "localhost:9094"
TOPIC_NAME = "farmer.events"


class Event(BaseModel):
    event_type: str
    payload: str


  
# Kafka Event Producer
class KafkaEventProducer:
  

    def __init__(self, bootstrap_servers: str = KAFKA_BOOTSTRAP_SERVERS):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None

    # Start Kafka producer
    async def start(self):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8"),
            key_serializer=lambda k: k.encode("utf-8") if k else None,
        )
        await self.producer.start()
     
    # Stop Kafka producer
    async def stop(self):
        if self.producer:
            await self.producer.stop()
            
    # Send event to Kafka topic
    async def send_event(self, event_type: str, payload: str, topic: str = TOPIC_NAME, key: str = None):
        event = Event(event_type=event_type, payload=payload)
        event_dict = event.model_dump()
        result = await self.producer.send_and_wait(
            topic=topic,
            value=event_dict,
            key=key,
        )
        return {"topic": topic, "partition": result.partition, "offset": result.offset}

#   Send sample events
async def run_producer_demo():
  
    prod = KafkaEventProducer()
    await prod.start()

    print("   PRODUCING DISEASE_DETECT EVENT")

    event_type = "disease_detect"
    payload = "Tomato Late Blight"

    result = await prod.send_event(event_type, payload,key="Sensor-123")
    print(result)
    
    await asyncio.sleep(0.5)

    await prod.stop()


if __name__ == "__main__":
    asyncio.run(run_producer_demo())
