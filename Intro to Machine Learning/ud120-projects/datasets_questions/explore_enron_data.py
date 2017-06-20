#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print "Number of people in the dataset: %d" % len(enron_data)

# For each person, how many features are available?
print "Number of features for each person: %d" % len(enron_data["METTS MARK"])

# How many POIs are there in the E+F dataset?
count_poi = 0
for key in enron_data:
    if enron_data[key]["poi"]:
        count_poi += 1
print "Number of POIs in the dataset: %d" % count_poi

# What is the total value of the stock belonging to James Prentice?
print "The total value of the stock belonging to James Prentice: %d" % enron_data["PRENTICE JAMES"]["total_stock_value"]

# How many email messages do we have from Wesley Colwell to persons of interest?
print "Number of email messages from Wesley Colwell to POI: %d" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "The value of stock options exercised by Jeffrey K Skilling: %d" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# How many folks in this dataset have a quantified salary? What about a known email address?
count_quantified_salary = 0
count_email_address = 0
for key in enron_data:
    if enron_data[key]["salary"] != "NaN":
        count_quantified_salary += 1
    if enron_data[key]["email_address"] != "NaN":
        count_email_address += 1
print "Number of people who have a quantified salary: %d" % count_quantified_salary
print "Number of people who have a known email address: %d" % count_email_address
