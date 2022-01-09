from lime import lime_tabular
import lime
import pickle
import shap


pipe = Pipeline(
    [
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("oversample", SMOTE()),
        ("logistic", LR(max_iter=500)),
    ]
)

param_grid = {
    "imputer__strategy": ["mean", "median"],
    "logistic__C": np.arange(20, 50, 1),
    "logistic__penalty": ["none", "l1", "l2"],
}
search = GridSearchCV(pipe, param_grid, verbose=1, n_jobs=4, scoring="recall")
search.fit(X_train, y_train)

search.best_params_

search.best_score_

y_pred = (search.predict_proba(X_test)[:, 1] < 0.05) + 0
recall_score(y_test, y_pred)

imp = SimpleImputer(strategy="mean")
ss = StandardScaler()
sm = SMOTE()
lg = LR(C=28, penalty="none", max_iter=500)
X_train2 = imp.fit_transform(X_train)
X_train2 = ss.fit_transform(X_train2)
X_train2, y_train2 = sm.fit_resample(X_train2, y_train)
lg.fit(X_train2, y_train2)
X_test2 = imp.transform(X_test)
X_test2 = ss.transform(X_test2)

y_pred = (lg.predict_proba(X_test2)[:, 1] > 0.5) + 0
recall_score(y_test, y_pred)

pipe2 = Pipeline(
    [
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("oversample", SMOTE()),
        ("rfc", RandomForestClassifier()),
    ]
)
param_grid = {
    "imputer__strategy": ["mean", "median", "most_frequent"],
    "rfc__max_depth": np.arange(1, 4, 1),
    "rfc__n_estimators": np.arange(20, 160, 20),
}
search = GridSearchCV(pipe2, param_grid, verbose=1, n_jobs=4, scoring="recall")
search.fit(X_train, y_train)
search.best_estimator_


search.best_params_

search.best_score_

imp = SimpleImputer(strategy="mean")
ss = StandardScaler()
sm = SMOTE()
lg = RandomForestClassifier(n_estimators=100, max_depth=1)
X_train2 = imp.fit_transform(X_train)
X_train2 = ss.fit_transform(X_train2)
X_train2, y_train2 = sm.fit_resample(X_train2, y_train)
lg.fit(X_train2, y_train2)
X_test2 = imp.transform(X_test)
X_test2 = ss.transform(X_test2)

y_pred = (lg.predict_proba(X_test2)[:, 1] > 0.5) + 0
recall_score(y_test, y_pred)


pipe3 = Pipeline(
    [
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("oversample", SMOTE()),
        ("lg", lgb.LGBMClassifier()),
    ]
)
param_grid = {
    "imputer__strategy": ["mean", "median"],
    "lg__num_leaves": np.arange(20, 50, 10),
    "lg__max_depth": np.arange(2, 10, 2),
    "lg__learning_rate": [0.001, 0.05, 0.01, 0.1, 0.5, 1],
}
search = GridSearchCV(pipe3, param_grid, verbose=2, n_jobs=4, scoring="recall")
search.fit(X_train, y_train)
search.best_estimator_

search.best_score_

search.best_params_

imp = SimpleImputer(strategy="median")
ss = StandardScaler()
sm = SMOTE()
lg = lgb.LGBMClassifier(num_leaves=30, max_depth=2, learning_rate=0.001)
X_train2 = imp.fit_transform(X_train)
X_train2 = ss.fit_transform(X_train2)
X_train2, y_train2 = sm.fit_resample(X_train2, y_train)
lg.fit(X_train2, y_train2)
X_test2 = imp.transform(X_test)
X_test2 = ss.transform(X_test2)

y_pred = (lg.predict_proba(X_test2)[:, 1] > 0.5) + 0
precision_score(y_test, y_pred)

lg.predict_proba(X_test2)


with open("model.pkl", "wb") as f:
    pickle.dump((lg, imp, ss), f)

temp = X_train.dropna()
with open("X_train.pkl", "wb") as f:
    pickle.dump(temp, f)

temp = X_train.dropna()
temp = y_train[temp.index]
with open("y_train.pkl", "wb") as f:
    pickle.dump(temp, f)

temp = X_test.dropna()

visualizer = discrimination_threshold(lg, X_train2, y_train2)

si = SimpleImputer()
X_train2 = si.fit_transform(X_train)
ss = StandardScaler()
X_train2 = ss.fit_transform(X_train2)
X_train2 = pd.DataFrame(X_train2, columns=X_train.columns)

X_test = si.transform(X_test)
X_test = ss.transform(X_test)

model = LR(max_iter=500)
model.fit(X_train, y_train)

X_test = pd.DataFrame(X_test, columns=X_train.columns)

lg.predict_proba(X_test2)


explainer = lime_tabular.LimeTabularExplainer(
    training_data=np.array(X_train2),
    feature_names=X_train.columns,
    class_names=["0", "1"],
    mode="classification",
)

exp = explainer.explain_instance(
    data_row=pd.DataFrame(X_test2, columns=X_train.columns).iloc[550],
    predict_fn=lg.predict_proba,
)

exp.show_in_notebook(show_table=True)

exp.as_pyplot_figure()
plt.savefig("./images/local.png")

explainer = shap.TreeExplainer(lg)
shap_values = explainer.shap_values(X_test2)
shap.summary_plot(shap_values, X_test2)
