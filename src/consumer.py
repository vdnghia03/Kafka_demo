from quixstreams import Application


app = Application(
    broker_address="localhost:9092"
    , consumer_group="text-splitter"
    , auto_offset_reset="earliest"
)

jokes_topic = app.topic(name="jokes", value_serializer="json")

sdf = app.dataframe( topic=jokes_topic)

sdf = sdf.update(lambda message: print(f"Input: {message}"))

def main():
    app.run()
