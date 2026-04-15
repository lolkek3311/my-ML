# Pandas - Полный Гайд по Обработке Данных

## Содержание
1. [Основы Pandas](#1-основы-pandas)
2. [Загрузка и сохранение данных](#2-загрузка-и-сохранение-данных)
3. [Исследование данных](#3-исследование-данных)
4. [Выборка и фильтрация](#4-выборка-и-фильтрация)
5. [Обработка пропущенных значений](#5-обработка-пропущенных-значений)
6. [Обработка дубликатов](#6-обработка-дубликатов)
7. [Преобразование данных](#7-преобразование-данных)
8. [Группировка и агрегация](#8-группировка-и-агрегация)
9. [Объединение данных](#9-объединение-данных)
10. [Работа с временными рядами](#10-работа-с-временными-рядами)
11. [Работа со строками](#11-работа-со-строками)
12. [Статистический анализ](#12-статистический-анализ)
13. [Визуализация](#13-визуализация)
14. [Оптимизация производительности](#14-оптимизация-производительности)
15. [Практические примеры](#15-практические-примеры)

---

## 1. Основы Pandas

### Создание DataFrame
```python
import pandas as pd
import numpy as np

# Из словаря
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['Moscow', 'Minsk', 'Moscow', 'Gomel'],
    'salary': [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)

# Из списка списков
data = [[1, 'Alice', 25], [2, 'Bob', 30], [3, 'Charlie', 35]]
df = pd.DataFrame(data, columns=['id', 'name', 'age'])

# Из numpy array
arr = np.random.randn(5, 3)
df = pd.DataFrame(arr, columns=['A', 'B', 'C'])

# Из Series
s1 = pd.Series([1, 2, 3], name='A')
s2 = pd.Series([4, 5, 6], name='B')
df = pd.concat([s1, s2], axis=1)

# С датой
df = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'value': np.random.randn(10)
})
```

### Базовые свойства
```python
df.shape              # Размер (строки, столбцы)
df.columns            # Имена столбцов
df.index              # Индекс
df.dtypes             # Типы данных
df.info()             # Общая информация
df.describe()         # Статистика
df.head()             # Первые 5 строк
df.tail()             # Последние 5 строк
df.sample(10)         # Случайные 10 строк
```

---

## 2. Загрузка и сохранение данных

### CSV
```python
# Чтение
df = pd.read_csv('file.csv')
df = pd.read_csv('file.csv', sep=';')           # Разделитель
df = pd.read_csv('file.csv', header=None)       # Без заголовков
df = pd.read_csv('file.csv', names=['A', 'B'])  # Свои имена
df = pd.read_csv('file.csv', index_col='id')    # Индекс по колонке
df = pd.read_csv('file.csv', usecols=['A', 'B']) # Только определенные колонки
df = pd.read_csv('file.csv', nrows=100)         # Только 100 строк
df = pd.read_csv('file.csv', na_values=['?', 'NA', '-'])  # NA значения
df = pd.read_csv('file.csv', encoding='utf-8')  # Кодировка
df = pd.read_csv('file.csv', parse_dates=['date'])  # Парсинг дат
df = pd.read_csv('file.csv', dtype={'id': str})  # Типы данных

# Запись
df.to_csv('output.csv', index=False)            # Без индекса
df.to_csv('output.csv', sep=';')                # Разделитель
df.to_csv('output.csv', encoding='utf-8')       # Кодировка
df.to_csv('output.csv', columns=['A', 'B'])     # Только определенные колонки
```

### Excel
```python
# Чтение
df = pd.read_excel('file.xlsx')
df = pd.read_excel('file.xlsx', sheet_name='Sheet2')
df = pd.read_excel('file.xlsx', sheet_name=None)  # Все листы (dict)
df = pd.read_excel('file.xlsx', header=1)         # Заголовок со 2-й строки

# Запись
df.to_excel('output.xlsx', index=False)
df.to_excel('output.xlsx', sheet_name='Data')

# С ExcelWriter
with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)
```

### JSON
```python
# Чтение
df = pd.read_json('file.json')
df = pd.read_json('file.json', orient='records')
df = pd.read_json('file.json', orient='columns')
df = pd.read_json('file.json', orient='index')

# Из строки
json_str = '[{"A": 1, "B": 2}, {"A": 3, "B": 4}]'
df = pd.read_json(json_str)

# Запись
df.to_json('output.json', orient='records')
df.to_json('output.json', orient='columns')
df.to_json('output.json', orient='index')
```

### SQL
```python
import sqlite3

# Подключение к БД
conn = sqlite3.connect('database.db')

# Чтение
df = pd.read_sql('SELECT * FROM table', conn)
df = pd.read_sql_query('SELECT * FROM table WHERE col > 5', conn)
df = pd.read_sql_table('table_name', conn)

# Запись
df.to_sql('table_name', conn, if_exists='replace', index=False)
df.to_sql('table_name', conn, if_exists='append', index=False)

# Закрытие
conn.close()
```

### Другие форматы
```python
# Parquet
df = pd.read_parquet('file.parquet')
df.to_parquet('output.parquet', index=False)

# Feather
df = pd.read_feather('file.feather')
df.to_feather('output.feather')

# Pickle
df = pd.read_pickle('file.pkl')
df.to_pickle('output.pkl')

# HTML
tables = pd.read_html('https://example.com/table')  # Все таблицы со страницы
df = tables[0]
df.to_html('output.html')
```

---

## 3. Исследование данных

### Общая информация
```python
df.info()                           # Типы, пропуски, размер
df.describe()                       # Статистика числовых колонок
df.describe(include='all')          # Статистика всех колонок
df.describe(include=['object'])     # Только категориальные
df.dtypes                           # Типы данных
df.shape                            # Размер
df.size                             # Количество элементов
df.memory_usage(deep=True)          # Использование памяти
```

### Статистика
```python
df.mean()                           # Среднее
df.median()                         # Медиана
df.mode()                           # Мода
df.std()                            # Стандартное отклонение
df.var()                            # Дисперсия
df.min()                            # Минимум
df.max()                            # Максимум
df.sum()                            # Сумма
df.count()                          # Количество не-null
df.quantile(0.25)                   # 25-й перцентиль
df.quantile([0.25, 0.5, 0.75])      # Несколько перцентилей

# Для конкретной колонки
df['column'].mean()
df['column'].median()
df['column'].value_counts()         # Частота значений
df['column'].value_counts(normalize=True)  # В процентах
df['column'].unique()               # Уникальные значения
df['column'].nunique()              # Количество уникальных
```

### Корреляция
```python
df.corr()                           # Корреляция Пирсона
df.corr(method='spearman')          # Корреляция Спирмена
df.corr(method='kendall')           # Корреляция Кендалла

# Корреляция с target
df.corr()['target'].sort_values(ascending=False)

# Ковариация
df.cov()
```

---

## 4. Выборка и фильтрация

### Выбор колонок
```python
# Одна колонка (Series)
df['column']
df.column

# Несколько колонок (DataFrame)
df[['col1', 'col2']]

# Переименование колонок
df.rename(columns={'old_name': 'new_name'}, inplace=True)
df.columns = ['A', 'B', 'C']
```

### Выбор строк
```python
# По индексу
df.loc[0]                # По метке индекса
df.iloc[0]               # По позиции
df.loc[0:5]              # Диапазон
df.iloc[0:5]             # Диапазон по позиции

# По условию
df.loc[[0, 2, 5]]        # Конкретные индексы
df.iloc[[0, 2, 5]]       # Конкретные позиции
```

### Фильтрация по условию
```python
# Простое условие
df[df['age'] > 25]
df[df['city'] == 'Moscow']
df[df['salary'] >= 50000]

# Несколько условий
df[(df['age'] > 25) & (df['city'] == 'Moscow')]    # AND
df[(df['age'] > 25) | (df['city'] == 'Minsk')]     # OR
df[~(df['city'] == 'Moscow')]                       # NOT

#isin()
df[df['city'].isin(['Moscow', 'Minsk'])]
df[~df['city'].isin(['Moscow'])]

# Строковые методы
df[df['name'].str.startswith('A')]
df[df['name'].str.contains('li')]
df[df['name'].str.endswith('e')]

# isin() с dict
criteria = {'city': ['Moscow', 'Minsk'], 'age': [25, 30]}
df[df.set_index(['city', 'age']).index.isin(list(criteria.items()))]
```

### query() метод
```python
df.query('age > 25')
df.query('age > 25 and city == "Moscow"')
df.query('salary >= 50000 or age < 30')
df.query('city in ["Moscow", "Minsk"]')
df.query('age > @threshold')  # С переменной
```

### Сортировка
```python
# По одной колонке
df.sort_values('age')
df.sort_values('age', ascending=False)

# По нескольким колонкам
df.sort_values(['city', 'age'])
df.sort_values(['city', 'age'], ascending=[True, False])

# По индексу
df.sort_index()

# Top N
df.nlargest(5, 'salary')      # Top 5 по зарплате
df.nsmallest(5, 'age')        # Top 5 по возрасту
```

---

## 5. Обработка пропущенных значений

### Обнаружение
```python
df.isnull().sum()                   # Пропуски по колонкам
df.isnull().sum().sum()             # Всего пропусков
df.isnull().mean() * 100            # Процент пропусков
df.isnull().any(axis=1).sum()       # Строк с пропусками
```

### Удаление
```python
# Удаление строк
df.dropna()                         # Все строки с NaN
df.dropna(subset=['age', 'salary'])  # Строки где NaN в этих колонках
df.dropna(how='all')                # Только полностью пустые строки
df.dropna(thresh=3)                 # Минимум 3 не-NaN значений

# Удаление колонок
df.dropna(axis=1)                   # Все колонки с NaN
df.dropna(axis=1, how='all')        # Только полностью пустые колонки
```

### Заполнение
```python
# Константой
df.fillna(0)
df['column'].fillna(0, inplace=True)

# Статистикой
df['age'].fillna(df['age'].mean(), inplace=True)
df['age'].fillna(df['age'].median(), inplace=True)
df['age'].fillna(df['age'].mode()[0], inplace=True)

# Forward/Backward fill
df.fillna(method='ffill')           # Заполнение предыдущим значением
df.fillna(method='bfill')           # Заполнение следующим значением
df.fillna(method='ffill', limit=2)  # Максимум 2 заполнения

# Интерполяция
df.interpolate()                    # Линейная интерполяция
df.interpolate(method='polynomial', order=2)
df.interpolate(method='time')       # Для временных рядов

# Групповое заполнение
df['age'] = df.groupby('city')['age'].transform(lambda x: x.fillna(x.median()))
```

### KNN Imputation
```python
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=5)
df[['col1', 'col2', 'col3']] = imputer.fit_transform(df[['col1', 'col2', 'col3']])
```

---

## 6. Обработка дубликатов

### Обнаружение
```python
df.duplicated().sum()               # Количество дубликатов
df.duplicated(subset=['name', 'age'])  # Дубликаты по колонкам
```

### Удаление
```python
df.drop_duplicates()                # Удаление дубликатов
df.drop_duplicates(subset=['name']) # По конкретным колонкам
df.drop_duplicates(keep='first')    # Оставить первый
df.drop_duplicates(keep='last')     # Оставить последний
df.drop_duplicates(keep=False)      # Удалить все дубликаты
```

---

## 7. Преобразование данных

### Создание новых колонок
```python
# Простое присваивание
df['age_squared'] = df['age'] ** 2
df['log_salary'] = np.log(df['salary'])
df['is_young'] = df['age'] < 30
df['name_length'] = df['name'].str.len()

# apply()
df['age_group'] = df['age'].apply(lambda x: 'Young' if x < 30 else 'Old')

# С функцией
def categorize_age(age):
    if age < 25:
        return 'Very Young'
    elif age < 35:
        return 'Young'
    else:
        return 'Old'

df['age_group'] = df['age'].apply(categorize_age)

# apply() с несколькими колонками
df['full_info'] = df.apply(lambda row: f"{row['name']} from {row['city']}", axis=1)
```

### map() и replace()
```python
# map()
df['city_code'] = df['city'].map({'Moscow': 1, 'Minsk': 2, 'Gomel': 3})

# replace()
df['city'].replace({'Moscow': 'MSK', 'Minsk': 'MNK'}, inplace=True)
df.replace(-999, np.nan, inplace=True)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
```

### cut() и qcut()
```python
# Бининг
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], 
                         labels=['Child', 'Young', 'Middle', 'Senior'])

# Квантильный бининг
df['salary_group'] = pd.qcut(df['salary'], q=4, 
                             labels=['Low', 'Medium', 'High', 'Very High'])
```

### astype()
```python
# Преобразование типов
df['age'] = df['age'].astype(int)
df['id'] = df['id'].astype(str)
df['date'] = pd.to_datetime(df['date'])
df['category'] = df['category'].astype('category')

# Категориальные типы
df['city'] = df['city'].astype('category')
df['city'].cat.categories
df['city'].cat.codes
```

### apply() с функциями
```python
# К числовым колонкам
df['salary'].apply(np.sqrt)
df[['age', 'salary']].apply(lambda x: x / x.max())

# К строковым колонкам
df['name'].str.lower()
df['name'].str.upper()
df['name'].str.title()
df['city'].str.strip()

# С несколькими выводами
def extract_info(text):
    return pd.Series({'length': len(text), 'words': len(text.split())})

df[['length', 'words']] = df['name'].apply(extract_info)
```

---

## 8. Группировка и агрегация

### groupby()
```python
# Базовая группировка
df.groupby('city').mean()
df.groupby('city')['salary'].mean()

# Несколько группировок
df.groupby(['city', 'gender']).mean()
df.groupby(['city', 'gender'])['salary'].agg(['mean', 'count'])

# Несколько агрегаций
df.groupby('city').agg({
    'salary': ['mean', 'max', 'min', 'count'],
    'age': ['mean', 'std']
})

# С именованными агрегациями
df.groupby('city').agg(
    avg_salary=('salary', 'mean'),
    max_age=('age', 'max'),
    count=('salary', 'count')
).reset_index()
```

### Агрегирующие функции
```python
# Доступные функции
df.groupby('city').agg(['mean', 'median', 'std', 'min', 'max', 'sum', 'count'])

# Кастомные функции
df.groupby('city')['salary'].agg(lambda x: x.max() - x.min())

# Несколько функций
df.groupby('city')['salary'].agg(['mean', 'std', 'count'])
```

### transform()
```python
# Нормализация по группе
df['salary_normalized'] = df.groupby('city')['salary'].transform(
    lambda x: (x - x.mean()) / x.std()
)

# Заполнение пропусков по группе
df['age'] = df.groupby('city')['age'].transform(lambda x: x.fillna(x.median()))

# Ранжирование
df['salary_rank'] = df.groupby('city')['salary'].rank(method='dense', ascending=False)
```

### pivot_table()
```python
# Pivot table
pivot = df.pivot_table(
    values='salary',
    index='city',
    columns='gender',
    aggfunc='mean',
    fill_value=0,
    margins=True,
    margins_name='Total'
)

# С несколькими значениями
pivot = df.pivot_table(
    values=['salary', 'age'],
    index='city',
    columns='gender',
    aggfunc='mean'
)

# С разными агрегациями
pivot = df.pivot_table(
    values=['salary', 'age'],
    index='city',
    aggfunc={'salary': 'mean', 'age': 'median'}
)
```

### crosstab()
```python
# Перекрестная таблица
pd.crosstab(df['city'], df['gender'])
pd.crosstab(df['city'], df['gender'], margins=True)
pd.crosstab(df['city'], df['gender'], normalize='index')  # В процентах
pd.crosstab(df['city'], df['gender'], values=df['salary'], aggfunc='mean')
```

---

## 9. Объединение данных

### concat()
```python
# По вертикали
df_combined = pd.concat([df1, df2], ignore_index=True)
df_combined = pd.concat([df1, df2], axis=0)

# По горизонтали
df_combined = pd.concat([df1, df2], axis=1)

# С ключами
df_combined = pd.concat([df1, df2], keys=['df1', 'df2'])

# С разными индексами
df_combined = pd.concat([df1, df2], join='inner')  # Только общие колонки
```

### merge()
```python
# Inner join
df_merged = df1.merge(df2, on='id')

# Left join
df_merged = df1.merge(df2, on='id', how='left')

# Right join
df_merged = df1.merge(df2, on='id', how='right')

# Outer join
df_merged = df1.merge(df2, on='id', how='outer')

# По разным колонкам
df_merged = df1.merge(df2, left_on='id1', right_on='id2')

# По нескольким колонкам
df_merged = df1.merge(df2, on=['id', 'date'])

# С суффиксами
df_merged = df1.merge(df2, on='id', suffixes=('_left', '_right'))

# Индикатор объединения
df_merged = df1.merge(df2, on='id', how='left', indicator=True)
```

### join()
```python
# Join по индексу
df_joined = df1.join(df2, lsuffix='_left', rsuffix='_right')

# Left join по индексу
df_joined = df1.join(df2, how='left')
```

---

## 10. Работа с временными рядами

### Парсинг дат
```python
# to_datetime()
df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Из отдельных колонок
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# date_range()
dates = pd.date_range('2024-01-01', periods=100, freq='D')
dates = pd.date_range('2024-01-01', '2024-12-31', freq='M')
dates = pd.date_range('2024-01-01', periods=24, freq='H')
```

### Атрибуты datetime
```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek
df['day_name'] = df['date'].dt.day_name()
df['month_name'] = df['date'].dt.month_name()
df['quarter'] = df['date'].dt.quarter
df['is_month_start'] = df['date'].dt.is_month_start
df['is_month_end'] = df['date'].dt.is_month_end

# Доступ
df['date'].dt.hour
df['date'].dt.minute
df['date'].dt.second
```

### Resample()
```python
# Установка индекса
df = df.set_index('date')

# Агрегация по времени
df.resample('D').mean()      # По дням
df.resample('W').mean()      # По неделям
df.resample('M').mean()      # По месяцам
df.resample('Q').mean()      # По кварталам
df.resample('Y').mean()      # По годам
df.resample('H').mean()      # По часам

# С разными агрегациями
df.resample('D').agg({
    'value': ['mean', 'sum'],
    'count': 'count'
})

# OHLC
df.resample('D').ohlc()
```

### Rolling()
```python
# Скользящее среднее
df['rolling_mean'] = df['value'].rolling(window=7).mean()
df['rolling_std'] = df['value'].rolling(window=7).std()

# Экспоненциальное среднее
df['ewm'] = df['value'].ewm(span=7).mean()

# Минимальный период
df['rolling_mean'] = df['value'].rolling(window=7, min_periods=3).mean()
```

### Сдвиг и разница
```python
# Сдвиг
df['prev_value'] = df['value'].shift(1)
df['next_value'] = df['value'].shift(-1)

# Разница
df['diff'] = df['value'].diff()
df['diff_2'] = df['value'].diff(2)

# Процентное изменение
df['pct_change'] = df['value'].pct_change()
```

---

## 11. Работа со строками

### str методы
```python
# Основные
df['name'].str.lower()
df['name'].str.upper()
df['name'].str.title()
df['name'].str.capitalize()
df['name'].str.strip()
df['name'].str.lstrip()
df['name'].str.rstrip()

# Поиск
df['name'].str.contains('pattern')
df['name'].str.startswith('A')
df['name'].str.endswith('e')
df['name'].str.find('pattern')

# Замена
df['name'].str.replace('old', 'new')
df['name'].str.replace('[aeiou]', '', regex=True)

# Извлечение
df['text'].str.extract(r'(\d+)')
df['text'].str.extract(r'(\w+)@(\w+)\.(\w+)')

# Разделение
df['full_name'].str.split(' ', expand=True)
df['path'].str.split('/', expand=True)

# Длина
df['name'].str.len()

# Паддинг
df['id'].str.zfill(5)
df['text'].str.pad(10, side='left')
```

### Регулярные выражения
```python
# С extract()
df[['first', 'last']] = df['name'].str.extract(r'(\w+)\s+(\w+)')

# С replace()
df['text'].str.replace(r'\d+', 'NUMBER', regex=True)

# С contains()
df[df['text'].str.contains(r'\b\d{3}\b', regex=True)]
```

---

## 12. Статистический анализ

### Описательная статистика
```python
df.describe()
df.describe(include='all')

# По колонкам
df['column'].mean()
df['column'].median()
df['column'].mode()
df['column'].std()
df['column'].var()
df['column'].skew()
df['column'].kurt()

# Ковариация и корреляция
df.cov()
df.corr()
df.corrwith(df['target'])
```

### Groupby статистика
```python
# Статистика по группам
df.groupby('category')['value'].describe()
df.groupby('category').agg(['mean', 'std', 'count'])

# T-test
from scipy import stats
group1 = df[df['category'] == 'A']['value']
group2 = df[df['category'] == 'B']['value']
t_stat, p_value = stats.ttest_ind(group1, group2)
```

### Аномалии
```python
# Z-score
z_scores = np.abs((df['value'] - df['value'].mean()) / df['value'].std())
outliers = df[z_scores > 3]

# IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['value'] < Q1 - 1.5*IQR) | (df['value'] > Q3 + 1.5*IQR)]
```

---

## 13. Визуализация

### Встроенные plot()
```python
import matplotlib.pyplot as plt

# Линейный график
df.plot(x='date', y='value')

# Столбчатая диаграмма
df['category'].value_counts().plot(kind='bar')

# Круговая диаграмма
df['category'].value_counts().plot(kind='pie')

# Гистограмма
df['value'].plot(kind='hist', bins=30)

# Boxplot
df.boxplot(column='value', by='category')

# Scatter plot
df.plot(kind='scatter', x='age', y='salary')

# Area plot
df.plot(kind='area', stacked=False)

# KDE
df['value'].plot(kind='kde')
```

### Seaborn интеграция
```python
import seaborn as sns

# Pairplot
sns.pairplot(df[['age', 'salary', 'score']])

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')

# Boxplot
sns.boxplot(x='category', y='value', data=df)

# Violin plot
sns.violinplot(x='category', y='value', data=df)

# Count plot
sns.countplot(x='category', data=df)

# Bar plot
sns.barplot(x='category', y='value', data=df)
```

---

## 14. Оптимизация производительности

### Типы данных
```python
# Оптимизация числовых типов
df['int_col'] = pd.to_numeric(df['int_col'], downcast='integer')
df['float_col'] = pd.to_numeric(df['float_col'], downcast='float')

# Категориальные типы
df['category'] = df['category'].astype('category')

# Проверка использования памяти
df.memory_usage(deep=True)
```

### Векторизация
```python
# Медленно - apply()
df['new'] = df['col'].apply(lambda x: x * 2)

# Быстро - векторизация
df['new'] = df['col'] * 2

# Медленно - цикл
for i in range(len(df)):
    df.loc[i, 'new'] = df.loc[i, 'a'] + df.loc[i, 'b']

# Быстро - векторизация
df['new'] = df['a'] + df['b']
```

### Чанки для больших файлов
```python
# Чтение по чанкам
chunk_iter = pd.read_csv('large_file.csv', chunksize=100000)

for chunk in chunk_iter:
    # Обработка чанка
    processed = chunk[chunk['value'] > 0]
    processed.to_csv('output.csv', mode='a', header=False)

# Dask для параллельной обработки
import dask.dataframe as dd
df = dd.read_csv('large_file.csv')
result = df.groupby('category')['value'].mean().compute()
```

---

## 15. Практические примеры

### Пример 1: Полный анализ данных
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка
df = pd.read_csv('sales.csv', parse_dates=['date'])

# Исследование
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Очистка
df = df.drop_duplicates()
df['price'] = df['price'].fillna(df['price'].median())
df = df[df['quantity'] > 0]

# Создание признаков
df['revenue'] = df['price'] * df['quantity']
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
df['is_weekend'] = df['day_of_week'] >= 5

# Анализ
monthly_revenue = df.groupby('month')['revenue'].sum()
category_stats = df.groupby('category').agg({
    'revenue': 'sum',
    'quantity': 'mean',
    'price': 'mean'
})

# Визуализация
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

monthly_revenue.plot(kind='bar', ax=axes[0, 0])
axes[0, 0].set_title('Monthly Revenue')

category_stats['revenue'].plot(kind='pie', ax=axes[0, 1])
axes[0, 1].set_title('Revenue by Category')

df['price'].plot(kind='hist', bins=30, ax=axes[1, 0])
axes[1, 0].set_title('Price Distribution')

sns.boxplot(x='category', y='revenue', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Revenue by Category')

plt.tight_layout()
plt.show()
```

### Пример 2: Подготовка данных для ML
```python
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Загрузка
df = pd.read_csv('dataset.csv')

# Разделение признаков и target
X = df.drop('target', axis=1)
y = df['target']

# Обработка пропусков
X = X.fillna(X.median())

# Кодирование категориальных
categorical_cols = X.select_dtypes(include=['object']).columns
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Создание DataFrame с обработанными данными
df_processed = pd.DataFrame(X_scaled, columns=X.columns)
df_processed['target'] = y

# Сохранение
df_processed.to_csv('processed_data.csv', index=False)
```

---

## Шпаргалка по основным функциям

| Задача | Функция/Метод |
|--------|---------------|
| Загрузка CSV | `pd.read_csv('file.csv')` |
| Сохранение | `df.to_csv('out.csv', index=False)` |
| Первые строки | `df.head()` |
| Информация | `df.info()` |
| Статистика | `df.describe()` |
| Фильтрация | `df[df['col'] > 5]` |
| Группировка | `df.groupby('col').mean()` |
| Сортировка | `df.sort_values('col')` |
| Пропуски | `df.fillna(0)`, `df.dropna()` |
| Дубликаты | `df.drop_duplicates()` |
| Groupby Agg | `df.groupby('col').agg({'val': ['mean', 'sum']})` |
| Pivot Table | `df.pivot_table(values, index, columns)` |
| Merge | `df1.merge(df2, on='id')` |
| Datetime | `pd.to_datetime(df['date'])` |
| Resample | `df.resample('D').mean()` |
| Rolling | `df['val'].rolling(7).mean()` |
| Apply | `df['col'].apply(func)` |
| Строки | `df['col'].str.contains('pattern')` |
| Plot | `df.plot()`, `df.plot.scatter()` |
