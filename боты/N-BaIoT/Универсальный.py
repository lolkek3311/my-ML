import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

# Инструменты анализа
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
import lightgbm as lgb
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.decomposition import PCA

# =========================================================
# БЛОК 1: УНИВЕРСАЛЬНЫЙ ЗАГРУЗЧИК
# =========================================================
def load_network_dataset(path, sample_size=10000):
    """
    Автоматически собирает данные, определяя метку по имени файла.
    """
    files = glob.glob(os.path.join(path, "*.csv"))
    data_list = []
    
    for f in files:
        if any(x in f for x in ['summary', 'info', 'features']): continue
        
        temp_df = pd.read_csv(f)
        # Сэмплирование для скорости
        temp_df = temp_df.sample(n=min(len(temp_df), sample_size), random_state=42)
        
        # Универсальная разметка: 0 если в имени есть 'benign' или 'normal', иначе 1
        name = f.lower()
        temp_df['is_attack'] = 0 if ('benign' in name or 'normal' in name) else 1
        data_list.append(temp_df)
        
    return pd.concat(data_list, ignore_index=True)

# =========================================================
# БЛОК 2: УМНАЯ ПРЕДОБРАБОТКА
# =========================================================
def preprocess_data(df):
    """
    Чистит данные от мусора, корреляции и приводит к одному масштабу.
    """
    X = df.drop('is_attack', axis=1)
    y = df['is_attack']
    
    # 1. Удаление константных признаков (где везде одно значение)
    X = X.loc[:, X.nunique() > 1]
    
    # 2. Удаление сильно коррелирующих признаков (>0.98)
    corr = X.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [col for col in upper.columns if any(upper[col] > 0.98)]
    X = X.drop(to_drop, axis=1)
    
    # 3. Масштабирование
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X, X_scaled, y, to_drop

# =========================================================
# БЛОК 3: ПОИСК АНОМАЛИЙ (БЕЗ УЧИТЕЛЯ)
# =========================================================
def detect_anomalies(X_scaled, n_clusters=2):
    """
    Находит аномальные группы в трафике без подсказок.
    """
    # Метод К-средних
    km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = km.fit_predict(X_scaled)
    
    # Метод Isolation Forest (специально для ИБ)
    # Находит "изолированные" точки, которые не похожи на остальные
    iso = IsolationForest(contamination=0.1, random_state=42)
    anomalies = iso.fit_predict(X_scaled) # -1 аномалия, 1 норма
    
    return clusters, anomalies

# =========================================================
# БЛОК 4: КЛАССИФИКАЦИЯ (С УЧИТЕЛЕМ)
# =========================================================
def train_super_model(X_train, y_train, X_test, y_test):
    """
    Обучает мощный бустинг для точного распознавания.
    """
    model = lgb.LGBMClassifier(class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    print("\n[ОТЧЕТ КЛАССИФИКАЦИИ]")
    print(classification_report(y_test, preds))
    return model

# =========================================================
# БЛОК 5: ВИЗУАЛИЗАЦИЯ И ИНТЕРПРЕТАЦИЯ
# =========================================================
def visualize_results(X_scaled, clusters, model, feature_names):
    # 1. Сжатие в 2D для карты трафика
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='tab10', alpha=0.5)
    plt.title("Кластеры сетевого поведения (PCA)")
    
    plt.subplot(1, 2, 2)
    lgb.plot_importance(model, max_num_features=10, importance_type='gain', ax=plt.gca())
    plt.title("Топ признаков-детекторов")
    
    plt.tight_layout()
    plt.show()

# =========================================================
# ГЛАВНЫЙ ЗАПУСК (MAIN)
# =========================================================

# 1. Загрузка
path = '/home/lolkek3310/python/Подготовка Гомель/боты/N-BaIoT'
df = load_network_dataset(path)

# 2. Подготовка
X_orig, X_scaled, y, dropped = preprocess_data(df)

# 3. Поиск аномалий (без учителя)
clusters, anomalies = detect_anomalies(X_scaled)

# 4. Точное обучение (с учителем)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, stratify=y)
clf_model = train_super_model(X_train, y_train, X_test, y_test)

# 5. Итоги
visualize_results(X_scaled, clusters, clf_model, X_orig.columns)