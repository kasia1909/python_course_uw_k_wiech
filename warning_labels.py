
import pandas as pd
import matplotlib.pyplot as plt

def warning_labels_analysis(df):
    '''
    This function accepts the dataframe and returns the global mean lung cancer incidence and mean lung cancer incidence in countries with different
    types of warning labels on cigarette packaging. It also displays histograms for lung cancer rates across different types of packaging
    '''
    #replaces values in df with 1,.5,0,-1 for iteration
    df['Tobacco packaging restrictions\nUse of graphic warning labels and plain packaging']=df['Tobacco packaging restrictions\nUse of graphic warning labels and plain packaging'].replace(['Graphic warning labels','Graphic warning labels + plain packaging','No graphic warning labels', 'No data'],[1,.5,0,-1])
    
   
    for sex in ['male','female']: #runs through each sex, prints global mean
        selected_columns = df[[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018','Tobacco packaging restrictions\nUse of graphic warning labels and plain packaging']]
        df_sex = selected_columns.copy()
        df_sex.drop(index=df[df[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        mean_global = df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'].mean()
        print(f'The mean lung cancer incidence for {sex} across all countries regardless of packing is: {mean_global}')
        
    
        for i in [1,.5,0,-1]: #runs through each label type and gives mean 
            i_warnings = df_sex.loc[df_sex['Tobacco packaging restrictions\nUse of graphic warning labels and plain packaging'] == i]
            df_i = i_warnings.copy()
            mean_i = df_i[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'].mean()
            if i == 1:
                i = "graphic warning labels"
            elif i == .5:
                i = "mixed packaging (some graphic, some normal)"
            elif i == 0:
                i = "no warning labels"
            else:
                i = "no data on warning labels"
            print(f'The mean cancer incidence per 100,000 {sex}s across all countries with {i} is: {mean_i}')
       
        for i in [1,.5,0,-1]: #creates histogram for each label type
            i_warnings = df_sex.loc[df_sex['Tobacco packaging restrictions\nUse of graphic warning labels and plain packaging'] == i]
            df_i = i_warnings.copy()
            plt.hist(df_i[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'], 
                bins=10, edgecolor='black')
            if i == 1:
                i = "graphic warning labels"
            elif i == .5:
                i = "mixed packaging (some graphic, some normal)"
            elif i == 0:
                i = "no warning labels"
            else:
                i = "no data on warning labels"
            plt.xlabel(f'Lung cancer incidence rates per 100,000 {sex}s across all countries with {i}')
            plt.ylabel('Frequency')
            plt.show()
