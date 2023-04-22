import pandas as pd
import datetime


class Solution:

    def __init__(self, data_loc):
        self.data_loc = data_loc

    def execute(self):
        initial_dataset = pd.read_csv(self.data_loc)
        dataset = initial_dataset.copy(deep=True)

        dataset['timestamp'] = pd.to_datetime(dataset['to_timestamp'])
        dataset = dataset.sort_values(['user_id', 'timestamp'], ascending=[True, True])
        dataset.reset_index(inplace=True)

        dataset['timestamp_prev'] = dataset['timestamp'].shift(1)
        dataset['user_prev'] = dataset['user_id'].shift(1)
        dataset['medium_prev'] = dataset['medium'].shift(1).fillna('Undefined')
        dataset['medium'] = dataset['medium'].fillna('Undefined')

        dataset['is_purchase'] = dataset['event_name'] == 'purchase'
        dataset['is_new_medium'] = dataset['medium'] != dataset['medium_prev']
        dataset['is_new_user'] = dataset['user_id'] != dataset['user_prev']
        dataset['over_2_hours'] = (dataset['timestamp'] - dataset['timestamp_prev']) > datetime.timedelta(hours=2)

        check_for_new_session = lambda row: True if any([row['is_purchase'],
                                            row['is_new_medium'],
                                            row['is_new_user'],
                                            row['over_2_hours']]) else False

        dataset['new_session'] = dataset.apply(check_for_new_session, axis=1)

        def new_session_calculator(df: pd.DataFrame):

            def eval_row_session(row: pd.Series):
                # non local variable ==> will use pre_value from the new_fun function
                nonlocal prev_value
                new_value = prev_value + 1 if row['new_session'] is True else prev_value
                row['session_num'] = new_value
                prev_value = row['session_num']
                return new_value

            # This line might throw a SettingWithCopyWarning warning
            df['session_num'] = None
            df.loc[0, "session_num"] = 0
            prev_value = df.loc[0, "session_num"]
            df["session_num"] = df.apply(eval_row_session, axis=1)
            return df

        dataset = new_session_calculator(df=dataset)
        return dataset
