import optuna
from sklearn.model_selection import cross_val_score
from lightgbm import LGBMClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import f1_score, make_scorer

f1 = make_scorer(f1_score, average='macro')

def find_best_class_weight(X, y, model_name='svc', n_trials=1):
    def objective(trial):
        class_weight = trial.suggest_categorical(
            'class_weight',
            [{0: w, 1: 100} for w in range(10, 110, 10)]
        )

        if model_name == 'lightgbm':
            clf = LGBMClassifier(class_weight=class_weight)
        elif model_name == 'random_forest':
            clf = RandomForestClassifier(class_weight=class_weight)
        elif model_name == 'svc':
            clf = SVC(class_weight=class_weight)
        else:
            raise ValueError(f"Unsupported model: {model_name}")

        score = cross_val_score(clf, X, y, cv=5, scoring=f1).mean()
        return score

    def objective2(trial):
        class_weight = trial.suggest_categorical(
            'class_weight',
            [{0: 100, 1: w} for w in range(10, 110, 10)]
        )

        if model_name == 'lightgbm':
            clf = LGBMClassifier(class_weight=class_weight)
        elif model_name == 'random_forest':
            clf = RandomForestClassifier(class_weight=class_weight)
        elif model_name == 'svc':
            clf = SVC(class_weight=class_weight)
        else:
            raise ValueError(f"Unsupported model: {model_name}")

        score = cross_val_score(clf, X, y, cv=5, scoring=f1).mean()
        return score

    # Optimize the first objective function
    study = optuna.create_study(direction='maximize')
    study.optimize(objective, n_trials=n_trials)
    best_trial = study.best_trial

    # Optimize the second objective function
    study2 = optuna.create_study(direction='maximize')
    study2.optimize(objective2, n_trials=n_trials)
    best_trial2 = study2.best_trial

    # Compare and return the best class weight
    if best_trial.value > best_trial2.value:
        return best_trial.params['class_weight']
    else:
        return best_trial2.params['class_weight']