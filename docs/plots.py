import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv('/Users/huubal/Documents/Documents - Huub’s MacBook Pro/infoVis/infomat123/docs/NSDUH_Workforce_Adults.csv')
# Column names
columns = ['race_str', 'PersonalIncome', 'education', 'countofdrugs_ever', 'FamilyIncome']

# Create DataFrame
df = pd.DataFrame(df, columns=columns)

# Using qcut
df['amount_drugs_qcut'], qcut_bins = pd.cut(df['countofdrugs_ever'], bins=3, labels=['Low', 'Medium','High'], retbins=True)
print("Bins for qcut:", qcut_bins)

# filter rows with only high and medium drug use.
df_filtered = df[df['amount_drugs_qcut'].isin(['Medium', 'High'])]
# Create Parallel Categories plot
parcatsall = go.Figure(data=[go.Parcats(dimensions=[
    {'label': 'Personal Income', 'values': df['PersonalIncome'], 'categoryorder': 'category ascending'},
    {'label': 'Education', 'values': df['education'], 'categoryorder': 'category ascending'},
    {'label': 'Family Income', 'values': df['FamilyIncome'], 'categoryorder': 'category ascending'},
    {'label': 'Drug Use', 'values': df['amount_drugs_qcut']},
],
    line={'color': df['amount_drugs_qcut'].map({'Low': 'lightblue','Medium': 'lightgreen', 'High': 'orangered'})},
    labelfont={'size': 12},
    tickfont={'size': 12},
    arrangement='freeform'
)],
    layout={'title': 'Analysis of Income, Education, and Drug Use'})
# Show plot
parcatsall.show()

# Create Parallel Categories plot
parcats = go.Figure(data=[go.Parcats(dimensions=[
    {'label': 'Personal Income', 'values': df_filtered['PersonalIncome'], 'categoryorder': 'category ascending'},
    {'label': 'Education', 'values': df_filtered['education'], 'categoryorder': 'category ascending'},
    {'label': 'Family Income', 'values': df_filtered['FamilyIncome'], 'categoryorder': 'category ascending'},
    {'label': 'Drug Use', 'values': df_filtered['amount_drugs_qcut']},
],
    line={'color': df_filtered['amount_drugs_qcut'].map({'Medium': 'lightgreen', 'High': 'orangered'})},
    labelfont={'size': 12},
    tickfont={'size': 12},
    arrangement='freeform'
)],
    layout={'title': 'Analysis of Income, Education, and Drug Use'})
# Show plot
parcats.show()