from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'X:\ecnu\stanford-corenlp-4.0.0')
# 这里改成你stanford-corenlp所在的目录
sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
print('Tokenize:', nlp.word_tokenize(sentence))
print('Part of Speech:', nlp.pos_tag(sentence))
print('Named Entities:', nlp.ner(sentence))
print('Constituency Parsing:', nlp.parse(sentence))
print('Dependency Parsing:', nlp.dependency_parse(sentence))
nlp.close()  # Do not forget to close! The backend server will consume a lot memery.
