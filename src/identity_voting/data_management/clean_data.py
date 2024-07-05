import pandas as pd
import numpy as np


def clean_raw_ess_11_data(data):

    clean_data = pd.DataFrame()

    clean_data["Country"] = data["cntry"]
    clean_data["Respondent_ID"] = data["idno"]
    clean_data["ESS_Round"] = data["essround"]
    clean_data["National_Election_Vote_First_Germany"] = data["prtvgde1"]
    clean_data["National_Election_Vote_Second_Germany"] = data["prtvgde2"]
    clean_data["Closest_Political_Party_Germany"] = pd.to_numeric(data["prtclgde"], errors="coerce")
    clean_data["Closest_Political_Party_Austria"] = pd.to_numeric(data["prtcleat"], errors='coerce')
    clean_data["Closest_Political_Party_Switzerland"] = pd.to_numeric(data["prtclhch"], errors="coerce")
    clean_data["Closeness_to_Party"] = data["prtdgcl"]
    clean_data["Satisfaction_Economy"] = data["stfeco"]
    clean_data['Stance_Homosexuality'] = data["freehms"].replace([7, 8, 9], pd.NA)
    clean_data['Stance_Homosexual_Adoption'] = data["hmsfmlsh"].replace([7, 8, 9], pd.NA)
    clean_data['Stance_EU_Unification'] = data["euftf"].replace([7, 8, 9], pd.NA)
    clean_data["Stance_Same_Race_Immigration"] = data["imsmetn"].replace([7, 8, 9], pd.NA)
    clean_data["Stance_Other_Race_Immigration"] = data["imdfetn"].replace([7, 8, 9], pd.NA)
    clean_data["Stance_Immigration_Outside_Europe"] = data["impcntr"].replace([7, 8, 9], pd.NA)
    clean_data["Stance_Immigration_on_Economy"] = data["imueclt"].replace([7, 8, 9], pd.NA)
    clean_data["Stance_Culture_Life_Immigrants"] = data["imueclt"].replace([7, 8, 9], pd.NA)
    clean_data["Strength_Religiosity"] = data["rlgdgr"].replace([77,88,99], pd.NA)
    clean_data["Strength_Religiosity_Halfed"] = clean_data["Strength_Religiosity"] / 2
    clean_data['Born_in_Country'] = data["brncntr"]
    clean_data["Age"] = data["agea"].replace(999, pd.NA)
    clean_data["Education_Level_ES_ISCED"] = data["eisced"]
    clean_data["Household_Total_Income"] = data["hinctnta"]

    clean_data["Closest_Political_Party_Summary"] = extract_non_na_values(clean_data[["Closest_Political_Party_Germany", "Closest_Political_Party_Austria",                                     "Closest_Political_Party_Switzerland"]])
    
    clean_data["Right_Wing_Indicator"] = create_right_wing_indicator(voting_codes = clean_data["Closest_Political_Party_Summary"], 
                                                                     country = clean_data["Country"])

    return clean_data



def create_right_wing_indicator(voting_codes: pd.Series, 
                                country: pd.Series) -> pd.Series:
    """
    Create a right wing indicator based on the voting codes. The right-wing parties are:
    AfD (code 7) for Germany, 
    FPÖ (code 3) for Austria.

    Args:

    voting_codes (pd.Series): A Series with the voting codes.
    country (pd.Series): A Series with the country codes.

    Returns:
    pd.Series: A Series with the right-wing indicator (1/0).
    """

    # Define the right-wing party codes for each country
    right_wing_parties = {
        'DE': 7,  # AfD
        'AT': 3 ,  # FPÖ
        'CH': 1 # SVP

    }
    
    # Create a DataFrame from the inputs
    df = pd.DataFrame({'country': country, 'voting_codes': voting_codes})
    
    # Replace country names with their corresponding right-wing party codes
    df['right_wing_code'] = df['country'].map(right_wing_parties)
    
    # Create the right-wing indicator
    right_wing_indicator = (df['voting_codes'] == df['right_wing_code']).astype(int)
    
    return right_wing_indicator





def extract_non_na_values(df: pd.DataFrame) -> pd.Series:
    """
    This function takes a DataFrame where all but one column are NA and returns a Series
    with the only non-NA values.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame with several columns, where all but one column are NA.
    
    Returns:
    pd.Series: A Series with the non-NA values.
    """

    def find_non_na(row):
        # Replace 'NaN' string with np.nan for consistent processing
        row = row.replace('NaN', np.nan)
        non_na_values = row.dropna()
        if not non_na_values.empty:
            return non_na_values.iloc[0]
        return np.nan  # or any default value you prefer

    non_na_series = df.apply(find_non_na, axis=1)
    return non_na_series


