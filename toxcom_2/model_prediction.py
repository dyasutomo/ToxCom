import re
import pickle
import joblib

# load STOPWORDS 
sw = open('english_STOPWORDS', 'r')
STOPWORDS = set([w.strip("\n") for w in sw.readlines()])

def prepare_text(text):
    text = text.lower()
    # remove \n
    text = re.sub("\\n", " ", text)
    # remove 've, 're
    text = re.sub("[a-z]*\'[r,v]e", "", text) 
    # remove 's, 't, 'r, 'v
    text = re.sub("[a-z]*\'[s,t,r,v]", "", text) 
    # Replace everything not a letter with a space
    text = re.sub("[^a-zA-Z]", " ", text)
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])
    return text

def predict(input_comment):

    model = joblib.load(open("./logres_3.joblib", "rb"))
    vectorizer = pickle.load(open("./vectorizer_tfidf.pkl", "rb"))
    com = prepare_text(input_comment)
    x = vectorizer.transform([com])
    pred = model.predict(x.toarray())[0]

    target_columns = ['toxic','severe_toxic','obscene','threat','insult','identity_hate']
    targets_dict = {i:target_columns[i] for i in range(6)}

    output_labels = []
    if sum(pred)==0:
        output_labels.append("Non-Toxic")
    else:
        for i, v in enumerate(pred):
            if v ==1:
                output_labels.append(targets_dict[i])

    return ", ".join(output_labels)


