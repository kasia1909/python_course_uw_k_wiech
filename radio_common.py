
import pandas as pd
def radiotherapy_cancer_survivor_analysis(df):
    '''
    This function accepts a dataframe and returns the correlation coefficent between radiotherapy availabilty 
    and the number of cancer survivors in a country.
    '''
    selected_columns = df[['Radiotherapy availability\nNumber of radiotherapy machines per 1,000 cancer patients',
                          'Cancer survivors\nEstimated number of cancer survivors diagnosed within the past five years per 100,000 population, both sexes, 2018']]
    df_radio = selected_columns.copy()
    
    #drop rows with cells with no data
    df_radio.drop(index=df_radio[df_radio['Radiotherapy availability\nNumber of radiotherapy machines per 1,000 cancer patients'] == 'No data'].index, inplace=True)
    df_radio.drop(index=df_radio[df_radio['Cancer survivors\nEstimated number of cancer survivors diagnosed within the past five years per 100,000 population, both sexes, 2018'] == 'No data'].index, inplace=True)
    df_radio = df_radio.astype('float64')
    
    #create variable for corr
    radio = df_radio['Radiotherapy availability\nNumber of radiotherapy machines per 1,000 cancer patients']
    cancer_surviors = df_radio['Cancer survivors\nEstimated number of cancer survivors diagnosed within the past five years per 100,000 population, both sexes, 2018']
    corr = cancer_surviors.corr(radio)
    print('The correlation between cancer surviors and radiotherapy availablity is:')
    print(corr)
    
    df_radio.plot.scatter('Radiotherapy availability\nNumber of radiotherapy machines per 1,000 cancer patients',
                          'Cancer survivors\nEstimated number of cancer survivors diagnosed within the past five years per 100,000 population, both sexes, 2018')


def top_cancer(df):
    '''
    This functions accepts a dataframe and retuns the top cancers and cancers deaths worldwide by gender.
    '''
    selected_columns = df[['Most common cancer cases worldwide, females\n2018',
                      'Most common cancer deaths worldwide, females\n2018',
                          'Most common cancer cases worldwide, males\n2018',
                          'Most common cancer deaths worldwide, males\n2018']]
    df_cancer_common = selected_columns.copy()
    
    dfs = []
    
    #loops through each colums and finds top values and creates one df with top values
    for col in df_cancer_common.columns:
        top_values = []
        top_values = df_cancer_common[col].mode()
        dfs.append(pd.DataFrame({col: top_values}).reset_index(drop=True))
    pd.concat(dfs, axis=1)
    return dfs

def leading_cause_of_death_count(df,age_group):
    '''
    This function returns the value counts for how many countries cancer is the leading cause of death.
    It accepts two arguments: a dataframe and the age group ('30-69','Under 70',).
    '''
    if age_group == '30-69':
        print(df['Cancer rank as leading cause of death among 30-69\n2016'].value_counts())
    elif age_group == 'Under 70':
        print(df['Cancer rank as leading cause of death among <70\n2016'].value_counts())
    else:
        raise ValueError('Please enter either "30-69" or "Under 70" into the second argument')
