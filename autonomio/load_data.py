import pandas as pd
from transform.col_name_generator import col_name_generator

url = 'https://github.com/autonomio/datasets/raw/master/autonomio-datasets/'
data_path = url


def load_data(name, mode, sep, delimiter, header):

    '''Data Loader

    WHAT: used for accessing datafiles that come with Autonomio, some unique
    and some common.
    '''

    try:

        if mode == 'default':

            if name == 'election_in_twitter':
                out = pd.read_msgpack(data_path+'election_in_twitter')
            if name == 'sites_category_and_vec':
                out = pd.read_msgpack(data_path+'sites_category_and_vec')
            if name == 'programmatic_ad_fraud':
                out = pd.read_msgpack(data_path+'programmatic_ad_fraud')
            if name == 'parties_and_employment':
                out = pd.read_msgpack(data_path+'parties_and_employment')
            if name == 'tweet_sentiment':
                out = pd.read_msgpack(data_path+'tweet_sentiment')
            if name == 'random_tweets':
                out = pd.read_msgpack(data_path+'random_tweets')
            if name == 'kaggle_titanic_train':
                out = pd.read_csv(data_path+'kaggle_titanic_train.csv')
            if name == 'bitcoin_price':
                out = pd.read_csv(data_path+'bitcoin_price.csv')

            return out

        elif mode == 'file':

            if name.endswith('.csv') or name.endswith('.txt'):

                try:
                    out = pd.read_csv(name, sep, delimiter, header)
                except ParserError:
                    out = pd.read_csv(name, sep, delimiter, header,
                                      error_bad_lines=False)

            elif name.endswith('.msgpack'):
                out = pd.read_msgpack(name)

            elif name.endswith('.json'):
                out = pd.read_json(name)

            else:

                out = ''
                print("MAYBE UNSUPPORTED? only csv/txt, json, and msgpack")

            # Convert number column names to alphabets

            if name.endswith('.csv') and header is None:
                out = col_name_generator(out)
            elif name.endswith('.csv') and header is None:
                out = col_name_generator(out)
            return out

    except UnboundLocalError:

        print("ERROR: you've probably tried to use 'name' which is wrong.")
        print("If you're trying to load from file, set mode to 'file' first.")
        print("USE: data('dataset_name') or data('filename.csv',mode='file')")

# Returns a Pandas dataframe
