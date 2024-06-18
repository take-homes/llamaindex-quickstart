# LlamaIndex

## Data
This example uses the text of Paul Graham's essay, ["What I Worked On"](http://paulgraham.com/worked.html). 

## Set your OpenAI API key
LlamaIndex uses OpenAI's `gpt-3.5-turbo` by default. Make sure your API key is available to your code by setting it in `starter.py`.

## Load the documents and create the index
This builds an index over the documents in the data folder (which in this case just consists of the essay text, but could contain many documents).

## Storing your data
By default, the data you just loaded is stored in memory as a series of vector embeddings. You can save time (and requests to OpenAI) by saving the embeddings to disk. That can be done with this line:
```
index.storage_context.persist()
```
By default, this will save the data to the directory storage, but you can change that by passing a persist_dir parameter.

## Viewing Queries and Events Using Logging
Use logging to see what's happening under the hood.

You can set the level to `DEBUG` for verbose output, or use `level=logging.INFO` for less.
