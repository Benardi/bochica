import sys, pickle, random
from ast import literal_eval
from functools import reduce

import pandas as pd


def retrieve_by_doc(index, query, k):
    try:
        import Queue as Q  # ver. < 3.0
    except ImportError:
        import queue as Q

    result = []
    q = Q.PriorityQueue()
    L = index.loc[lambda df: df.word.isin(query)]

    all_docs = set(index["doc_id:freq"].\
                   apply(lambda pairs: list(doc_id for doc_id, freq in pairs)).sum())
    
    base_documents = L["doc_id:freq"].sum()
    
    for doc in all_docs:
        score = base_documents
        
        if score == 0:
            pass
        
        elif score == []:
            score = 0
        else:
            score = [fq for d_id, fq in score if d_id == doc]
            if score != []:
                score = reduce(lambda a,b : a+b,score)
            else:
                score = 0
                
        q.put(((-1) * score,doc))
    
    i = 0
    while not q.empty() and i < k:
        pair = q.get()
        pair = ((-1) *pair[0],pair[1])
        result.append(pair)
        i += 1
        
    return result


if len(sys.argv) < 3:
    print("The script demands two arguments")
else:
    df = pd.read_csv("../output/inverted_index.csv")
    df["doc_id:freq"] = df["doc_id:freq"].apply(lambda x: list(literal_eval(x)))
    k = int(sys.argv[1])
    nw = int(sys.argv[2])
    
    all_words = pickle.load( open( "all_words.p", "rb" ) )
    query = random.sample(all_words, nw)
    retrieve_by_doc(df, query, k) 
