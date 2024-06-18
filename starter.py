from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os

os.environ["OPENAI_API_KEY"] = "XXXXX"

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
