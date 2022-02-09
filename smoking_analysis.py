
import pandas as pd
from IPython.display import display

def smoking_cancer_analysis(df, outlier):
    '''
    This function accepts two arguments, a dataframe and a boolean value that decided whether to include outliers (True to include outliers, False to not).
    It provides a scatterplot and the correlation value for proportion of smokers for each sex/gender and the lung cancer incidence
    '''
    
    #runs through both sexes
    for sex,gender in [['male','men'],['female','women']]:
        selected_columns = df[[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] == 'No data'].index, inplace=True)
        df_sex = df_sex.astype('float64')
    
        if outlier == True:
        ## RUN THIS LINE TO REMOVE THE OUTLIER IN THE MALE CANCER DATA
            df_sex = df_sex[~(df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] >= 60)]
        ## 
        else:
            None #skips if not on
            
        smoke = df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}']
        cancer = df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']
        corr = smoke.corr(cancer)
        print(f'The correlation between lung cancer and smoking prevelance for {gender} is {corr}')
    
        df_sex.plot.scatter(f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}',
                        f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')

def smoke_rank(df,rank_type,number):
    '''
    This function accepts three arguments, a dataframe, a rank type (most, least, or both) and an integer and returns 
    the countries with the most or least amount of smokers.
    '''
    if type(number) != int:
        raise ValueError('Please enter an integer into the second argument')
    for sex,gender in [['male','men'],['female','women']]:
        selected_columns = df[['Country or Territory',
                               f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] == 'No data'].index, inplace=True)

        df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] = pd.to_numeric(df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'], downcast="float")
        df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
        top_smoke = df_sex.nlargest(number,f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}')
        bot_smoke = df_sex.nsmallest(number,f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}')
        if rank_type == 'Most':
            print(f'The {number} countries with largest proportion of {sex} smokers are listed below')
            display(top_smoke)
        elif rank_type == 'Least':
            print(f'The {number} countries with smallest proportion of {sex} smokers are listed below')
            display(bot_smoke)
        elif rank_type == 'Both':
            print(f'The {number} countries with largest proportion of {sex} smokers are listed below')
            display(top_smoke)
            print(f'The {number} countries with smallest proportion of {sex} smokers are listed below')
            display(bot_smoke)
        else:
            raise ValueError("Please enter either 'Most', 'Least' or 'Both' into the second argument")


def cancer_rank(df,rank_type,number):
    '''
    This function accepts three arguments: a dataframe, a rank type("Most", "Least", or "Both"), and an integer.
    It returns a list of the countries with the highest or lowest lung cancer incidence.
    '''
    if type(number) != int:
        raise ValueError('Please enter an integer into the second argument')
    for sex,gender in [['male','men'],['female','women']]:
        selected_columns = df[['Country or Territory',
                               f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] == 'No data'].index, inplace=True)

        df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] = pd.to_numeric(df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'], downcast="float")
        df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
        top_cancer = df_sex.nlargest(number, f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')
        bot_cancer = df_sex.nsmallest(number,f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')
        if rank_type == 'Most' or 'Both':
            print(f'The {number} countries with largest proportion of {gender} with lung cancer are listed below')
            display(top_cancer)
        elif rank_type == 'Least' or 'Both':
            print(f'The {number} countries with smallest proportion of {gender} with lung cancer are listed below')
            display(bot_cancer)
        else:
            raise ValueError("Please enter either 'Most', 'Least' or 'Both' into the second argument")

def compare_cancer_smoker(df,rank_type, number):
    '''
    This function accepts three arguments, dataframe, rank type ("Most", "Least", "Both") and an integer. 
    It returns a list of countries that are on both the highest/lowest lung cancer list and highest/lower smokers list.
    '''
    if type(number) != int:
        raise ValueError('Please enter an integer into the second argument')
        
    ## generate both dataframes
    for sex,gender in [['male','men'],['female','women']]:
        selected_columns = df[['Country or Territory',
                               f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] == 'No data'].index, inplace=True)

        df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'] = pd.to_numeric(df_sex[f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}'], downcast="float")
        df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
       
        #generates orginial dataframes
        top_smoke = df_sex.nlargest(number,f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}')
        bot_smoke = df_sex.nsmallest(number,f'Smoking prevalence {sex}\nPrevalence (%) of daily smoking for {gender}')
        top_cancer = df_sex.nlargest(number, f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')
        bot_cancer = df_sex.nsmallest(number,f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')
        ##
        
        #generates comparison of dataframes
        mergedTop = pd.merge(top_cancer, top_smoke, how='inner')
        mergedBottom = pd.merge(bot_cancer,bot_smoke,how='inner')
        
        if rank_type == 'Most':
            print(f'Countries that appear on both the top {number} smoker list and top {number} lung cancer list for {gender} are:')
            display(mergedTop)
        elif rank_type == 'Least':
            print(f'Countries that appear on both the bottom {number} smoker list and bottom {number} lung cancer list for {gender} are:')
            display(mergedBottom)
        elif rank_type == 'Both':
            print(f'Countries that appear on both the top {number} smoker list and top {number} lung cancer list for {gender} are:')
            display(mergedTop)
            print(f'Countries that appear on both the bottom {number} smoker list and bottom {number} lung cancer list for {gender} are:')
            display(mergedBottom)
        else:
            raise ValueError("Please enter either 'Most', 'Least' or 'Both' into the second argument") 
