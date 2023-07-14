import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.naive_bayes import GaussianNB
from category_encoders import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

for k in range(1,7):

        # data = pd.read_csv(f'attribute_vector{k}.csv')
        # X = data[['Property_1', 'Property_2', 'Property_3', 'Property_4', 'Property_5']]
        
        data = pd.read_csv(f'features_G{k}.csv')
        y = data['category'] 
        X = data.drop("category", axis=1)
        y = data['category'].str.replace('category', '')
        

        # Encode categorical data 
        encoder = OrdinalEncoder()
        X = encoder.fit_transform(X)

        # Split to train and test 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=100)

        Classifiers=[
            DecisionTreeClassifier(),
            RandomForestClassifier(),
            KNeighborsClassifier(n_neighbors=7),
            BaggingClassifier(),
            AdaBoostClassifier(),
            GaussianNB(),
            SVC(),
            LogisticRegression(max_iter=5000),
            SGDClassifier(),
            VotingClassifier(estimators=[('lr', LogisticRegression()), ('rf', RandomForestClassifier()), ('gnb', GaussianNB())])
        ]

        results=[]
        for i in range(len(Classifiers)):
            classifier = Classifiers[i]
            classifier.fit(X_train, y_train)
            y_pred = classifier.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            results.append(accuracy)
        df = pd.DataFrame({"Algorithm": ["Decision Tree", "Random Forest", "K-Nearest Neighbor", "Bagging", "Boosting",
                                        "Naive Bayes", "SVM", "Logistic Regression", "SGD", "Voting"], "Accuracy": results})
        df = df.sort_values(by="Accuracy", ascending=False)
        print("graph ",str(k))
        print(df)
