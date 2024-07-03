import pandas as pd


def clean_raw_ess_11_data(data):

    clean_data = pd.DataFrame()

    clean_data["Country"] = data["cntry"]
    clean_data["Respondent_ID"] = data["idno"]
    clean_data["ESS_Round"] = data["essround"]
    clean_data["National_Election_Vote_First"] = data["prtvgde1"]
    clean_data["National_Election_Vote_Second"] = data["prtvgde2"]
    clean_data["Closest_Political_Party"] = data["prtclgde"]
    clean_data["Closeness_to_Party"] = data["prtdgcl"]
    clean_data["Satisfaction_Economy"] = data["stfeco"]
    clean_data['Stance_Homosexuality'] = data["freehms"]
    clean_data['Stance_Homosexual_Adoption'] = data["hmsfmlsh"]
    clean_data['Stance_EU_Unification'] = data["euftf"]
    clean_data["Stance_Same_Race_Immigration"] = data["imsmetn"]
    clean_data["Stance_Other_Race_Immigration"] = data["imdfetn"]
    clean_data["Stance_Immigration_Outside_Europe"] = data["impcntr"]
    clean_data["Stance_Immigration_on_Economy"] = data["imueclt"]
    clean_data["Stance_Culture_Life_Immigrants"] = data["imueclt"]
    clean_data["Strength_Religiosity"] = data["rlgdgr"]
    clean_data['Born_in_Country'] = data["brncntr"]
    clean_data["Age"] = data["agea"]
    clean_data["Education_Level_ES_ISCED"] = data["eisced"]
    clean_data["Household_Total_Income"] = data["hinctnta"]

    return clean_data