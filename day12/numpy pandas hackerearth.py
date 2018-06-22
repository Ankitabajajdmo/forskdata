import pandas as pd
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)


#********************************************************************
def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'

lower = lambda x: x.lower()
data['food'] = data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')

#**********************************************************************

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)

pd.cut(ages,bins,right=False)

cats.codes

pd.value_counts(cats)

bin_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
new_cats = pd.cut(ages, bins,labels=bin_names)

pd.value_counts(new_cats)
pd.value_counts(new_cats).cumsum()

#************************************************************************
import numpy as np
df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
df

grouped = df['data1'].groupby(df['key1'])
grouped.mean()
#************************************************************************
dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
df[:3]
df['20130101':'20130104']
df.loc[:,['A','B']]
df.loc['20130102':'20130103',['A','B']]
df.iloc[3]
df.iloc[2:4, 0:2]
df.iloc[[1,5],[0,2]]
df[df.A > 0.3]
df2 = df.copy()
df2['E']=['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]
df2[~df2['E'].isin(['two','four'])]
df.query('A > C')
df.query('A < B | C > A')

#create a data frame
import pandas as pd
import numpy as np
data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data.pivot_table(values='ounces',index='group',aggfunc='count')
