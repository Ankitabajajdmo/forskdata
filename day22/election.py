import pandas as pd
df=pd.read_csv("election_data.csv")
df=df.iloc[:,1:]
x=list(set(df["Name_of_Candidate"]))

#candidates who have contested in more than one Assembly elections
multi_assmbly=[]
for i in x:
    temp = list(set(df["Assembly_no"][df["Name_of_Candidate"]==i]))
    if len(temp) > 1:
        multi_assmbly.append(i)

#candidates contest from the different constituency in all the elections
diff_constituency=[]
constituency_no = []
for i in multi_assmbly:
    same_contituency=list(set(df["Constituency_no"][df["Name_of_Candidate"]==i]))
    if len(same_contituency) > 1:
         diff_constituency.append(i)
         constituency_no.append(same_contituency)
        
#effect on the performance of the candidate
\]\
  ]=]=]
df2= []
#new_df.columns=["Name_of_Candidate"]
for i,j in zip(diff_constituency,constituency_no):
    votes = []
    for p in j:
        votes.append(df["Total_valid_votes"][(df["Constituency_no"]==p) & (df["Name_of_Candidate"]==i)].mean())
    df2.append(votes)



