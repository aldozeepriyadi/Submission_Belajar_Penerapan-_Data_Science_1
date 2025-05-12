import numpy as np
import pandas as pd
import joblib
import warnings
from sklearn.preprocessing import FunctionTransformer

def simple_preprocessing(x):
  # Hapus Kolom yang tidak diperlukan
  x = x.drop(columns=['EmployeeId','EmployeeCount', 'StandardHours', 'Over18'])

  # Menghapus Fitur berdasarkan hasil uji chi-square
  x =  x.drop(columns=['PerformanceRating', 'Education',  'RelationshipSatisfaction', 'EducationField'])

  return x

# Bungkus hasil preprocessing menggunakan function_transformer
preprocessor = FunctionTransformer(simple_preprocessing)
load_model = joblib.load('model_rf.pkl')
# Membuat data baru secara acak
def generate_new_data():
    data = {
        'EmployeeId': np.random.randint(1, 1471),
        'Age': np.random.randint(18, 95),
        'BusinessTravel': np.random.choice(['Non-Travel', 'Travel_Frequently', 'Travel_Rarely']),
        'DailyRate': np.random.randint(102, 1499),
        'Department': np.random.choice(['Research & Development', 'Human Resources', 'Sales']),
        'DistanceFromHome': np.random.randint(1, 29),
        'Education': np.random.randint(1, 5),
        'EducationField': np.random.choice(['Medical', 'Life Sciences', 'Marketing', 'Technical Degree', 'Human Resources', 'Other']),
        'EmployeeCount': 1470,
        'EnvironmentSatisfaction': np.random.randint(1, 4),
        'Gender': np.random.choice(['Female', 'Male']),
        'HourlyRate': np.random.randint(30, 100),
        'JobInvolvement': np.random.randint(1, 4),
        'JobLevel': np.random.randint(1, 5),
        'JobRole': np.random.choice(['Healthcare Representative', 'Research Scientist', 'Sales Executive', 'Manager',
                                      'Laboratory Technician', 'Research Director', 'Manufacturing Director',
                                      'Human Resources', 'Sales Representative']),
        'JobSatisfaction': np.random.randint(1, 4),
        'MaritalStatus': np.random.choice(['Married', 'Single', 'Divorced']),
        'MonthlyIncome': np.random.randint(1009, 19999),
        'MonthlyRate': np.random.randint(2094, 26999),
        'NumCompaniesWorked': np.random.randint(0, 9),
        'Over18': 'Y',
        'OverTime': np.random.choice(['No', 'Yes']),
        'PercentSalaryHike': np.random.randint(11, 25),
        'PerformanceRating': np.random.randint(3, 4),
        'RelationshipSatisfaction': np.random.randint(1, 4),
        'StandardHours': 80,
        'StockOptionLevel': np.random.randint(0, 3),
        'TotalWorkingYears': np.random.randint(0, 39),
        'TrainingTimesLastYear': np.random.randint(0, 9),
        'WorkLifeBalance': np.random.randint(1, 5),
        'YearsAtCompany': np.random.randint(0, 41),
        'YearsInCurrentRole': np.random.randint(0, 19),
        'YearsSinceLastPromotion': np.random.randint(0, 16),
        'YearsWithCurrManager': np.random.randint(0, 17)
    }

    return pd.DataFrame([data])

# Menghasilkan data baru
new_data = generate_new_data()

# Melakukan prediksi
prediction = load_model.predict(new_data)

# Menentukan hasil prediksi
result = 'Attrition: Yes' if prediction[0] == 1 else 'Attrition: No'

# Menampilkan hasil
new_data['Attrition'] = prediction
print(result)
print(new_data)