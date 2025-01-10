
---> The data is of 4 days having forecasting of each minute.
---> The solar system is not operating from 12.00pm to 12.59am in different timezone
---> first the model is trained using se2vec model implemented optimisers and layer optimization and trained
     by seq2seq rnn and lstm
---> Added an additional feature where it value ranges from(0 to 23) and it is zero for values 12 to 23 and zero
---> model          r^2                     MAE
     seq2vec        0.9682738537291566      2.55
     vanilla rnn    0.9761708124406997      4.977
     lstm           0.9823860561800698      3.398
---> for last two model mae is less compared to first which suggests the complexity of the models
---> for implementing the website we can use fastapi and save the data(data storage) in an database and create api for to query the      
     information and the model can by hosted by tensorflow serving or can done using retrieving data and loading the weights.
     And lastly for fast deployment we can use streamlit framework for designing the website and hosting it in streamlit itself for free.
