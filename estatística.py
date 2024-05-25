import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame with examples of employee variables
data = {
    'ID': [101, 102, 103, 104, 105],
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'José'],
    'Idade': [35, 28, 42, 39, 45], # Continuous quantitative variable (age)
    'Departamento': ['Vendas', 'TI', 'RH', 'Marketing', 'Vendas'], # Nominal qualitative variable (department)
    'Salário': [5000, 6000, 5500, 7000, 4800], # Continuous quantitative variable (salary)
    'Nível_Educação': ['Graduação', 'Pós-graduação', 'Graduação', 'Graduação', 'Mestrado'], # Ordinal qualitative variable (education level)
    'Horas_Trabalhadas': [160, 180, 160, 190, 170], # Discrete quantitative variable (hours worked per week)
    'Avaliação_Desempenho': ['Bom', 'Regular', 'Ótimo', 'Bom', 'Bom'] # Ordinal qualitative variable (performance evaluation)
}

# Creating the DataFrame
df = pd.DataFrame(data)

