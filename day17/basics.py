DUMMY VARIABLE TRAP:
    drop any 1 column generated by one hot encoding
        bcoz we can generate nth column using n-1 one encoded columns (to reduce redundancy)
        
    ex: features=features[:,1:]

reshape(-1,1) 
reshape(1,-1)
    
backward elimination:
    statsmodel library - requirement is insert one constant value column to dataframe

***Pvalue >> gives importance of feature  
        greater pvalue -- less is importance of a feature

>>eliminate one feature at a time

>>eliminate features with pvalue > 5% = 0.05