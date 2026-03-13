from imblearn.under_sampling import EditedNearestNeighbours
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer


def CTGANENN(minClass,majClass,genData,targetLabel):

    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(minClass)
    metadata.validate()

    synthesizer = CTGANSynthesizer(metadata)
    synthesizer.fit(minClass)
    synthetic_data = synthesizer.sample(num_rows=genData)

    #concat original data and gan data
    data_concat = pd.concat([minClass, synthetic_data])
    # combine data churn and not churn
    data=pd.concat([majClass, data_concat])
    enn = EditedNearestNeighbours(n_neighbors=3)
    X=data.drop([targetLabel],axis=1)
    y=data[targetLabel]
    X, y = enn.fit_resample(X, y)

    return X,y
