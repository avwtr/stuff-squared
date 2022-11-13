import pandas as pd

hard_coded = pd.read_csv("hardcoded_responses.csv")

def read_response(respo):
    if respo in hard_coded["Key"]:
        filtered = hard_coded[hard_coded["Key"] == respo]
        return filtered["Value"][0]
    else:
        return False
