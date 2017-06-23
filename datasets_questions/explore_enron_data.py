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

pois = 0
for person, attributes in enron_data.iteritems():
    if attributes['poi'] is True:
        pois += 1
print 'Persons of interest: {0}'.format(pois)

print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Skilling took {0}'.format(enron_data['SKILLING JEFFREY K']['total_payments'])
print 'Fastow took {0}'.format(enron_data['FASTOW ANDREW S']['total_payments'])
print 'Lay took {0}'.format(enron_data['LAY KENNETH L']['total_payments'])

quantified_salary = 0
for person, attributes in enron_data.iteritems():
    if attributes['salary'] != 'NaN':
        quantified_salary += 1
print 'Quantified salaries: {0}'.format(quantified_salary)

email_addresses = 0
for person, attributes in enron_data.iteritems():
    if attributes['email_address'] != 'NaN':
        email_addresses += 1
print 'Email addresses: {0}'.format(email_addresses)

total_payments_nan = 0
for person, attributes in enron_data.iteritems():
    if attributes['total_payments'] == 'NaN':
        total_payments_nan += 1
print 'Total payment NaNs: {0}'.format(total_payments_nan)

total_people = len(enron_data)
print 'Total people: {0}'.format(total_people)

nan_payments_perc = 21 * 100 / total_people
print 'Percentage of NaN payments: {0}'.format(nan_payments_perc)

total_payments_nan_poi = 0
for person, attributes in enron_data.iteritems():
    if attributes['total_payments'] == 'NaN' and attributes['poi'] is True:
        total_payments_nan_poi += 1
print 'Total payment NaNs POI: {0}'.format(total_payments_nan_poi)
