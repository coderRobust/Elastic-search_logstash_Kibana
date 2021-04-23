import logging
import logstash
#from logstash import
import sys

host = 'localhost'
#import pdb; pdb.set_trace()
test_logger = logging.getLogger('python-logstash-logger')
#test_logger= logging.basicConfig(filename='example.log',level=logging.DEBUG)
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 9600, version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))
#test_logger = logging.FileHandler('python_logging.log')
#test_logger.setLevel(logging.DEBUG)


# add extra field to logstash message
#extra = {
#    'test_string': 'python version: ' + repr(sys.version_info),
#    'test_boolean': True,
#    'test_dict': {'a': 1, 'b': 'c'},
#    'test_float': 1.23,
#   'test_integer': 123,
#   'test_list': [1, 2, '3'],
#

data1 = {'time': 'Feb 18 05:46:52',
        'data' :{'last_name': u'DFGHJ', 'full_site_code': u'LBLBNCZ', 'postal_code': u'WEQFE', 'number_of_deposits': 1, 'original_account_id': 3402006, 'city': u'EWFG', 'subscribed': 1, 'site_code': u'LB', 'mobile_activated': False, 'date_of_birth': 886723200, 'username': u'test100', 'account_id': 3402006, 'chat_enabled': True, 'last_wager_time': 1550468063, 'registration_time': 1524580129, 'first_deposit_time': 1524580185, 'notes': None, 'gender': u'male', 'country': u'GB', 'buddy_account_id': None, 'mobile_verified': False, 'total_payouts': {u'Cash_GBP': 0.0}, 'locale': 'en_US', 'depositor': True, 'currency': u'GBP', 'email_activated': False, 'is_acquired': True, 'first_name': u'sdfghF', 'in_house': False, 'state': None, 'last_login': 1550466333, 'email': u'TEST100@VFEF.COM', 'status': 1, 'last_deposit_time': 1524580185, 'last_withdrawal_time': None, 'tracker_id': None, 'total_deposits': {u'Cash_GBP': 5.0}, 'address': u'WREFWF', 'properties': {u'gdpr_properties_updated_at': u'popup', u'optin_ed_sheeran': True, u'receive_text': True, u'auto_username': False, u'receive_telemarketing': True, u'account_activated': True, u'mobile_activated': False, u'adventure_4_2_val': 255.05, u'opted_vip_1kcashtourney': True, u'adventure_4_3_val': 5102.100000000001, u'adventure_4_2': True, u'receive_call': True, u'nationality': u'GB', u'receive_email': True, u'adventure_4_1': True, u'adventure_4_3': True, u'accepted_landmarkbingo_terms': True, u'opted_first_deposit_bonus': False, u'optin_spinner_promotion': True, u'mobile': u'12345745', u'optin_vikasfirstfinaltest_optin': True, u'vikasfirstfinaltest_optin': True, u'optin_weekend_promotion': True, u'gdpr_popup_shown': True}, 'bonus_enabled': True, 'number_of_payouts': 0, 'mobile': u'12345745', 'email_verified': False}}
data2 = {'time':'Feb 18 05:46:08',
         'data':{'last_name': u'DFGHJ', 'full_site_code': u'LBLBNCZ', 'postal_code': u'WEQFE', 'number_of_deposits': 1, 'original_account_id': None, 'city': u'EWFG', 'subscribed': 1, 'site_code': u'LB', 'mobile_activated': False, 'date_of_birth': 886723200, 'username': u'test100', 'account_id': 3402006, 'chat_enabled': True, 'last_wager_time': 1550468063, 'registration_time': 1524580129, 'first_deposit_time': 1524580185, 'notes': None, 'gender': u'male', 'country': u'GB', 'buddy_account_id': None, 'mobile_verified': False, 'total_payouts': {u'Cash_GBP': 0.0}, 'locale': 'en_US', 'depositor': True, 'currency': u'GBP', 'email_activated': False, 'is_acquired': True, 'first_name': u'sdfghF', 'in_house': False, 'state': None, 'last_login': 1550466333, 'email': u'TEST100@VFEF.COM', 'status': 1, 'last_deposit_time': 1524580185, 'last_withdrawal_time': None, 'tracker_id': None, 'total_deposits': {u'Cash_GBP': 5.0}, 'address': u'WREFWF', 'properties': {u'gdpr_properties_updated_at': u'popup', u'optin_ed_sheeran': True, u'receive_text': True, u'auto_username': False, u'receive_telemarketing': True, u'account_activated': True, u'mobile_activated': False, u'adventure_4_2_val': 255.05, u'opted_vip_1kcashtourney': True, u'adventure_4_3_val': 5102.100000000001, u'adventure_4_2': True, u'receive_call': True, u'nationality': u'GB', u'receive_email': True, u'adventure_4_1': True, u'adventure_4_3': True, u'accepted_landmarkbingo_terms': True, u'opted_first_deposit_bonus': False, u'optin_spinner_promotion': True, u'mobile': u'12345745', u'optin_vikasfirstfinaltest_optin': True, u'vikasfirstfinaltest_optin': True, u'optin_weekend_promotion': True, u'gdpr_popup_shown': True}, 'bonus_enabled': True, 'number_of_payouts': 0, 'mobile': u'12345745', 'email_verified': False}}
test_logger.info('registration data', extra=data1)
test_logger.info('registration_data', extra=data2)
print('done')