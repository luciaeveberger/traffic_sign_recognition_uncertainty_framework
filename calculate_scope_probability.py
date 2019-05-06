import time
import pandas as pd

import ScopeModelValidator

data_file_path = "test_dataset/data/generated_data1.csv"

if __name__ == '__main__':
    df = pd.read_csv(data_file_path)
    df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))
    df['Scope_Score'] = 0
    print("Actual size {}".format(len(df)))
    sample = df.head(50)
    count = 0
    scope_scores = list()
    for row in sample.itertuples():
        s = ScopeModelValidator.ScopeModelValidator(timestamp=row.Datetime,
                                month_stamp=row.month,
                                temperature=row.Temperature,
                                coordinates=row.Coordinates_Joined,
                                sign_type=row.ClassId,
                                road_type=row.RoadTypes,
                                velocity=row.Speed,
                                rain_sensor=4
                                )
        scope_scores.append(s.calculate_scope())
        count = count + 1

        if count % 25 == 0:
            ## sleep is added to not clog the api
            time.sleep(15)

    sample['Scope_Score'] = scope_scores
    sample.to_csv("dummy.csv")