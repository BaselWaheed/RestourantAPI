import pickle
df = (input('d5l ay 7aga\n'))
model=pickle.load(open(r'C:\Users\7lawa\Desktop\testmachine\model.pkl', 'rb'))
cv=pickle.load(open(r'C:\Users\7lawa\Desktop\testmachine\cv.pkl', 'rb'))
X = cv.transform([df])
y_pred = model.predict(X)
print(y_pred)