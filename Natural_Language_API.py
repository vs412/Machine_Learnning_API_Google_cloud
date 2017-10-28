from google.cloud import language

def language_analysis(text):
    client = language.Client()
    document = client.document_from_text(text)
    sent_analysis = document.analyze_sentiment()
    dir(sent_analysis)
    sentiment = sent_analysis.sentiment

    ent_analysis = document.analyze_entities()
    dir(ent_analysis)
    entities = ent_analysis.entities

    return sentiment, entities


example_text = '''Python is a widely used high-level programming language for general-$

Python features a dynamic type system and automatic memory management and supports mul$

Python interpreters are available for many operating systems, allowing Python code to $

sentiment, entities = language_analysis(example_text)
print(sentiment.score, sentiment.magnitude)
for e in entities:
    print(e.name, e.entity_type, e.metadata, e.salience)
