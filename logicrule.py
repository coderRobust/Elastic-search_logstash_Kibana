   {'title': 'CHB : Welcome mail',
     'id': 'fc519a88-1b05-11e5-aced-1380e75b9986',
     'event': 'registration',
     'statements': [
         {'actions': [Method('fetch_account_misc')]},
         {'condition': Condition('in',
                                 ['_site_code',
                                  ["'FOBBNCZ'", "'OFBBNCZ'", "'FFBBNCZ'"]]),
          'actions': [Method('stop_rule')]
          },
         {'actions': [
             Method('fetch_profile'),
             Method('set_value', {'value': '_profile["first_name"]'},
                    ['_first_name']),
             Method('fetch_site'),
             Method('fetch_affiliate_link_details'),
             Method('convert_currency_to_symbol',
                    {'currency': '_profile["currency"]'},
                    ['_currency_symbol']),
             Method('create_dictionary',
                    {'random': "'1E4E5FD654804000'",
                     'encrypt':
                     "'EdX7CqkmlzfM8SA9MOPu2N_WXUgPGdu3_D3Zc6kyWMDZKpY'",
                     'notification_id': '1705507'},
                    ['_message']),
             Method('nucleus.default.currency.scale_simple',
                    {'from_value': '20'},
                    ['_bonus_amount'])]
          },
         {'actions': [Method('get_network_code', {'account_id': 'account_id'},
                             ['_network_code'])]
          },
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"FBN"']),
             Condition('in', ['_site_code', ['"HBFBNCZ"', '"MHFBNCZ"']])]),
         'actions': [
              Method('create_dictionary',
                     {'random': "'3F47601654804003'",
                      'encrypt':
                      "'EdX7CqkmlzfL8SA9MOPu2N_UXkh9Gq3C_D3Zc6kyWMDaKuU'",
                      'notification_id': '1705508'},
                    ['_message'])]},
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"FBN"']),
             Condition('in', ['_site_code', ['"UBFBNCZ"', '"MUFBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'100006A84200A581'",
                      'encrypt':
                      "'EdX7CqkmlwSK8SA9MOPu2N_WKEx6HKuy8jzfe6lHXcjYK1k'",
                      'notification_id': '1717605'},
                     ['_message'])]},
         {'condition': Condition('=', ['_network_code', '"SBN"']),
          'actions': [
              Method('create_dictionary',
                     {'random': "'80001ED2402CA908'",
                      'encrypt':
                      "'EdX7CqkmlzfK8SA9MOPu2N_fKEx6Hdi3-DzdedpHUcDRKp4'",
                      'notification_id': '1717605'},
                     ['_message'])]},
         {'condition': Condition('=', ['_network_code', '"SBN"']),
          'actions': [
              Method('create_dictionary',
                     {'random': "'80001ED2402CA908'",
                      'encrypt':
                      "'EdX7CqkmlzfK8SA9MOPu2N_fKEx6Hdi3-DzdedpHUcDRKp4'",
                      'notification_id': '1705509'},
                    ['_message']),
              Method('nucleus.default.currency.scale_simple',
                     {'from_value': '15'},
                     ['_bonus_amount'])]},
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"SBN"']),
             Condition('in', ['_site_code', ['"HSSBNCZ"', '"HMSBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'2D02B2A402000018'",
                      'encrypt':
                      "'EdX7CqkmlzfJ8SA9MOPu2N_VXEx4bq-y_jjfe6k2WMHRKuA'",
                      'notification_id': '1705510'},
                     ['_message'])]},
         {'condition': Condition('=', ['_network_code', '"BBN"']),
          'actions': [
              Method('create_dictionary',
                     {'random': "'1491102B2A402001'",
                      'encrypt':
                      "'EdX7CqkmlzfI8SA9MOPu2N_WLEV7Ha3BiDqsf6k0WMDYKu0'",
                      'notification_id': '1705511'},
                     ['_message']),
              Method('nucleus.default.currency.scale_simple',
                     {'from_value': '15'},
                     ['_bonus_amount'])]
          },
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"BBN"']),
             Condition('in', ['_site_code', ['"SABBNCZ"', '"AMBBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'CFAC3D4B4020000E'",
                      'encrypt':
                      "'EdX7Cqkml39e8SA9MOPu2N-kXj0JH9nHiDzdeak2WMCsK4Q'",
                      'notification_id': '1724081'},
                     ['_message'])]},
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"BBN"']),
             Condition('in', ['_site_code', ['"GBBBNCZ"', '"MGBBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'A4020000E22F04B2'",
                      'encrypt':
                      "'EdX7CqkmlzfH8SA9MOPu2N-mLEx4HK3D-k3fed82XLLbKow'",
                      'notification_id': '1705512'},
                    ['_message'])]},
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"BBN"']),
             Condition('in', ['_site_code', ['"OBBBNCZ"', '"OMBBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'E5C010000AA87E53'",
                      'encrypt':
                      "'EdX7Cqkml2oG8SA9MOPu2N-iLT96Ha3D-jisCqExLcXaK7g'",
                      'notification_id': '1727465'},
                     ['_message'])]},
         {'condition': Condition('and', [
             Condition('=', ['_network_code', '"BBN"']),
             Condition('in', ['_site_code', ['"GOBBNCZ"']])]),
          'actions': [
              Method('create_dictionary',
                     {'random': "'30B93ED5C040030B'",
                      'encrypt':
                      "'EdX7CqkmlwV_8SA9MOPu2N_UKD5zH9i3_0vdf6k2W8CrKzk'",
                     'notification_id': '1717392'},
                     ['_message'])]},
         {'actions': [
             Method('create_dictionary',
                    {'account_id': 'account_id',
                     'username': 'username',
                     'first_name': '_first_name',
                     'site_name': '_site["site_name"]',
                     'site_url': '_site["site_url"]',
                     'site_code': '_site_code',
                     'full_site_code': '_site["site_code"]',
                     'bonus_currency': '_profile["currency"]',
                     'currency_symbol': '_currency_symbol',
                     'bonus_amount': '_bonus_amount',
                     'locale': '_profile["locale"]',
                     'link_name': '_link_name'},
                    ['_tokens']),
             Method('nucleus.mail.send',
                    {'backend': "'emailvision'",
                     'to_address': 'email',
                     'message': '_message',
                     'tokens': '_tokens'})]
          }]
     },
