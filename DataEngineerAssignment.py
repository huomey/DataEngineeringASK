#Cheap Crowdfunding Problem
def find_min_pledge(pledge_list):
    positive_pledges = sorted([pledge for pledge in pledge_list if pledge > 0])

    min_pledge = 1

    for pledge in positive_pledges:
        if pledge == min_pledge:
            min_pledge += 1
        elif pledge > min_pledge:
            break

    return min_pledge

assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1

#-----------------------------------------------------------------

#Extract Titles from RSS feed

import requests
import xml.etree.ElementTree as ET

def get_headlines(rss_url):

    url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

    for item in root.findall(".//item"):
            title = item.find('title').text
            print(title)
    return []

# Example usage
google_news_url = "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en"
print(get_headlines(google_news_url))

#-----------------------------------------------------------
# Streaming Payments Processor

import io
def get_payments_storage():
    return io.BytesIO()

def stream_payments_to_storage(storage):
    for i in range(10):
        storage.write(bytes([1, 2, 3, 4, 5]))
def process_payments():
    storage = get_payments_storage()
    stream_payments_to_storage(storage)
    storage.seek(0)
    data_written = storage.read()
    checksum = sum(data_written)
    print(checksum)

process_payments()

#-------------------------------------------------
# Streaming Payments Processor, two vendors edition.

import io

def stream_payments(callback_fn):
    for i in range(10):
        callback_fn(i)

def store_payments(amount_iterator):
    for i in amount_iterator:
        print(i)

def process_payments_2():

    def payment_generator():

        def callback_fn(amount):
            yield amount
        return callback_fn

    gen = payment_generator()
    store_payments(gen())

process_payments_2()


#------------------------------------------------

# Code Review

def get_value(data, key, default, lookup=None, mapper=None):
    return_value =  data.get(key, default) #to avoid key errors
    if return_value is None or return_value == "":
        return_value = default
    if lookup is not None: #specifying the value
        return_value = lookup.get(return_value, default)  #we can modify the lookup according to previous change
    if mapper is not None: #specifying the value
        return_value = mapper(return_value)

    return return_value

--------------------------------------------------------------------------
def ftp_file_prefix(namespace):
    # we can check if the namespace is empty
    if not namespace:
        return 'ftp'
    return ".".join(namespace.split(".")[:-1]) + '.ftp'

---------------------------------------------------------------------------
def string_to_bool(string):
    # we can Convert the string to lowercase for case-insensitive comparison
    lower_string = string.lower()
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
raise ValueError(f'String {string} is neither true nor false')

--------------------------------------------------------------------------------

def config_from_dict(text):  #we can avoid using dict, I have reamed it

    namespace = text.get('Namespace', '') #extracting namespace from text
    return (

        text.get(['Airflow DAG'],{"earliest_available_delta_days": 0, "lif_encoding": 'json',"earliest_available_time":
        get_value(dict, 'Available Start Time', '07:00'),"latest_available_time":
        get_value(dict, 'Available End Time', '08:00'),"require_schema_match":
        get_value(dict, 'Requires Schema Match', 'True',mapper=string_to_bool),"schedule_interval":
        get_value(dict, 'Schedule', '1 7 * * * '),"delta_days":
        get_value(dict, 'Delta Days', 'DAY_BEFORE',lookup=DeltaDays),"ftp_file_wildcard":
        get_value(dict, 'File Naming Pattern', None),"ftp_file_prefix":
        get_value(dict, 'FTP File Prefix',ftp_file_prefix(namespace)),"namespace": namespace
}
)