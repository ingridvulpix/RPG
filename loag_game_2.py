import pickle

story = {
    1: {
      'Text': [
            "Cap 2"
        ],
      'Options': []
}
}

with open('chapter2.bin', 'wb') as chapter:
  pickle.dump(story, chapter)
