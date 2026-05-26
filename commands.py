import pickle
model = pickle.load(open('artifacts/model.pkl', 'rb'))
print(model)