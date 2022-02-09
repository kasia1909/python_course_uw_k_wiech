
import pandas as pd

def outdoor_pol_cancer_analysis(df):
    '''
    This function accepts one argument a dataframe and returns a scatterplot and the correlation coefficent for outdoor pollution and lung cancer incidence. 
    '''
    for sex in ['male','female']:
        selected_columns = df[['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017'] == 'No data'].index, inplace=True)
        df_sex = df_sex.astype('float64')
    
        outdoor_pol = df_sex['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017']
        cancer = df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']
        corr = cancer.corr(outdoor_pol)
        print(f'The correlation between lung cancer and outdoor pollution for {sex}s is {corr}')
    
        df_sex.plot.scatter('Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017',
                        f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')

def indoor_pol_cancer_analysis(df):
    '''
    This function accepts one argument a dataframe and returns a scatterplot and the correlation coefficent for indoor pollution and lung cancer incidence.
    '''
    for sex in ['male','female']:
        selected_columns = df[['Indoor air pollution\nProportion (%) of population using solid fuels in 2017',
                           f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']]
        df_sex = selected_columns.copy()
        df_sex.drop(index=df_sex[df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
        df_sex.drop(index=df_sex[df_sex['Indoor air pollution\nProportion (%) of population using solid fuels in 2017'] == 'No data'].index, inplace=True)
        df_sex = df_sex.astype('float64')
    
        indoor_pol = df_sex['Indoor air pollution\nProportion (%) of population using solid fuels in 2017']
        cancer = df_sex[f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018']
        corr = cancer.corr(indoor_pol)
        print(f'The correlation between lung cancer and indoor pollution for {sex}s is {corr}')
    
        df_sex.plot.scatter('Indoor air pollution\nProportion (%) of population using solid fuels in 2017',
                        f'Lung cancer incidence rates, {sex}\nAge-standardized rate (world) per 100,000, all ages, 2018')

def outdoor_pol_rank(df,rank_type,number):
    '''
    This function accepts a dataframe, a rank type ('Most', 'Least', or 'Both'), and an integer.
    It returns a dataframe with the countries with highest amount of outdoor air pollution.
    '''
    if type(number) != int:
        raise ValueError('Please enter an integer into the second argument')
    selected_columns = df[['Country or Territory',
                               'Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017',
                           'Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018',
                               'Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018',
                          'Smoking prevalence male\nPrevalence (%) of daily smoking for men',
                          'Smoking prevalence female\nPrevalence (%) of daily smoking for women']]
    df_out = selected_columns.copy()
     
    #removes all cells with 'No data'
    df_out.drop(index=df_out[df_out['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
    df_out.drop(index=df_out[df_out['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
    df_out.drop(index=df_out[df_out['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017'] == 'No data'].index, inplace=True)
    df_out.drop(index=df_out[df_out['Smoking prevalence male\nPrevalence (%) of daily smoking for men'] == 'No data'].index, inplace=True)
    df_out.drop(index=df_out[df_out['Smoking prevalence female\nPrevalence (%) of daily smoking for women'] == 'No data'].index, inplace=True)
    
    #converts all to floats so they can be ranked
    df_out['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017'] = pd.to_numeric(df_out['Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017'], downcast="float")
    df_out['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_out['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
    df_out['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_out['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
    df_out['Smoking prevalence male\nPrevalence (%) of daily smoking for men'] = pd.to_numeric(df_out['Smoking prevalence male\nPrevalence (%) of daily smoking for men'], downcast='float')
    df_out['Smoking prevalence female\nPrevalence (%) of daily smoking for women'] = pd.to_numeric(df_out['Smoking prevalence female\nPrevalence (%) of daily smoking for women'], downcast='float')
    
    
    top_out_pol = df_out.nlargest(number, 'Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017')
    bot_out_pol = df_out.nsmallest(number,'Outdoor air pollution\nAverage annual population-weighted concentrations of PM2.5 (particulate matter of 2.5 μm diameter or less), measured in μg/m3, 2017')
        
    if rank_type == 'Most':
        print(f'The {number} countries with the most outdoor air pollution are')
        display(top_out_pol)
    elif rank_type == 'Least':
        print(f'The {number} countries with the least outdoor air pollution are:')
        display(bot_out_pol)
    elif rank_type == 'Both': #for some reason or would not work in earlier in the if statement and i had to add another elif
        print(f'The {number} countries with the most outdoor air pollution are')
        display(top_out_pol)
        print(f'The {number} countries with the least outdoor air pollution are:')
        display(bot_out_pol)
    else:
        raise ValueError("Please enter either 'Most', 'Least' or 'Both' into the second argument")

def indoor_pol_rank(df,rank_type,number):
    '''
    This function accepts three arguments; a dataframe, a rank type ('Most', 'Least', or 'Both') and an integer.
    It returns a dataframe with the countries with the highest indoor air pollution.
    '''
    if type(number) != int:
        raise ValueError('Please enter an integer into the second argument')
    selected_columns = df[['Country or Territory',
                               'Indoor air pollution\nProportion (%) of population using solid fuels in 2017',
                           'Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018',
                               'Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018',
                          'Smoking prevalence male\nPrevalence (%) of daily smoking for men',
                          'Smoking prevalence female\nPrevalence (%) of daily smoking for women']]
    df_in = selected_columns.copy()
    
    #removes cells with no data
    df_in.drop(index=df_in[df_in['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
    df_in.drop(index=df_in[df_in['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'] == 'No data'].index, inplace=True)
    df_in.drop(index=df_in[df_in['Indoor air pollution\nProportion (%) of population using solid fuels in 2017'] == 'No data'].index, inplace=True)
    df_in.drop(index=df_in[df_in['Smoking prevalence male\nPrevalence (%) of daily smoking for men'] == 'No data'].index, inplace=True)
    df_in.drop(index=df_in[df_in['Smoking prevalence female\nPrevalence (%) of daily smoking for women'] == 'No data'].index, inplace=True)
    
    #converts data to floats
    df_in['Indoor air pollution\nProportion (%) of population using solid fuels in 2017'] = pd.to_numeric(df_in['Indoor air pollution\nProportion (%) of population using solid fuels in 2017'], downcast="float")
    df_in['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_in['Lung cancer incidence rates, male\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
    df_in['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'] = pd.to_numeric(df_in['Lung cancer incidence rates, female\nAge-standardized rate (world) per 100,000, all ages, 2018'], downcast="float")
    df_in['Smoking prevalence male\nPrevalence (%) of daily smoking for men'] = pd.to_numeric(df_in['Smoking prevalence male\nPrevalence (%) of daily smoking for men'], downcast='float')
    df_in['Smoking prevalence female\nPrevalence (%) of daily smoking for women'] = pd.to_numeric(df_in['Smoking prevalence female\nPrevalence (%) of daily smoking for women'], downcast='float')
    
    top_in_pol = df_in.nlargest(number, 'Indoor air pollution\nProportion (%) of population using solid fuels in 2017')
    bot_in_pol = df_in.nsmallest(number,'Indoor air pollution\nProportion (%) of population using solid fuels in 2017')
        
    if rank_type == 'Most':
        print(f'The {number} countries with the most indoor air pollution are')
        display(top_in_pol)
    elif rank_type == 'Least':
        print(f'The {number} countries with the least indoor air pollution are:')
        display(bot_in_pol)
    elif rank_type == 'Both': #for some reason or would not work in earlier in the if statement and i had to add another elif
        print(f'The {number} countries with the most indoor air pollution are')
        display(top_in_pol)
        print(f'The {number} countries with the least indoor air pollution are:')
        display(bot_in_pol)
    else:
        raise ValueError("Please enter either 'Most', 'Least' or 'Both' into the second argument")
