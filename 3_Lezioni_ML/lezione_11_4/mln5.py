import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Carica il dataset
df = pd.read_csv("iris.csv")

print(df.columns)

# Sostituisci 'species' con il nome corretto della colonna se diverso
X = df.drop("target", axis=1)
y = df["target"]

# Dividi in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modello
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Previsioni
y_pred = clf.predict(X_test)

# Valutazione
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Esempio di previsione su nuovo dato
nuovo = [[5.1, 3.5, 1.4, 0.2]]  # lunghezza/larghezza sepalo, lunghezza/larghezza petalo
print("Specie prevista:", clf.predict(nuovo))