#pip install monkeylearn

from monkeylearn import MonkeyLearn
 
ml = MonkeyLearn('<<Your API key here>>')
data = ['The restaurant was great!', 'The curtains were disgusting']
model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)

print(result.body)