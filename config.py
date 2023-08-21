import os

path = os.getcwd()
dir_path = "{}/templates/flags".format(path)
field_types = {0: 'text', 1: 'facial_image', 2: 'mrz', 3: 'signature'}

fields = {
    0: 'name',
    1: 'surname',
    2: 'nationality',
    3: 'birth_date',
    4: 'expiry_date',
    5: 'sex',
    6: 'document_type',
    7: 'document_number',
    8: 'optional_data'
}
id_types = {
    792: {
        'country': 'Turkey',
        'alpha': 'TUR',
        'flag': f'{dir_path}/Turkey.png',
        'card_types': {
            'id': {
                'extended_name': 'Republic of Turkey Identity Card',
                'front_side': True,
                'back_side': True,
                'mrz': True,
                'config_front': '792_id_front',
                'config_back': '792_id_back'
            },
            'passport': {
                'extended_name': 'Republic of Turkey Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '792_passport_front',
            },
            'driving_licence': {
                'extended_name': 'Republic of Turkey Driving Licence Card',
                'front_side': True,
                'back_side': True,
                'mrz': False,
                'config_front': '792_driving_licence_front',
                'config_back': '792_driving_licence_back'
            }
        }
    },
    31: {
        'country': 'Azerbaijan',
        'alpha': 'AZE',
        'flag': f'{dir_path}/Azerbaijan.png',
        'card_types': {
            'id': {
                'extended_name': 'Azerbaijan Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '31_id_front',
            },
            'passport': {
                'extended_name': 'Azerbaijan Passport Card',
                'front': True,
                'back_side': False,
                'mrz': False,
                'config_front': '31_passport_front',
            }
        }
    },
    250: {
        'country': 'France',
        'alpha': 'FRA',
        'flag': f'{dir_path}/France.png',
        'card_types': {
            'id': {
                'extended_name': 'France Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '250_id_front',
            }
        }
    },
    276: {
        'country': 'Germany',
        'alpha': 'DEU',
        'flag': f'{dir_path}/Germany.png',
        'card_types': {
            'id': {
                'extended_name': 'Germany Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '276_id_front',
            },
            'passport': {
                'extended_name': 'Germany Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '276_passport_front',
            }
        }
    },
    40: {
        'country': 'Austria',
        'alpha': 'AUT',
        'flag': f'{dir_path}/Austria.png',
        'card_types': {
            'id': {
                'extended_name': 'Austria Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '40_id_front',
            }
        }
    },
    56: {
        'country': 'Belgium',
        'alpha': 'BEL',
        'flag': f'{dir_path}/Belgium.png',
        'card_types': {
            'id': {
                'extended_name': 'Belgium Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '56_id_front',
            }
        }
    },
    100: {
        'country': 'Bulgaria',
        'alpha': 'BGR',
        'flag': f'{dir_path}/Bulgaria.png',
        'card_types': {
            'id': {
                'extended_name': 'Bulgaria Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '100_id_front',
            }
        }
    },
    191: {
        'country': 'Croatia',
        'alpha': 'HRV',
        'flag': f'{dir_path}/Croatia.png',
        'card_types': {
            'id': {
                'extended_name': 'Croatia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '191_id_front',
            }
        }
    },
    233: {
        'country': 'Estonia',
        'alpha': 'EST',
        'flag': f'{dir_path}/Estonia.png',
        'card_types': {
            'id': {
                'extended_name': 'Estonia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '233_id_front',
            }
        }
    },
    348: {
        'country': 'Hungary',
        'alpha': 'HUN',
        'flag': f'{dir_path}/Hungary.png',
        'card_types': {
            'id': {
                'extended_name': 'Hungary Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '348_id_front',
            },
        }
    },
    438: {
        'country': 'Liechtenstein',
        'alpha': 'LIE',
        'flag': f'{dir_path}/Liechtenstein.png',
        'card_types': {
            'id': {
                'extended_name': 'Liechtenstein Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '438_id_front',
            }
        }
    },
    616: {
        'country': 'Poland',
        'alpha': 'POL',
        'flag': f'{dir_path}/Poland.png',
        'card_types': {
            'id': {
                'extended_name': 'Poland Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '616_id_front',
            }
        }
    },
    620: {
        'country': 'Portugal',
        'alpha': 'PRT',
        'flag': f'{dir_path}/Portugal.png',
        'card_types': {
            'id': {
                'extended_name': 'Portugal Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '620_id_front',
            }
        }
    },
    642: {
        'country': 'Romania',
        'alpha': 'ROU',
        'flag': f'{dir_path}/Romania.png',
        'card_types': {
            'id': {
                'extended_name': 'Romania Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '642_id_front',
            },
            'driving_licence': {
                'extended_name': 'Romania Driving Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '642_driving_licence_front',
            }
        }
    },
    703: {
        'country': 'Slovakia',
        'alpha': 'SVK',
        'flag': f'{dir_path}/Slovakia.png',
        'card_types': {
            'id': {
                'extended_name': 'Slovakia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '703_id_front',
            }
        }
    },
    724: {
        'country': 'Spain',
        'alpha': 'ESP',
        'flag': f'{dir_path}/Spain.png',
        'card_types': {
            'id': {
                'extended_name': 'Spain Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '724_id_front',
            }
        }
    },
    578: {
        'country': 'Norway',
        'alpha': 'NOR',
        'flag': f'{dir_path}/Norway.png',
        'card_types': {
            'id': {
                'extended_name': 'Norway Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '578_id_front',
            }
        }
    },
    470: {
        'country': 'Malta',
        'alpha': 'MLT',
        'flag': f'{dir_path}/Malta.png',
        'card_types': {
            'id': {
                'extended_name': 'Malta Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '470_id_front',
            }
        }
    },
    380: {
        'country': 'Italy',
        'alpha': 'ITA',
        'flag': f'{dir_path}/Italy.png',
        'card_types': {
            'id': {
                'extended_name': 'Italy Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '380_id_front',
            }
        }
    },
    246: {
        'country': 'Finland',
        'alpha': 'FIN',
        'flag': f'{dir_path}/Finland.png',
        'card_types': {
            'id': {
                'extended_name': 'Finland Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '246_id_front',
            }
        }
    },
    203: {
        'country': 'Czech Republic',
        'alpha': 'CZE',
        'flag': f'{dir_path}/CzechRepublic.png',
        'card_types': {
            'id': {
                'extended_name': 'Czech Republic Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '203_id_front',
            }
        }
    },
    440: {
        'country': 'Lithuania',
        'alpha': 'LTU',
        'flag': f'{dir_path}/Lithuania.png',
        'card_types': {
            'id': {
                'extended_name': 'Lithuania Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '440_id_front',
            }
        }
    },
    428: {
        'country': 'Latvia',
        'alpha': 'LVA',
        'flag': f'{dir_path}/Latvia.png',
        'card_types': {
            'id': {
                'extended_name': 'Latvia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '428_id_front',
            }
        }
    },
    804: {
        'country': 'Ukraine',
        'alpha': 'UKR',
        'flag': f'{dir_path}/Ukraine.png',
        'card_types': {
            'id': {
                'extended_name': 'Ukraine Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '804_id_front',
            }
        }
    },
    826: {
        'country': 'United Kingdom',
        'alpha': 'GBR',
        'flag': f'{dir_path}/UnitedKingdom.png',
        'card_types': {
            'id': {
                'extended_name': 'United Kingdom Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '826_id_front',
            },
            'passport': {
                'extended_name': 'United Kingdom Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '826_passport_front',
            }
        }
    },
    784: {
        'country': 'United Arab Emirates',
        'alpha': 'ARE',
        'flag': f'{dir_path}/UnitedArabEmirates.png',
        'card_types': {
            'id': {
                'extended_name': 'United Arab Emirates Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '784_id_front',
            }
        }
    },
    756: {
        'country': 'Switzerland',
        'alpha': 'CHE',
        'flag': f'{dir_path}/Switzerland.png',
        'card_types': {
            'id': {
                'extended_name': 'Switzerland Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '756_id_front',
            }
        }
    },
    710: {
        'country': 'South Africa',
        'alpha': 'ZAF',
        'flag': f'{dir_path}/SouthAfrica.png',
        'card_types': {
            'id': {
                'extended_name': 'South Africa Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '710_id_front',
            }
        }
    },
    705: {
        'country': 'Slovenia',
        'alpha': 'SVN',
        'flag': f'{dir_path}/Slovenia.png',
        'card_types': {
            'id': {
                'extended_name': 'Slovenia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '705_id_front',
            }
        }
    },
    528: {
        'country': 'Netherlands',
        'alpha': 'NLD',
        'flag': f'{dir_path}/Netherlands.png',
        'card_types': {
            'id': {
                'extended_name': 'Netherlands Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '528_id_front',
            },
            'passport': {
                'extended_name': 'Netherlands Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '528_passport_front',
            }
        }
    },
    442: {
        'country': 'Luxembourg',
        'alpha': 'LUX',
        'flag': f'{dir_path}/Luxembourg.png',
        'card_types': {
            'id': {
                'extended_name': 'Luxembourg Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '442_id_front',
            }
        }
    },
    417: {
        'country': 'Kyrgyzstan',
        'alpha': 'KGZ',
        'flag': f'{dir_path}/Kyrgyzstan.png',
        'card_types': {
            'id': {
                'extended_name': 'Kyrgyzstan Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '417_id_front',
            }
        }
    },
    268: {
        'country': 'Georgia',
        'alpha': 'GEO',
        'flag': f'{dir_path}/Georgia.png',
        'card_types': {
            'id': {
                'extended_name': 'Georgia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '268_id_front',
            }
        }
    },
    8: {
        'country': 'Albania',
        'alpha': 'ALB',
        'flag': f'{dir_path}/Albania.png',
        'card_types': {
            'id': {
                'extended_name': 'Albania Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '8_id_front',
            }
        }
    },
    752: {
        'country': 'Sweden',
        'alpha': 'SWE',
        'flag': f'{dir_path}/Sweden.png',
        'card_types': {
            'id': {
                'extended_name': 'Sweden Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '752_id_front',
            }
        }
    },
    840: {
        'country': 'United States of America',
        'alpha': 'USA',
        'flag': f'{dir_path}/UnitedStates.png',
        'card_types': {
            'passport': {
                'extended_name': 'United States of America Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '840_passport_front',
            }
        }
    },
    586: {
        'country': 'Pakistan',
        'alpha': 'PAK',
        'flag': f'{dir_path}/Pakistan.png',
        'card_types': {
            'nic_id': {
                'extended_name': 'National Identity Card Pakistan',
                'front_side': True,
                'back_side': True,
                'mrz': True,
                'config_front': '586_nic_id_front',
                'config_back': '586_nic_id_back'
            },
            'nicop_id': {
                'extended_name': 'National Identity Card for Overseas Pakistan Card',
                'front_side': True,
                'back_side': True,
                'mrz': True,
                'config_front': '586_nicop_id_front',
                'config_back': '586_nicop_id_back'
            }
        }
    },
    414: {
        'country': 'Kuwait',
        'alpha': 'KWT',
        'flag': f'{dir_path}/Kuwait.png',
        'card_types': {
            'id': {
                'extended_name': 'Kuwait Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '414_id_front',
            }
        }
    },
    196: {
        'country': 'Cyprus',
        'alpha': 'CYP',
        'flag': f'{dir_path}/Cyprus.png',
        'card_types': {
            'id': {
                'extended_name': 'Cyprus Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '196_id_front',
            }
        }
    },
    498: {
        'country': 'Moldova',
        'alpha': 'MDA',
        'flag': f'{dir_path}/Moldova.png',
        'card_types': {
            'id': {
                'extended_name': 'Moldova Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '498_id_front',
            }
        }
    },
    458: {
        'country': 'Malaysia',
        'alpha': 'MYS',
        'flag': f'{dir_path}/Malaysia.png',
        'card_types': {
            'id': {
                'extended_name': 'Malaysia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '458_id_front',
            },
            'passport': {
                'extended_name': 'Malaysia Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '458_passport_front',
            }
        }
    },
    524: {
        'country': 'Nepal',
        'alpha': 'NPL',
        'flag': f'{dir_path}/Nepal.png',
        'card_types': {
            'id': {
                'extended_name': 'Nepal Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '524_id_front',
            }
        }
    },
    70: {
        'country': 'Bosnia and Herzegovina',
        'alpha': 'BIH',
        'flag': f'{dir_path}/BosniaandHerzegovina.png',
        'card_types': {
            'id': {
                'extended_name': 'Bosnia and Herzegovina Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '70_id_front',
            }
        }
    },
    674: {
        'country': 'San Marino',
        'alpha': 'SMR',
        'flag': f'{dir_path}/SanMarino.png',
        'card_types': {
            'id': {
                'extended_name': 'San Marino Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '674_id_front',
            }
        }
    },
    608: {
        'country': 'Philippines',
        'alpha': 'PHL',
        'flag': f'{dir_path}/Philippines.png',
        'card_types': {
            'id': {
                'extended_name': 'Philippines Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '608_id_front',
            },
            'passport': {
                'extended_name': 'Philippines Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '608_passport_front',
            }
        }
    },
    702: {
        'country': 'Singapore',
        'alpha': 'SGP',
        'flag': f'{dir_path}/Singapore.png',
        'card_types': {
            'id': {
                'extended_name': 'Singapore Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '702_id_front',
            }
        }
    },
    688: {
        'country': 'Serbia',
        'alpha': 'SRB',
        'flag': f'{dir_path}/Serbia.png',
        'card_types': {
            'id': {
                'extended_name': 'Serbia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '688_id_front',
            }
        }
    },
    356: {
        'country': 'India',
        'alpha': 'IND',
        'flag': f'{dir_path}/India.png',
        'card_types': {
            'id': {
                'extended_name': 'India Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '356_id_front',
            }
        }
    },
    372: {
        'country': 'Ireland',
        'alpha': 'IRL',
        'flag': f'{dir_path}/Ireland.png',
        'card_types': {
            'id': {
                'extended_name': 'Ireland Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '372_id_front',
            }
        }
    },
    32: {
        'country': 'Argentina',
        'alpha': 'ARG',
        'flag': f'{dir_path}/Argentina.png',
        'card_types': {
            'id': {
                'extended_name': 'Argentina Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '32_id_front',
            }
        }
    },
    344: {
        'country': 'Hong Kong',
        'alpha': 'HKG',
        'flag': f'{dir_path}/HongKong.png',
        'card_types': {
            'id': {
                'extended_name': 'Hong Kong Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '344_id_front',
            }
        }
    },
    51: {
        'country': 'Armenia',
        'alpha': 'ARM',
        'flag': f'{dir_path}/Armenia.png',
        'card_types': {
            'id': {
                'extended_name': 'Armenia Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '51_id_front',
            }
        }
    },
    364: {
        'country': 'Iran',
        'alpha': 'IRN',
        'flag': f'{dir_path}/Iran.png',
        'card_types': {
            'passport': {
                'extended_name': 'Iran Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '364_passport_front',
            }
        }
    },
    214: {
        'country': 'Dominican Republic',
        'alpha': 'DOM',
        'flag': f'{dir_path}/DominicanRepublic.png',
        'card_types': {
            'id': {
                'extended_name': 'Dominican Republic Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '214_id_front',
            }
        }
    },
    124: {
        'country': 'Canada',
        'alpha': 'CAN',
        'flag': f'{dir_path}/Canada.png',
        'card_types': {
            'id': {
                'extended_name': 'Canada Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '124_id_front',
            },
            'passport': {
                'extended_name': 'Canada Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '124_passport_front',
            }
        }
    },
    76: {
        'country': 'Brazil',
        'alpha': 'BRA',
        'flag': f'{dir_path}/Brazil.png',
        'card_types': {
            'id': {
                'extended_name': 'Brazil Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '76_id_front',
            },
            'passport': {
                'extended_name': 'Brazil Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '76_passport_front'
            }
        }
    },
    112: {
        'country': 'Belarus',
        'alpha': 'BLR',
        'flag': f'{dir_path}/Belarus.png',
        'card_types': {
            'id': {
                'extended_name': 'Belarus Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '112_id_front',
            }
        }
    },
    152: {
        'country': 'Chile',
        'alpha': 'CHL',
        'flag': f'{dir_path}/Chile.png',
        'card_types': {
            'id': {
                'extended_name': 'Chile Identity Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '152_id_front',
            }
        }
    },
    368: {
        'country': 'Iraq',
        'alpha': 'IRQ',
        'flag': f'{dir_path}/Iraq.png',
        'card_types': {
            'passport': {
                'extended_name': 'Iraq Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '368_passport_front',
            }
        }
    },
    496: {
        'country': 'Mongolia',
        'alpha': 'MNG',
        'flag': f'{dir_path}/Mongolia.png',
        'card_types': {
            'passport': {
                'extended_name': 'Mongolia Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '496_passport_front',
            }
        }
    },
    275: {
        'country': 'Palestine',
        'alpha': 'PSE',
        'flag': f'{dir_path}/Palestine.png',
        'card_types': {
            'driving_licence': {
                'extended_name': 'Palestine Driving Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '275_driving_licence_front',
            }
        }
    },
    598: {
        'country': 'Papua_New_Guinea',
        'alpha': 'PSE',
        'flag': f'{dir_path}/Papua_New_Guinea.png',
        'card_types': {
            'driving_licence': {
                'extended_name': 'Papua Driving Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '598_driving_licence_front',
            }
        }
    },
    704: {
        'country': 'Vietnam',
        'alpha': 'VNM',
        'flag': f'{dir_path}/Vietnam.png',
        'card_types': {
            'passport': {
                'extended_name': 'Vietnam Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '704_passport_front',
            }
        }
    },
    36: {
        'country': 'Australia',
        'alpha': 'AUS',
        'flag': f'{dir_path}/Australia.png',
        'card_types': {
            'driving_licence': {
                'extended_name': 'Australia Driving Card',
                'front_side': True,
                'back_side': False,
                'mrz': False,
                'config_front': '36_driving_licence_front',
            }
        }
    },
    504: {
        'country': 'Morocco',
        'alpha': 'MAR',
        'flag': f'{dir_path}/Morocco.png',
        'card_types': {
            'passport': {
                'extended_name': 'Morocco Passport Card',
                'front_side': True,
                'back_side': False,
                'mrz': True,
                'config_front': '504_passport_front',
            }
        }
    },
}
config_android = {
    "792_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 853,
                  "w": 1329
            },
            "ref": {
                  "x": 350,
                  "y": 119,
                  "h": 54,
                  "w": 375
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 72,
                              "y": 287,
                              "h": 449,
                              "w": 375
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 81,
                              "y": 222,
                              "h": 73,
                              "w": 380
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 450,
                              "y": 428,
                              "h": 70,
                              "w": 588
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 338,
                              "h": 75,
                              "w": 387
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 510,
                              "h": 75,
                              "w": 260
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 600,
                              "h": 70,
                              "w": 260
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 680,
                              "h": 80,
                              "w": 260
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 785,
                              "y": 518,
                              "h": 66,
                              "w": 223
                        },
                        "ocr_type": 1, "regex": "[EK]\\/[MF]"
                  }
            }
      },
    "792_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 857,
                  "w": 1398
            },
            "ref": {
                  "x": 406,
                  "y": 269,
                  "h": 46,
                  "w": 351
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "mother_name",
                        "type": 0,
                        "points": {
                              "x": 371,
                              "y": 204,
                              "h": 69,
                              "w": 580
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "1": {
                        "name": "father_name",
                        "type": 0,
                        "points": {
                              "x": 371,
                              "y": 300,
                              "h": 69,
                              "w": 580
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "2": {
                        "name": "mrz",
                        "mrz_type": "td1",
                        "type": 2,
                        "points": {
                              "x": 72,
                              "y": 509,
                              "h": 321,
                              "w": 1289
                        },
                        "check_mrz": True
                  }
            }
      },
    "792_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 768,
                  "w": 1024
            },
            "ref": {
                  "x": 88,
                  "y": 82,
                  "h": 115,
                  "w": 192
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 44,
                              "y": 212,
                              "h": 329,
                              "w": 265
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 715,
                              "y": 330,
                              "h": 42,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 195,
                              "h": 35,
                              "w": 285
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 160,
                              "h": 35,
                              "w": 285
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 310,
                              "y": 400,
                              "h": 50,
                              "w": 180
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 705,
                              "y": 130,
                              "h": 40,
                              "w": 170
                        },
                        "ocr_type": 1, "regex": "([0-9A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 320,
                              "y": 505,
                              "h": 45,
                              "w": 185
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 720,
                              "y": 268,
                              "h": 28,
                              "w": 80
                        },
                        "ocr_type": 1, "regex": "[EK]\\/[MF]"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 655,
                              "y": 450,
                              "h": 100,
                              "w": 220
                        }
                  },
                  "9": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 45,
                              "y": 555,
                              "h": 140,
                              "w": 910
                        },
                        "check_mrz": True
                  }
            }
      },
    "792_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1134,
                  "w": 2016
            },
            "ref": {
                  "x": 1095,
                  "y": 99,
                  "h": 167,
                  "w": 439
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 261,
                              "y": 277,
                              "h": 599,
                              "w": 489
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 1349,
                              "y": 580,
                              "h": 90,
                              "w": 379
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 839,
                              "y": 349,
                              "h": 83,
                              "w": 645
                        },
                        "ocr_type": 0, "regex": "([A-Za-zĞÇŞÜÖİğçşüöı]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 837,
                              "y": 269,
                              "h": 89,
                              "w": 563
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 840,
                              "y": 433,
                              "h": 77,
                              "w": 330
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 840,
                              "y": 580,
                              "h": 100,
                              "w": 330
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "licence_number",
                        "type": 0,
                        "points": {
                              "x": 845,
                              "y": 650,
                              "h": 110,
                              "w": 279
                        },
                        "ocr_type": 1, "regex": "([0-9]){1,}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 857,
                              "y": 751,
                              "h": 165,
                              "w": 507
                        }
                  },
                  "8": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 330,
                              "y": 850,
                              "h": 79,
                              "w": 650
                        }
                  }
            }
      },
    "792_driving_licence_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 813,
                  "w": 1280
            },
            "ref": {
                  "x": 294,
                  "y": 69,
                  "h": 465,
                  "w": 104
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "blood_type",
                        "type": 3,
                        "points": {
                              "x": 90,
                              "y": 30,
                              "h": 85,
                              "w": 173
                        }
                  },
                  "1": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 291,
                              "y": 27,
                              "h": 749,
                              "w": 824
                        }
                  }
            }
      },
    "31_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1085,
                  "w": 1675
            },
            "ref": {
                  "x": 330,
                  "y": 49,
                  "h": 59,
                  "w": 281
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 77,
                              "y": 155,
                              "h": 621,
                              "w": 509
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 1080,
                              "y": 725,
                              "h": 102,
                              "w": 269
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]+\\s?){7}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 589,
                              "y": 352,
                              "h": 79,
                              "w": 681
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 599,
                              "y": 215,
                              "h": 91,
                              "w": 697
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 1195,
                              "y": 600,
                              "h": 90,
                              "w": 353
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 725,
                              "h": 97,
                              "w": 377
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]+\\s?){9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 599,
                              "y": 853,
                              "h": 115,
                              "w": 323
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 601,
                              "y": 595,
                              "h": 90,
                              "w": 147
                        },
                        "ocr_type": 1, "regex": "[QKMF/]{1,}"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 1077,
                              "y": 861,
                              "h": 160,
                              "w": 519
                        }
                  }
            }
      },
    "31_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 732,
                  "w": 1040
            },
            "ref": {
                  "x": 208,
                  "y": 64,
                  "h": 51,
                  "w": 95
            },
            "threshold": 0.76,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 50,
                              "y": 115,
                              "h": 317,
                              "w": 250
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 500,
                              "y": 342,
                              "h": 40,
                              "w": 200
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]+\\s?){7}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 245,
                              "h": 40,
                              "w": 238
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 132,
                              "h": 70,
                              "w": 249
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 311,
                              "y": 340,
                              "h": 40,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 660,
                              "y": 85,
                              "h": 35,
                              "w": 202
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]+\\s?){9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 435,
                              "h": 42,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 733,
                              "y": 342,
                              "h": 34,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": "[QKMF/]{1,}"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 737,
                              "y": 443,
                              "h": 100,
                              "w": 249
                        }
                  },
                  "9": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 40,
                              "y": 574,
                              "h": 118,
                              "w": 960
                        },
                        "check_mrz": True
                  }
            }
      },
    "250_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 652,
                  "w": 1024
            },
            "ref": {
                  "x": 62,
                  "y": 33,
                  "h": 113,
                  "w": 184
            },
            "threshold": 0.83,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 67,
                              "y": 143,
                              "h": 452,
                              "w": 325
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 400,
                              "y": 234,
                              "h": 37,
                              "w": 374
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "2": {
                        "name": "alternative_name",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 418,
                              "h": 41,
                              "w": 346
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 317,
                              "h": 31,
                              "w": 166
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 476,
                              "h": 42,
                              "w": 283
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 470,
                              "h": 27,
                              "w": 182
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 317,
                              "h": 38,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": "[FM][1]"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 446,
                              "y": 516,
                              "h": 81,
                              "w": 256
                        }
                  }
            }
      },
    "276_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 525,
                  "w": 834
            },
            "ref": {
                  "x": 31,
                  "y": 15,
                  "h": 79,
                  "w": 221
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 33,
                              "y": 105,
                              "h": 402,
                              "w": 314
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 364,
                              "y": 219,
                              "h": 35,
                              "w": 248
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 361,
                              "y": 136,
                              "h": 62,
                              "w": 319
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 293,
                              "h": 30,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 577,
                              "y": 20,
                              "h": 48,
                              "w": 228
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 409,
                              "h": 35,
                              "w": 168
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "nationality",
                        "type": 0,
                        "points": {
                              "x": 546,
                              "y": 289,
                              "h": 38,
                              "w": 226
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1,}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 354,
                              "y": 436,
                              "h": 78,
                              "w": 253
                        }
                  }
            }
      },
    "276_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 678,
                  "w": 958
            },
            "ref": {
                  "x": 341,
                  "y": 14,
                  "h": 30,
                  "w": 189
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 40,
                              "y": 111,
                              "h": 337,
                              "w": 261
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 332,
                              "y": 122,
                              "h": 20,
                              "w": 140
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 330,
                              "y": 148,
                              "h": 27,
                              "w": 155
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 323,
                              "y": 267,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "4": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 605,
                              "y": 72,
                              "h": 34,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{9}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 519,
                              "y": 273,
                              "h": 32,
                              "w": 58
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 524,
                              "y": 377,
                              "h": 38,
                              "w": 147
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 688,
                              "y": 392,
                              "h": 90,
                              "w": 255
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 14,
                              "y": 517,
                              "h": 121,
                              "w": 926
                        },
                        "ocr_type": 2,
                        "check_mrz": True
                  }
            }
      },
    "40_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 387,
                  "w": 619
            },
            "ref": {
                  "x": 368,
                  "y": 9,
                  "h": 57,
                  "w": 180
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 28,
                              "y": 93,
                              "h": 262,
                              "w": 193
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 114,
                              "h": 24,
                              "w": 204
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 242,
                              "y": 92,
                              "h": 24,
                              "w": 213
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 284,
                              "h": 28,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 241,
                              "y": 202,
                              "h": 23,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{9}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 247,
                              "h": 24,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 238,
                              "y": 322,
                              "h": 30,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 479,
                              "y": 275,
                              "h": 38,
                              "w": 132
                        }
                  }
            }
      },
    "56_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 466,
                  "w": 737
            },
            "ref": {
                  "x": 504,
                  "y": 5,
                  "h": 61,
                  "w": 136
            },
            "threshold": 0.81,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 25,
                              "y": 160,
                              "h": 286,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 18,
                              "y": 86,
                              "h": 25,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 20,
                              "y": 123,
                              "h": 26,
                              "w": 252
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 564,
                              "y": 191,
                              "h": 25,
                              "w": 122
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 289,
                              "h": 27,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": "[0-9.-]{1,}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 338,
                              "h": 29,
                              "w": 121
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 268,
                              "y": 190,
                              "h": 29,
                              "w": 54
                        },
                        "ocr_type": 1, "regex": "([WM]{1})[/]{1}([MF]{1})"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 330,
                              "y": 371,
                              "h": 81,
                              "w": 227
                        }
                  }
            }
      },
    "100_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 378,
                  "w": 598
            },
            "ref": {
                  "x": 366,
                  "y": 33,
                  "h": 38,
                  "w": 210
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 33,
                              "y": 94,
                              "h": 198,
                              "w": 151
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 318,
                              "y": 206,
                              "h": 24,
                              "w": 107
                        },
                        "ocr_type": 1, "regex": "[0-9]{10}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 279,
                              "y": 147,
                              "h": 21,
                              "w": 167
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 277,
                              "y": 105,
                              "h": 22,
                              "w": 186
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 250,
                              "h": 20,
                              "w": 90
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 446,
                              "y": 287,
                              "h": 28,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": "[0-9]{9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 368,
                              "y": 270,
                              "h": 18,
                              "w": 92
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 499,
                              "y": 207,
                              "h": 25,
                              "w": 39
                        },
                        "ocr_type": 1, "regex": "(.+\\s?){1,}"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 437,
                              "y": 319,
                              "h": 49,
                              "w": 139
                        }
                  }
            }
      },
    "191_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 379,
                  "w": 600
            },
            "ref": {
                  "x": 153,
                  "y": 31,
                  "h": 45,
                  "w": 175
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 23,
                              "y": 111,
                              "h": 252,
                              "w": 188
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 228,
                              "y": 258,
                              "h": 25,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": "[0-9]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 229,
                              "y": 147,
                              "h": 20,
                              "w": 171
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 229,
                              "y": 96,
                              "h": 28,
                              "w": 222
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 444,
                              "y": 205,
                              "h": 27,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 444,
                              "y": 255,
                              "h": 24,
                              "w": 132
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 228,
                              "y": 204,
                              "h": 28,
                              "w": 51
                        },
                        "ocr_type": 1, "regex": "(.+\\s?){1,}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 242,
                              "y": 306,
                              "h": 62,
                              "w": 165
                        }
                  }
            }
      },
    "233_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 603,
                  "w": 954
            },
            "ref": {
                  "x": 64,
                  "y": 56,
                  "h": 37,
                  "w": 237
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 65,
                              "y": 100,
                              "h": 391,
                              "w": 333
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 716,
                              "y": 351,
                              "h": 55,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": "[0-9]{12}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 166,
                              "h": 41,
                              "w": 223
                        },
                        "ocr_type": 0, "regex": "([A-Z-]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 118,
                              "h": 43,
                              "w": 269
                        },
                        "ocr_type": 0, "regex": "([A-Z-]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 713,
                              "y": 296,
                              "h": 43,
                              "w": 178
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 394,
                              "y": 401,
                              "h": 45,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 394,
                              "y": 350,
                              "h": 39,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 613,
                              "y": 246,
                              "h": 34,
                              "w": 60
                        },
                        "ocr_type": 1, "regex": "[MFN][/][MFN]"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 442,
                              "y": 510,
                              "h": 66,
                              "w": 182
                        }
                  }
            }
      },
    "348_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 648,
                  "w": 1022
            },
            "ref": {
                  "x": 902,
                  "y": 37,
                  "h": 165,
                  "w": 94
            },
            "threshold": 0.81,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 42,
                              "y": 143,
                              "h": 451,
                              "w": 329
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 426,
                              "y": 169,
                              "h": 45,
                              "w": 226
                        },
                        "ocr_type": 0, "regex": "([A-Z-]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 654,
                              "y": 171,
                              "h": 40,
                              "w": 213
                        },
                        "ocr_type": 0, "regex": "([A-Z-]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 780,
                              "y": 310,
                              "h": 36,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 806,
                              "y": 380,
                              "h": 47,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{8}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 777,
                              "y": 342,
                              "h": 40,
                              "w": 231
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 521,
                              "y": 274,
                              "h": 41,
                              "w": 64
                        },
                        "ocr_type": 1, "regex": "[NFM][/][NFM]"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 446,
                              "y": 532,
                              "h": 69,
                              "w": 296
                        }
                  }
            }
      },
    "368_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 751,
                  "w": 1105
            },
            "ref": {
                  "x": 18,
                  "y": 33,
                  "h": 42,
                  "w": 305
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 13,
                              "y": 158,
                              "h": 376,
                              "w": 291
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 314,
                              "y": 196,
                              "h": 41,
                              "w": 481
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 310,
                              "y": 249,
                              "h": 32,
                              "w": 261
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 561,
                              "y": 315,
                              "h": 36,
                              "w": 182
                        },
                        "ocr_type": 1, "regex": "[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 841,
                              "y": 135,
                              "h": 32,
                              "w": 218
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}[0-9]{8}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 303,
                              "y": 468,
                              "h": 37,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": "[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 307,
                              "y": 303,
                              "h": 52,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 10,
                              "y": 622,
                              "h": 103,
                              "w": 1073
                        },
                        "check_mrz": True
                  }
            }
      },
    "438_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 642,
                  "w": 1024
            },
            "ref": {
                  "x": 308,
                  "y": 105,
                  "h": 48,
                  "w": 319
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 80,
                              "y": 215,
                              "h": 342,
                              "w": 266
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 42,
                              "h": 44,
                              "w": 247
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 389,
                              "y": 420,
                              "h": 43,
                              "w": 326
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 390,
                              "y": 310,
                              "h": 41,
                              "w": 398
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 533,
                              "h": 48,
                              "w": 189
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 663,
                              "y": 496,
                              "h": 106,
                              "w": 332
                        }
                  }
            }
      },
    "616_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 646,
                  "w": 1024
            },
            "ref": {
                  "x": 172,
                  "y": 22,
                  "h": 45,
                  "w": 374
            },
            "threshold": 0.55,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 50,
                              "y": 182,
                              "h": 417,
                              "w": 289
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 232,
                              "h": 43,
                              "w": 302
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 153,
                              "h": 47,
                              "w": 338
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 307,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": "[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 395,
                              "h": 39,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{9}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 460,
                              "h": 35,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": "[0-9]{4}\\-[0-9]{1,2}\\-[0-9]{1,2}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 392,
                              "h": 34,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 373,
                              "y": 528,
                              "h": 83,
                              "w": 391
                        }
                  }
            }
      },
    "620_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 645,
                  "w": 946
            },
            "ref": {
                  "x": 572,
                  "y": 45,
                  "h": 84,
                  "w": 353
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 701,
                              "y": 294,
                              "h": 296,
                              "w": 207
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 284,
                              "y": 432,
                              "h": 43,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 264,
                              "y": 248,
                              "h": 44,
                              "w": 327
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 268,
                              "y": 157,
                              "h": 44,
                              "w": 411
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 345,
                              "h": 41,
                              "w": 139
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 422,
                              "h": 51,
                              "w": 76
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 435,
                              "h": 37,
                              "w": 138
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 260,
                              "y": 515,
                              "h": 74,
                              "w": 415
                        }
                  },
                  "8": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 262,
                              "y": 342,
                              "h": 40,
                              "w": 46
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "642_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 633,
                  "w": 1021
            },
            "ref": {
                  "x": 160,
                  "y": 33,
                  "h": 96,
                  "w": 305
            },
            "threshold": 0.82,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 32,
                              "y": 133,
                              "h": 476,
                              "w": 348
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 407,
                              "y": 362,
                              "h": 38,
                              "w": 270
                        },
                        "ocr_type": 1, "regex": "[0-9]{13}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 201,
                              "h": 71,
                              "w": 302
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 403,
                              "y": 136,
                              "h": 42,
                              "w": 334
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 775,
                              "y": 299,
                              "h": 35,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 405,
                              "y": 431,
                              "h": 33,
                              "w": 194
                        },
                        "ocr_type": 1, "regex": "[A-Z]{2}[0-9]{7}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 777,
                              "y": 429,
                              "h": 40,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 402,
                              "y": 295,
                              "h": 40,
                              "w": 52
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 470,
                              "y": 511,
                              "h": 130,
                              "w": 380
                        }
                  }
            }
      },
    "642_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 874,
                  "w": 1333
            },
            "ref": {
                  "x": 1051,
                  "y": 56,
                  "h": 83,
                  "w": 217
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 84,
                              "y": 256,
                              "h": 310,
                              "w": 264
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 730,
                              "y": 344,
                              "h": 63,
                              "w": 244
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 177,
                              "h": 51,
                              "w": 338
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 117,
                              "h": 63,
                              "w": 355
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 225,
                              "h": 69,
                              "w": 411
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 389,
                              "h": 64,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 471,
                              "y": 337,
                              "h": 54,
                              "w": 188
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 119,
                              "y": 674,
                              "h": 76,
                              "w": 537
                        }
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 571,
                              "y": 466,
                              "h": 139,
                              "w": 279
                        }
                  }
            }
      },
    "703_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 500,
                  "w": 765
            },
            "ref": {
                  "x": 99,
                  "y": 36,
                  "h": 40,
                  "w": 319
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 38,
                              "y": 110,
                              "h": 284,
                              "w": 209
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 234,
                              "h": 35,
                              "w": 181
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 261,
                              "y": 146,
                              "h": 31,
                              "w": 253
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 264,
                              "y": 103,
                              "h": 29,
                              "w": 286
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 192,
                              "h": 29,
                              "w": 153
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 262,
                              "y": 295,
                              "h": 38,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 322,
                              "h": 31,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 263,
                              "y": 235,
                              "h": 29,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 441,
                              "y": 393,
                              "h": 81,
                              "w": 286
                        }
                  }
            }
      },
    "724_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 865,
                  "w": 1536
            },
            "ref": {
                  "x": 261,
                  "y": 53,
                  "h": 109,
                  "w": 475
            },
            "threshold": 0.84,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 45,
                              "y": 229,
                              "h": 587,
                              "w": 537
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 153,
                              "h": 85,
                              "w": 573
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 597,
                              "y": 371,
                              "h": 53,
                              "w": 441
                        },
                        "ocr_type": 0, "regex": "[A-Z]{1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 601,
                              "y": 253,
                              "h": 93,
                              "w": 479
                        },
                        "ocr_type": 0, "regex": "[A-Za-z]{1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 1203,
                              "y": 447,
                              "h": 51,
                              "w": 289
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 603,
                              "h": 55,
                              "w": 333
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 897,
                              "y": 525,
                              "h": 57,
                              "w": 289
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[0-9]{1,2}\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 591,
                              "y": 449,
                              "h": 51,
                              "w": 81
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 647,
                              "y": 651,
                              "h": 127,
                              "w": 527
                        }
                  }
            }
      },
    "578_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 578,
                  "w": 906
            },
            "ref": {
                  "x": 24,
                  "y": 20,
                  "h": 61,
                  "w": 199
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 41,
                              "y": 106,
                              "h": 433,
                              "w": 327
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 376,
                              "y": 136,
                              "h": 36,
                              "w": 380
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 90,
                              "h": 35,
                              "w": 325
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 377,
                              "y": 255,
                              "h": 39,
                              "w": 239
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 377,
                              "y": 325,
                              "h": 36,
                              "w": 230
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 378,
                              "y": 397,
                              "h": 32,
                              "w": 240
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 184,
                              "h": 35,
                              "w": 31
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 382,
                              "y": 455,
                              "h": 80,
                              "w": 256
                        }
                  }
            }
      },
    "470_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 715,
                  "w": 1169
            },
            "ref": {
                  "x": 252,
                  "y": 67,
                  "h": 64,
                  "w": 373
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 61,
                              "y": 231,
                              "h": 386,
                              "w": 285
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 906,
                              "y": 196,
                              "h": 50,
                              "w": 197
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 266,
                              "h": 52,
                              "w": 317
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 231,
                              "h": 43,
                              "w": 347
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 794,
                              "y": 407,
                              "h": 39,
                              "w": 240
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 800,
                              "y": 455,
                              "h": 45,
                              "w": 203
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 528,
                              "h": 43,
                              "w": 239
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 370,
                              "y": 408,
                              "h": 40,
                              "w": 62
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 377,
                              "y": 590,
                              "h": 89,
                              "w": 381
                        }
                  }
            }
      },
    "380_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 386,
                  "w": 600
            },
            "ref": {
                  "x": 117,
                  "y": 22,
                  "h": 47,
                  "w": 288
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 29,
                              "y": 125,
                              "h": 205,
                              "w": 164
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 201,
                              "y": 163,
                              "h": 15,
                              "w": 179
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 202,
                              "y": 132,
                              "h": 17,
                              "w": 171
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 479,
                              "y": 192,
                              "h": 25,
                              "w": 73
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 443,
                              "y": 20,
                              "h": 38,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 265,
                              "h": 19,
                              "w": 74
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 201,
                              "y": 234,
                              "h": 20,
                              "w": 23
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 227,
                              "y": 309,
                              "h": 36,
                              "w": 101
                        }
                  }
            }
      },
    "246_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 646,
                  "w": 1024
            },
            "ref": {
                  "x": 38,
                  "y": 23,
                  "h": 77,
                  "w": 459
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 55,
                              "y": 142,
                              "h": 346,
                              "w": 268
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 255,
                              "h": 44,
                              "w": 246
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 162,
                              "h": 38,
                              "w": 307
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 415,
                              "h": 43,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 730,
                              "y": 417,
                              "h": 38,
                              "w": 187
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 726,
                              "y": 478,
                              "h": 39,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 492,
                              "y": 356,
                              "h": 39,
                              "w": 38
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 37,
                              "y": 526,
                              "h": 70,
                              "w": 424
                        }
                  }
            }
      },
    "203_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 336,
                  "w": 532
            },
            "ref": {
                  "x": 22,
                  "y": 12,
                  "h": 63,
                  "w": 96
            },
            "threshold": 0.83,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 126,
                              "h": 181,
                              "w": 126
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 121,
                              "y": 71,
                              "h": 14,
                              "w": 173
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 130,
                              "y": 90,
                              "h": 15,
                              "w": 175
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 184,
                              "y": 119,
                              "h": 25,
                              "w": 166
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 372,
                              "y": 42,
                              "h": 23,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 180,
                              "y": 287,
                              "h": 30,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 123,
                              "h": 48,
                              "w": 72
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 331,
                              "y": 245,
                              "h": 56,
                              "w": 164
                        }
                  }
            }
      },
    "440_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 645,
                  "w": 1024
            },
            "ref": {
                  "x": 25,
                  "y": 23,
                  "h": 108,
                  "w": 307
            },
            "threshold": 0.84,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 34,
                              "y": 175,
                              "h": 436,
                              "w": 317
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 540,
                              "y": 417,
                              "h": 37,
                              "w": 185
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 373,
                              "y": 260,
                              "h": 40,
                              "w": 328
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 166,
                              "h": 38,
                              "w": 384
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 788,
                              "y": 415,
                              "h": 38,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 539,
                              "y": 480,
                              "h": 37,
                              "w": 156
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 788,
                              "y": 480,
                              "h": 45,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 350,
                              "h": 32,
                              "w": 102
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 378,
                              "y": 538,
                              "h": 81,
                              "w": 336
                        }
                  }
            }
      },
    "428_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 338,
                  "w": 544
            },
            "ref": {
                  "x": 11,
                  "y": 9,
                  "h": 21,
                  "w": 172
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 18,
                              "y": 57,
                              "h": 242,
                              "w": 183
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 320,
                              "y": 171,
                              "h": 30,
                              "w": 151
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 107,
                              "h": 19,
                              "w": 150
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 56,
                              "h": 23,
                              "w": 165
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 215,
                              "h": 22,
                              "w": 99
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 420,
                              "y": 5,
                              "h": 23,
                              "w": 104
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 255,
                              "h": 20,
                              "w": 105
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 205,
                              "y": 290,
                              "h": 41,
                              "w": 127
                        }
                  }
            }
      },
    "804_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 571,
                  "w": 911
            },
            "ref": {
                  "x": 474,
                  "y": 20,
                  "h": 102,
                  "w": 383
            },
            "threshold": 0.73,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 136,
                              "h": 400,
                              "w": 312
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 626,
                              "y": 401,
                              "h": 42,
                              "w": 238
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 378,
                              "y": 205,
                              "h": 67,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 121,
                              "h": 67,
                              "w": 312
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 383,
                              "y": 402,
                              "h": 40,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 620,
                              "y": 457,
                              "h": 42,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 385,
                              "y": 460,
                              "h": 40,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 346,
                              "h": 39,
                              "w": 78
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 471,
                              "y": 497,
                              "h": 61,
                              "w": 234
                        }
                  }
            }
      },
    "826_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 600,
                  "w": 1200
            },
            "ref": {
                  "x": 884,
                  "y": 147,
                  "h": 201,
                  "w": 286
            },
            "threshold": 0.59,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 216,
                              "h": 351,
                              "w": 391
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 196,
                              "y": 160,
                              "h": 49,
                              "w": 424
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 195,
                              "y": 116,
                              "h": 47,
                              "w": 425
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 429,
                              "y": 374,
                              "h": 52,
                              "w": 285
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 433,
                              "y": 508,
                              "h": 52,
                              "w": 228
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 430,
                              "y": 313,
                              "h": 46,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 828,
                              "y": 477,
                              "h": 83,
                              "w": 325
                        }
                  }
            }
      },
    "826_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 590,
                  "w": 845
            },
            "ref": {
                  "x": 101,
                  "y": 6,
                  "h": 39,
                  "w": 185
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 62,
                              "y": 114,
                              "h": 268,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 530,
                              "y": 75,
                              "h": 36,
                              "w": 149
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 292,
                              "y": 157,
                              "h": 33,
                              "w": 333
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 116,
                              "h": 35,
                              "w": 333
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 237,
                              "h": 33,
                              "w": 238
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 287,
                              "y": 356,
                              "h": 34,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 430,
                              "y": 313,
                              "h": 46,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 529,
                              "y": 368,
                              "h": 63,
                              "w": 223
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 27,
                              "y": 439,
                              "h": 115,
                              "w": 773
                        },
                        "ocr_type": 1, "regex": "",
                        "check_mrz": True
                  }
            }
      },
    "784_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 585,
                  "w": 909
            },
            "ref": {
                  "x": 9,
                  "y": 18,
                  "h": 43,
                  "w": 367
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 45,
                              "y": 127,
                              "h": 269,
                              "w": 219
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 308,
                              "y": 172,
                              "h": 58,
                              "w": 279
                        },
                        "ocr_type": 1, "regex": "[0-9]{3}\\-[0-9]{4}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 351,
                              "y": 249,
                              "h": 56,
                              "w": 348
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 483,
                              "y": 286,
                              "h": 66,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 336,
                              "y": 500,
                              "h": 63,
                              "w": 178
                        },
                        "ocr_type": 1,
                        "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 809,
                              "y": 485,
                              "h": 66,
                              "w": 74
                        },
                        "ocr_type": 1,
                        "regex": "[MF]{1}"
                  },
                  "6": {
                        "name": "nationality",
                        "type": 0,
                        "points": {
                              "x": 410,
                              "y": 378,
                              "h": 50,
                              "w": 238
                        },
                        "regex": "([A-Za-z]+\\s?){1,}",
                        "ocr_type": 1
                  }
            }
      },
    "756_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 163,
                  "y": 81,
                  "h": 132,
                  "w": 350
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 177,
                              "y": 251,
                              "h": 336,
                              "w": 267
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 810,
                              "y": 244,
                              "h": 54,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 463,
                              "y": 435,
                              "h": 38,
                              "w": 277
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 340,
                              "h": 66,
                              "w": 387
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 466,
                              "y": 559,
                              "h": 49,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 752,
                              "y": 487,
                              "h": 71,
                              "w": 246
                        }
                  }
            }
      },
    "710_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 161,
                  "y": 99,
                  "h": 82,
                  "w": 406
            },
            "threshold": 0.77,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 736,
                              "y": 179,
                              "h": 326,
                              "w": 275
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 432,
                              "h": 31,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 276,
                              "h": 30,
                              "w": 276
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 223,
                              "h": 32,
                              "w": 347
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 485,
                              "h": 32,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 326,
                              "h": 35,
                              "w": 44
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 798,
                              "y": 548,
                              "h": 61,
                              "w": 242
                        }
                  }
            }
      },
    "705_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 351,
                  "y": 103,
                  "h": 106,
                  "w": 302
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 148,
                              "y": 246,
                              "h": 343,
                              "w": 294
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 770,
                              "y": 165,
                              "h": 50,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 416,
                              "h": 44,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 336,
                              "h": 61,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 493,
                              "h": 39,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 562,
                              "h": 42,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 494,
                              "h": 40,
                              "w": 34
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 725,
                              "y": 510,
                              "h": 79,
                              "w": 280
                        }
                  }
            }
      },
    "528_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 665,
                  "w": 1142
            },
            "ref": {
                  "x": 108,
                  "y": 53,
                  "h": 69,
                  "w": 303
            },
            "threshold": 0.62,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 124,
                              "y": 133,
                              "h": 343,
                              "w": 235
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 420,
                              "y": 259,
                              "h": 37,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": "[A-Za-z]{1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 418,
                              "y": 210,
                              "h": 35,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": "[A-Za-z]{1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 419,
                              "y": 364,
                              "h": 36,
                              "w": 305
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 782,
                              "y": 158,
                              "h": 36,
                              "w": 194
                        },
                        "ocr_type": 1, "regex": "[0-9]{9}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 415,
                              "y": 462,
                              "h": 40,
                              "w": 272
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 415,
                              "y": 310,
                              "h": 37,
                              "w": 69
                        },
                        "ocr_type": 1, "regex": "[A-Z]\\/[A-Z]"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 117,
                              "y": 498,
                              "h": 73,
                              "w": 263
                        }
                  }
            }
      },
    "528_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 440,
                  "w": 600
            },
            "ref": {
                  "x": 398,
                  "y": 20,
                  "h": 30,
                  "w": 194
            },
            "threshold": 0.60,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 18,
                              "y": 66,
                              "h": 207,
                              "w": 157
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 190,
                              "y": 128,
                              "h": 27,
                              "w": 259
                        },
                        "ocr_type": 0, "regex": "[A-Za-z]{1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 186,
                              "y": 88,
                              "h": 23,
                              "w": 207
                        },
                        "ocr_type": 0, "regex": "[A-Za-z]{1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 175,
                              "y": 154,
                              "h": 24,
                              "w": 195
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 432,
                              "y": 64,
                              "h": 26,
                              "w": 154
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{1}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 447,
                              "y": 231,
                              "h": 26,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 191,
                              "y": 204,
                              "h": 23,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": "[A-Z]\\/[A-Z]"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 191,
                              "y": 256,
                              "h": 333,
                              "w": 363
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 191,
                              "y": 256,
                              "h": 333,
                              "w": 363
                        },
                        "check_mrz": True
                  }
            }
      },
    "442_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 911,
                  "y": 419,
                  "h": 186,
                  "w": 104
            },
            "threshold": 0.9,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 169,
                              "y": 201,
                              "h": 324,
                              "w": 258
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 328,
                              "h": 40,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 469,
                              "y": 236,
                              "h": 38,
                              "w": 277
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 473,
                              "y": 449,
                              "h": 37,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 508,
                              "h": 42,
                              "w": 221
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 472,
                              "y": 572,
                              "h": 50,
                              "w": 164
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 388,
                              "h": 44,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 167,
                              "y": 530,
                              "h": 54,
                              "w": 272
                        }
                  }
            }
      },
    "417_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 142,
                  "y": 72,
                  "h": 102,
                  "w": 358
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 175,
                              "y": 216,
                              "h": 346,
                              "w": 244
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 751,
                              "y": 509,
                              "h": 38,
                              "w": 183
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 469,
                              "y": 274,
                              "h": 59,
                              "w": 317
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 470,
                              "y": 201,
                              "h": 62,
                              "w": 360
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 472,
                              "y": 495,
                              "h": 37,
                              "w": 159
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 753,
                              "y": 576,
                              "h": 36,
                              "w": 154
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 473,
                              "y": 393,
                              "h": 42,
                              "w": 90
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 472,
                              "y": 551,
                              "h": 65,
                              "w": 246
                        }
                  }
            }
      },
    "268_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 132,
                  "y": 94,
                  "h": 86,
                  "w": 310
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 165,
                              "y": 209,
                              "h": 358,
                              "w": 262
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 715,
                              "y": 445,
                              "h": 40,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 447,
                              "y": 287,
                              "h": 38,
                              "w": 262
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 454,
                              "y": 352,
                              "h": 34,
                              "w": 247
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 451,
                              "y": 525,
                              "h": 40,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 202,
                              "y": 585,
                              "h": 44,
                              "w": 212
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 665,
                              "y": 520,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 600,
                              "y": 451,
                              "h": 35,
                              "w": 103
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 706,
                              "y": 573,
                              "h": 76,
                              "w": 254
                        }
                  }
            }
      },
    "8_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 653,
                  "w": 1040
            },
            "ref": {
                  "x": 330,
                  "y": 17,
                  "h": 33,
                  "w": 361
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 82,
                              "y": 111,
                              "h": 305,
                              "w": 223
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 685,
                              "y": 459,
                              "h": 47,
                              "w": 232
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 327,
                              "y": 171,
                              "h": 41,
                              "w": 282
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 326,
                              "y": 113,
                              "h": 43,
                              "w": 303
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 328,
                              "y": 345,
                              "h": 39,
                              "w": 195
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 688,
                              "y": 229,
                              "h": 47,
                              "w": 204
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 684,
                              "y": 402,
                              "h": 41,
                              "w": 258
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 684,
                              "y": 345,
                              "h": 39,
                              "w": 56
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 59,
                              "y": 460,
                              "h": 73,
                              "w": 251
                        }
                  }
            }
      },
    "752_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 622,
                  "w": 1024
            },
            "ref": {
                  "x": 66,
                  "y": 18,
                  "h": 94,
                  "w": 309
            },
            "threshold": 0.67,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 55,
                              "y": 152,
                              "h": 406,
                              "w": 295
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 390,
                              "y": 284,
                              "h": 34,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 171,
                              "h": 37,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 113,
                              "h": 35,
                              "w": 443
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 227,
                              "h": 37,
                              "w": 243
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 486,
                              "y": 337,
                              "h": 35,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 484,
                              "y": 411,
                              "h": 39,
                              "w": 233
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 389,
                              "y": 227,
                              "h": 37,
                              "w": 59
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 682,
                              "y": 513,
                              "h": 96,
                              "w": 334
                        }
                  }
            }
      },
    "840_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1010,
                  "w": 1521
            },
            "ref": {
                  "x": 506,
                  "y": 12,
                  "h": 89,
                  "w": 542
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 1069,
                              "y": 141,
                              "h": 61,
                              "w": 301
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "1": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 535,
                              "y": 200,
                              "h": 55,
                              "w": 445
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 535,
                              "y": 271,
                              "h": 59,
                              "w": 383
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 530,
                              "y": 412,
                              "h": 62,
                              "w": 227
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 526,
                              "y": 635,
                              "h": 65,
                              "w": 219
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 1208,
                              "y": 486,
                              "h": 65,
                              "w": 69
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 24,
                              "y": 823,
                              "h": 160,
                              "w": 1478
                        },
                        "check_mrz": True
                  },
                  "7": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 104,
                              "y": 206,
                              "h": 550,
                              "w": 380
                        }
                  }
            }
      },
    "586_nic_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 651,
                  "w": 1031
            },
            "ref": {
                  "x": 243,
                  "y": 33,
                  "h": 88,
                  "w": 265
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 726,
                              "y": 145,
                              "h": 325,
                              "w": 238
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 283,
                              "y": 472,
                              "h": 58,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 130,
                              "h": 70,
                              "w": 431
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 281,
                              "y": 259,
                              "h": 70,
                              "w": 402
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 280,
                              "y": 391,
                              "h": 59,
                              "w": 100
                        },
                        "ocr_type": 1, "regex": "([FM]){1}"
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 520,
                              "y": 460,
                              "h": 60,
                              "w": 180
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 520,
                              "y": 535,
                              "h": 65,
                              "w": 180
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 740,
                              "y": 464,
                              "h": 108,
                              "w": 223
                        }
                  }
            }
      },
    "586_nic_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 752,
                  "w": 1148
            },
            "ref": {
                  "x": 178,
                  "y": 41,
                  "h": 53,
                  "w": 313
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 40,
                              "y": 57,
                              "h": 130,
                              "w": 125
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 815,
                              "y": 40,
                              "h": 65,
                              "w": 270
                        },
                        "ocr_type": 0, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "present_address",
                        "type": 1,
                        "points": {
                              "x": 179,
                              "y": 81,
                              "h": 100,
                              "w": 664
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "3": {
                        "name": "permanent_address",
                        "type": 1,
                        "points": {
                              "x": 184,
                              "y": 238,
                              "h": 100,
                              "w": 635
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "4": {
                        "name": "mrz",
                        "mrz_type": "",
                        "type": 2,
                        "points": {
                              "x": 25,
                              "y": 490,
                              "h": 220,
                              "w": 1050
                        },
                        "check_mrz": True
                  }
            }
      },
    "586_nicop_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 421,
                  "w": 669
            },
            "ref": {
                  "x": 161,
                  "y": 24,
                  "h": 46,
                  "w": 194
            },
            "threshold": 0.55,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 25,
                              "y": 68,
                              "h": 205,
                              "w": 168
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 255,
                              "y": 124,
                              "h": 40,
                              "w": 232
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}\\-[0-9]{6}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 278,
                              "y": 163,
                              "h": 32,
                              "w": 221
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 338,
                              "y": 194,
                              "h": 29,
                              "w": 249
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 340,
                              "y": 223,
                              "h": 29,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 254,
                              "h": 25,
                              "w": 123
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 452,
                              "y": 306,
                              "h": 58,
                              "w": 204
                        }
                  }
            }
      },
    "586_nicop_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 638,
                  "w": 1024
            },
            "ref": {
                  "x": 225,
                  "y": 109,
                  "h": 54,
                  "w": 268
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 77,
                              "y": 191,
                              "h": 151,
                              "w": 130
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 956,
                              "y": 158,
                              "h": 267,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "present_address",
                        "type": 1,
                        "points": {
                              "x": 214,
                              "y": 142,
                              "h": 87,
                              "w": 589
                        },
                        "ocr_type": 0, "regex": "([-,/0-9A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "permanent_address",
                        "type": 1,
                        "points": {
                              "x": 215,
                              "y": 258,
                              "h": 93,
                              "w": 583
                        },
                        "ocr_type": 0, "regex": "([-,/0-9A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 876,
                              "y": 227,
                              "h": 199,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "mrz",
                        "mrz_type": "td1",
                        "type": 2,
                        "points": {
                              "x": 66,
                              "y": 441,
                              "h": 181,
                              "w": 923
                        },
                        "check_mrz": True
                  }
            }
      },
    "414_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 544,
                  "w": 1024
            },
            "ref": {
                  "x": 272,
                  "y": 101,
                  "h": 42,
                  "w": 523
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 143,
                              "y": 133,
                              "h": 249,
                              "w": 184
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 142,
                              "h": 48,
                              "w": 246
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 305,
                              "h": 51,
                              "w": 462
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 363,
                              "y": 404,
                              "h": 44,
                              "w": 86
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 642,
                              "y": 469,
                              "h": 49,
                              "w": 143
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 311,
                              "y": 465,
                              "h": 45,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "196_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 460,
                  "w": 730
            },
            "ref": {
                  "x": 35,
                  "y": 12,
                  "h": 56,
                  "w": 352
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 39,
                              "y": 190,
                              "h": 241,
                              "w": 190
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 541,
                              "y": 32,
                              "h": 40,
                              "w": 176
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 28,
                              "y": 150,
                              "h": 39,
                              "w": 196
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 28,
                              "y": 91,
                              "h": 44,
                              "w": 226
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 435,
                              "y": 206,
                              "h": 39,
                              "w": 79
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 206,
                              "h": 42,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 248,
                              "y": 341,
                              "h": 41,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 246,
                              "y": 397,
                              "h": 46,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 501,
                              "y": 383,
                              "h": 64,
                              "w": 209
                        }
                  }
            }
      },
    "498_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 500,
                  "w": 780
            },
            "ref": {
                  "x": 140,
                  "y": 32,
                  "h": 39,
                  "w": 406
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 64,
                              "y": 131,
                              "h": 271,
                              "w": 209
                        }
                  },
                  "1": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 582,
                              "y": 48,
                              "h": 41,
                              "w": 160
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 291,
                              "y": 189,
                              "h": 32,
                              "w": 215
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 142,
                              "h": 30,
                              "w": 253
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 241,
                              "h": 30,
                              "w": 47
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 291,
                              "y": 286,
                              "h": 32,
                              "w": 146
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 289,
                              "y": 380,
                              "h": 33,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 163,
                              "y": 406,
                              "h": 69,
                              "w": 191
                        }
                  }
            }
      },
    "458_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 154,
                  "y": 68,
                  "h": 101,
                  "w": 496
            },
            "threshold": 0.48,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 727,
                              "y": 212,
                              "h": 349,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 124,
                              "y": 172,
                              "h": 56,
                              "w": 330
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}\\-[0-9]{2}\\-[0-9]{4}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 136,
                              "y": 427,
                              "h": 52,
                              "w": 400
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  }
            }
      },
    "458_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 788,
                  "w": 1108
            },
            "ref": {
                  "x": 77,
                  "y": 54,
                  "h": 70,
                  "w": 241
            },
            "threshold": 0.48,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 74,
                              "y": 159,
                              "h": 343,
                              "w": 262
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 186,
                              "h": 37,
                              "w": 210
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 703,
                              "y": 244,
                              "h": 40,
                              "w": 189
                        },
                        "ocr_type": 1, "regex": "[0-9]{12}"
                  },
                  "3": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 842,
                              "y": 113,
                              "h": 32,
                              "w": 153
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}[0-9]{8}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 306,
                              "h": 37,
                              "w": 172
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 705,
                              "y": 427,
                              "h": 33,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 349,
                              "y": 365,
                              "h": 35,
                              "w": 77
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}\\-[A-Z]{1}"
                  }
            }
      },
    "524_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 634,
                  "w": 1024
            },
            "ref": {
                  "x": 51,
                  "y": 30,
                  "h": 86,
                  "w": 97
            },
            "threshold": 0.85,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 719,
                              "y": 141,
                              "h": 308,
                              "w": 228
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 62,
                              "y": 388,
                              "h": 54,
                              "w": 204
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 264,
                              "h": 68,
                              "w": 283
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 146,
                              "h": 80,
                              "w": 300
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 205,
                              "y": 143,
                              "h": 42,
                              "w": 61
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 481,
                              "y": 388,
                              "h": 45,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 689,
                              "y": 513,
                              "h": 91,
                              "w": 286
                        }
                  }
            }
      },
    "70_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 803,
                  "w": 1280
            },
            "ref": {
                  "x": 67,
                  "y": 21,
                  "h": 120,
                  "w": 376
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 72,
                              "y": 178,
                              "h": 496,
                              "w": 381
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 417,
                              "h": 80,
                              "w": 295
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 221,
                              "h": 77,
                              "w": 424
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 121,
                              "y": 700,
                              "h": 49,
                              "w": 291
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 541,
                              "h": 48,
                              "w": 108
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 496,
                              "y": 633,
                              "h": 44,
                              "w": 178
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 491,
                              "y": 715,
                              "h": 45,
                              "w": 183
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 804,
                              "y": 651,
                              "h": 88,
                              "w": 369
                        }
                  }
            }
      },
    "674_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 389,
                  "w": 614
            },
            "ref": {
                  "x": 212,
                  "y": 8,
                  "h": 63,
                  "w": 383
            },
            "threshold": 0.51,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 26,
                              "y": 154,
                              "h": 205,
                              "w": 172
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 208,
                              "y": 204,
                              "h": 48,
                              "w": 270
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 210,
                              "y": 138,
                              "h": 41,
                              "w": 267
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 204,
                              "y": 87,
                              "h": 31,
                              "w": 125
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 207,
                              "y": 272,
                              "h": 23,
                              "w": 202
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "608_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 684,
                  "w": 1072
            },
            "ref": {
                  "x": 88,
                  "y": 13,
                  "h": 155,
                  "w": 142
            },
            "threshold": 0.87,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 57,
                              "y": 271,
                              "h": 257,
                              "w": 232
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 20,
                              "y": 192,
                              "h": 67,
                              "w": 373
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 491,
                              "y": 332,
                              "h": 79,
                              "w": 486
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 485,
                              "y": 255,
                              "h": 46,
                              "w": 508
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 489,
                              "y": 512,
                              "h": 58,
                              "w": 331
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "608_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 651,
                  "w": 963
            },
            "ref": {
                  "x": 127,
                  "y": 52,
                  "h": 35,
                  "w": 329
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 42,
                              "y": 148,
                              "h": 345,
                              "w": 291
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 613,
                              "y": 93,
                              "h": 68,
                              "w": 253
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 212,
                              "h": 44,
                              "w": 255
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 154,
                              "h": 49,
                              "w": 290
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 308,
                              "h": 48,
                              "w": 267
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 456,
                              "h": 63,
                              "w": 236
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 314,
                              "y": 366,
                              "h": 44,
                              "w": 73
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 48,
                              "y": 515,
                              "h": 124,
                              "w": 891
                        }
                  },
            }
      },
    "702_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 400,
                  "w": 614
            },
            "ref": {
                  "x": 426,
                  "y": 5,
                  "h": 119,
                  "w": 139
            },
            "threshold": 0.85,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 36,
                              "y": 96,
                              "h": 202,
                              "w": 152
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 308,
                              "y": 147,
                              "h": 34,
                              "w": 179
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 210,
                              "y": 144,
                              "h": 36,
                              "w": 93
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 212,
                              "y": 305,
                              "h": 27,
                              "w": 124
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 226,
                              "y": 48,
                              "h": 38,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 348,
                              "y": 307,
                              "h": 26,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "688_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 452,
                  "w": 720
            },
            "ref": {
                  "x": 241,
                  "y": 17,
                  "h": 39,
                  "w": 249
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 38,
                              "y": 115,
                              "h": 238,
                              "w": 197
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 164,
                              "h": 30,
                              "w": 227
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 238,
                              "y": 116,
                              "h": 34,
                              "w": 258
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 210,
                              "h": 33,
                              "w": 262
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 350,
                              "h": 37,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 370,
                              "y": 257,
                              "h": 35,
                              "w": 181
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 258,
                              "h": 33,
                              "w": 64
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 521,
                              "y": 376,
                              "h": 56,
                              "w": 167
                        }
                  }
            }
      },
    "356_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 534,
                  "w": 900
            },
            "ref": {
                  "x": 15,
                  "y": 338,
                  "h": 136,
                  "w": 221
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 17,
                              "y": 119,
                              "h": 224,
                              "w": 199
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 287,
                              "y": 135,
                              "h": 36,
                              "w": 307
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 285,
                              "y": 165,
                              "h": 34,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "3": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 267,
                              "y": 193,
                              "h": 33,
                              "w": 54
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "372_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 571,
                  "w": 850
            },
            "ref": {
                  "x": 116,
                  "y": 15,
                  "h": 55,
                  "w": 148
            },
            "threshold": 0.77,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 14,
                              "y": 105,
                              "h": 343,
                              "w": 251
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 569,
                              "y": 131,
                              "h": 41,
                              "w": 253
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 281,
                              "y": 231,
                              "h": 38,
                              "w": 238
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 282,
                              "y": 182,
                              "h": 38,
                              "w": 272
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 566,
                              "y": 282,
                              "h": 40,
                              "w": 285
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 570,
                              "y": 381,
                              "h": 37,
                              "w": 279
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 277,
                              "y": 334,
                              "h": 33,
                              "w": 50
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 322,
                              "y": 455,
                              "h": 75,
                              "w": 490
                        }
                  }
            }
      },
    "32_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 637,
                  "w": 1024
            },
            "ref": {
                  "x": 59,
                  "y": 33,
                  "h": 100,
                  "w": 284
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 84,
                              "y": 151,
                              "h": 349,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 385,
                              "y": 540,
                              "h": 60,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 218,
                              "h": 39,
                              "w": 285
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 386,
                              "y": 131,
                              "h": 41,
                              "w": 329
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 388,
                              "y": 365,
                              "h": 34,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 383,
                              "y": 479,
                              "h": 39,
                              "w": 219
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 80,
                              "y": 547,
                              "h": 54,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 381,
                              "y": 304,
                              "h": 36,
                              "w": 74
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 754,
                              "y": 343,
                              "h": 95,
                              "w": 216
                        }
                  }
            }
      },
    "344_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 601,
                  "w": 955
            },
            "ref": {
                  "x": 127,
                  "y": 71,
                  "h": 47,
                  "w": 210
            },
            "threshold": 0.43,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 53,
                              "y": 220,
                              "h": 340,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 220,
                              "h": 49,
                              "w": 310
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 155,
                              "y": 175,
                              "h": 49,
                              "w": 265
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 27,
                              "y": 177,
                              "h": 44,
                              "w": 110
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 345,
                              "h": 46,
                              "w": 221
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 517,
                              "h": 56,
                              "w": 223
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 645,
                              "y": 519,
                              "h": 58,
                              "w": 276
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 610,
                              "y": 341,
                              "h": 51,
                              "w": 72
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "51_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 592,
                  "w": 928
            },
            "ref": {
                  "x": 595,
                  "y": 40,
                  "h": 81,
                  "w": 265
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 49,
                              "y": 225,
                              "h": 314,
                              "w": 233
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 604,
                              "y": 432,
                              "h": 39,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 299,
                              "y": 266,
                              "h": 44,
                              "w": 304
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 298,
                              "y": 181,
                              "h": 35,
                              "w": 343
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 301,
                              "y": 432,
                              "h": 34,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 304,
                              "y": 486,
                              "h": 41,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 302,
                              "y": 381,
                              "h": 35,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "364_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1117,
                  "w": 1599
            },
            "ref": {
                  "x": 898,
                  "y": 86,
                  "h": 42,
                  "w": 165
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 85,
                              "y": 175,
                              "h": 579,
                              "w": 399
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 1309,
                              "y": 175,
                              "h": 70,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]){1,}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 629,
                              "y": 347,
                              "h": 80,
                              "w": 371
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 659,
                              "y": 255,
                              "h": 85,
                              "w": 369
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 887,
                              "y": 549,
                              "h": 75,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "expired_date",
                        "type": 0,
                        "points": {
                              "x": 787,
                              "y": 841,
                              "h": 85,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 597,
                              "y": 689,
                              "h": 85,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 93,
                              "y": 915,
                              "h": 175,
                              "w": 1400
                        },
                        "check_mrz": True
                  }
            }
      },
    "214_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 120,
                  "y": 71,
                  "h": 100,
                  "w": 433
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 132,
                              "y": 200,
                              "h": 336,
                              "w": 245
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 477,
                              "y": 167,
                              "h": 64,
                              "w": 412
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 153,
                              "y": 540,
                              "h": 35,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 154,
                              "y": 580,
                              "h": 38,
                              "w": 299
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 409,
                              "y": 319,
                              "h": 33,
                              "w": 252
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 406,
                              "y": 486,
                              "h": 50,
                              "w": 264
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 481,
                              "y": 388,
                              "h": 44,
                              "w": 34
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 134,
                              "y": 466,
                              "h": 65,
                              "w": 242
                        }
                  }
            }
      },
    "124_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 139,
                  "y": 75,
                  "h": 58,
                  "w": 233
            },
            "threshold": 0.74,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 136,
                              "y": 198,
                              "h": 350,
                              "w": 307
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 275,
                              "h": 36,
                              "w": 212
                        },
                        "ocr_type": 1, "regex": "[0-9]{4}\\-[0-9]{4}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 461,
                              "y": 197,
                              "h": 39,
                              "w": 340
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 161,
                              "h": 37,
                              "w": 237
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 512,
                              "h": 41,
                              "w": 264
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 462,
                              "y": 569,
                              "h": 40,
                              "w": 246
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 453,
                              "y": 354,
                              "h": 43,
                              "w": 40
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 193,
                              "y": 554,
                              "h": 70,
                              "w": 220
                        }
                  }
            }
      },
    "124_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 562,
                  "w": 816
            },
            "ref": {
                  "x": 354,
                  "y": 5,
                  "h": 49,
                  "w": 185
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 31,
                              "y": 97,
                              "h": 364,
                              "w": 294
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 240,
                              "y": 150,
                              "h": 30,
                              "w": 354
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 240,
                              "y": 113,
                              "h": 32,
                              "w": 323
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 235,
                              "y": 228,
                              "h": 33,
                              "w": 278
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 248,
                              "y": 349,
                              "h": 32,
                              "w": 241
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 246,
                              "y": 267,
                              "h": 38,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "6": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 577,
                              "y": 73,
                              "h": 40,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{8}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 16,
                              "y": 434,
                              "h": 116,
                              "w": 771
                        },
                        "check_mrz": True
                  }
            }
      },
    "76_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 385,
                  "y": 77,
                  "h": 70,
                  "w": 380
            },
            "threshold": 0.72,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 743,
                              "y": 214,
                              "h": 316,
                              "w": 267
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 151,
                              "y": 413,
                              "h": 55,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": "[0-9]{8}\\-[0-9]{2}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 227,
                              "h": 29,
                              "w": 332
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 196,
                              "h": 33,
                              "w": 396
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 359,
                              "y": 373,
                              "h": 35,
                              "w": 138
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 425,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 274,
                              "h": 36,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 452,
                              "y": 526,
                              "h": 90,
                              "w": 263
                        }
                  }
            }
      },
    "76_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 780,
                  "w": 1287
            },
            "ref": {
                  "x": 134,
                  "y": 80,
                  "h": 74,
                  "w": 188
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 30,
                              "y": 98,
                              "h": 296,
                              "w": 221
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 250,
                              "y": 151,
                              "h": 33,
                              "w": 282
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 250,
                              "y": 113,
                              "h": 32,
                              "w": 215
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 249,
                              "y": 231,
                              "h": 31,
                              "w": 296
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 252,
                              "y": 350,
                              "h": 29,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 252,
                              "y": 270,
                              "h": 30,
                              "w": 38
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "6": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 587,
                              "y": 74,
                              "h": 35,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": "[A-Z]{2}[0-9]{6}"
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 28,
                              "y": 427,
                              "h": 111,
                              "w": 760
                        },
                        "check_mrz": True
                  }
            }
      },
    "112_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 131,
                  "y": 80,
                  "h": 82,
                  "w": 314
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 136,
                              "y": 168,
                              "h": 318,
                              "w": 285
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 615,
                              "y": 167,
                              "h": 35,
                              "w": 276
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 500,
                              "y": 302,
                              "h": 92,
                              "w": 393
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 505,
                              "y": 207,
                              "h": 94,
                              "w": 364
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 560,
                              "y": 467,
                              "h": 41,
                              "w": 164
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 847,
                              "y": 567,
                              "h": 46,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 563,
                              "y": 563,
                              "h": 53,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 855,
                              "y": 461,
                              "h": 56,
                              "w": 112
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 125,
                              "y": 555,
                              "h": 69,
                              "w": 234
                        }
                  }
            }
      },
    "152_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 680,
                  "w": 1074
            },
            "ref": {
                  "x": 254,
                  "y": 19,
                  "h": 70,
                  "w": 547
            },
            "threshold": 0.63,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 58,
                              "y": 164,
                              "h": 379,
                              "w": 275
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 118,
                              "y": 578,
                              "h": 57,
                              "w": 222
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 368,
                              "y": 219,
                              "h": 45,
                              "w": 477
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 363,
                              "y": 117,
                              "h": 77,
                              "w": 427
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 367,
                              "y": 352,
                              "h": 51,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 616,
                              "y": 355,
                              "h": 45,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 615,
                              "y": 424,
                              "h": 44,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 610,
                              "y": 286,
                              "h": 46,
                              "w": 49
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 356,
                              "y": 490,
                              "h": 129,
                              "w": 452
                        }
                  }
            }
      },
    "496_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 832,
                  "w": 1108
            },
            "ref": {
                  "x": 792,
                  "y": 66,
                  "h": 63,
                  "w": 236
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 41,
                              "y": 179,
                              "h": 423,
                              "w": 295
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 797,
                              "y": 145,
                              "h": 59,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}[0-9]{7}"
                  },
                  "5": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 792,
                              "y": 220,
                              "h": 65,
                              "w": 210
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{10}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 301,
                              "h": 56,
                              "w": 184
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 210,
                              "h": 61,
                              "w": 245
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 358,
                              "y": 478,
                              "h": 55,
                              "w": 169
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 782,
                              "y": 574,
                              "h": 52,
                              "w": 159
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 779,
                              "y": 484,
                              "h": 57,
                              "w": 61
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 3,
                        "points": {
                              "x": 13,
                              "y": 646,
                              "h": 157,
                              "w": 1076
                        },
                        "check_mrz": True
                  }
            }
      },
    "275_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 521,
                  "w": 792
            },
            "ref": {
                  "x": 29,
                  "y": 23,
                  "h": 36,
                  "w": 219
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 517,
                              "y": 127,
                              "h": 322,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 541,
                              "y": 453,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{10}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 88,
                              "y": 312,
                              "h": 38,
                              "w": 129
                        },
                        "ocr_type": 1, "regex": "[0-9]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 407,
                              "y": 215,
                              "h": 35,
                              "w": 97
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 156,
                              "h": 32,
                              "w": 91
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 338,
                              "y": 248,
                              "h": 39,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 342,
                              "y": 278,
                              "h": 34,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "7": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 401,
                              "y": 369,
                              "h": 40,
                              "w": 74
                        }
                  }
            }
      },
    "598_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 714,
                  "w": 1105
            },
            "ref": {
                  "x": 495,
                  "y": 48,
                  "h": 64,
                  "w": 148
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 75,
                              "y": 92,
                              "h": 342,
                              "w": 271
                        }
                  },
                  "1": {
                        "name": "licence_number",
                        "type": 0,
                        "points": {
                              "x": 162,
                              "y": 549,
                              "h": 87,
                              "w": 186
                        },
                        "ocr_type": 1, "regex": "[0-9]{5}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 477,
                              "y": 186,
                              "h": 40,
                              "w": 387
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 682,
                              "y": 477,
                              "h": 50,
                              "w": 365
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 387,
                              "y": 566,
                              "h": 71,
                              "w": 297
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 670,
                              "y": 357,
                              "h": 79,
                              "w": 274
                        }
                  }
            }
      },
    "704_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 573,
                  "w": 810
            },
            "ref": {
                  "x": 70,
                  "y": 70,
                  "h": 35,
                  "w": 208
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 78,
                              "y": 111,
                              "h": 269,
                              "w": 196
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 576,
                              "y": 95,
                              "h": 41,
                              "w": 122
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}[0-9]{7}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 143,
                              "h": 39,
                              "w": 197
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 295,
                              "y": 217,
                              "h": 35,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 521,
                              "y": 314,
                              "h": 38,
                              "w": 142
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 285,
                              "y": 265,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1,}\\/[A-Z]{1,}"
                  },
                  "6": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 49,
                              "y": 409,
                              "h": 123,
                              "w": 729
                        },
                        "check_mrz": True
                  }
            }
      },
    "36_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 591,
                  "w": 898
            },
            "ref": {
                  "x": 218,
                  "y": 38,
                  "h": 47,
                  "w": 235
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 633,
                              "y": 243,
                              "h": 237,
                              "w": 195
                        }
                  },
                  "1": {
                        "name": "licence_number",
                        "type": 0,
                        "points": {
                              "x": 714,
                              "y": 181,
                              "h": 51,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": "[0-9]{7}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 15,
                              "y": 268,
                              "h": 33,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 17,
                              "y": 235,
                              "h": 33,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 304,
                              "y": 389,
                              "h": 43,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[a-zA-Z]{3}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 17,
                              "y": 383,
                              "h": 48,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\s[a-zA-Z]{3}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 12,
                              "y": 450,
                              "h": 38,
                              "w": 253
                        }
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 12,
                              "y": 484,
                              "h": 87,
                              "w": 321
                        }
                  }
            }
      },
    "504_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 757,
                  "w": 1106
            },
            "ref": {
                  "x": 9,
                  "y": 4,
                  "h": 45,
                  "w": 308
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 633,
                              "y": 243,
                              "h": 237,
                              "w": 195
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 717,
                              "y": 90,
                              "h": 42,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 348,
                              "y": 179,
                              "h": 45,
                              "w": 328
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 342,
                              "y": 272,
                              "h": 46,
                              "w": 358
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 704,
                              "y": 333,
                              "h": 44,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 499,
                              "h": 52,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 110,
                              "y": 501,
                              "h": 51,
                              "w": 151
                        }
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 771,
                              "y": 494,
                              "h": 86,
                              "w": 279
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 42,
                              "y": 564,
                              "h": 144,
                              "w": 1033
                        }
                  }
            }
      }
}
config_ios = {
    "792_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 853,
                  "w": 1329
            },
            "ref": {
                  "x": 320,
                  "y": 150,
                  "h": 140,
                  "w": 140
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 25.0,
                              "y": 30.0,
                              "h": 165.0,
                              "w": 125.0
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 5,
                              "y": 200,
                              "h": 40,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 150,
                              "y": 125,
                              "h": 40,
                              "w": 185
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 150,
                              "y": 150,
                              "h": 40,
                              "w": 180
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 150,
                              "y": 90,
                              "h": 40,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 150,
                              "y": 50,
                              "h": 35,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": "[A-Z0-9]{9}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 150,
                              "y": 25,
                              "h": 40,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  # "7": {
                  #       "name": "gender",
                  #       "type": 0,
                  #       "points": {
                  #             "x": 785,
                  #             "y": 518,
                  #             "h": 66,
                  #             "w": 223
                  #       },
                  #       "ocr_type": 1, "regex": "[EK]\\/[MF]"
                  # }
            }
      },
    "792_id_front_test": {
        "initial": {
            "x": 0,
            "y": 0,
            "h": 662,
            "w": 1047
        },
        "ref": {
            "x": 680,
            "y": 126,
            "h": 221,
            "w": 336
        },
        "threshold": 0.65,
        "fields": {
            "0": {
                "name": "photo",
                "type": 1,
                "points": {
                    "x": 64.0,
                    "y": 234.0,
                    "h": 349.0,
                    "w": 261.0
                }
            },
            "1": {
                "name": "identity_number",
                "type": 0,
                "points": {
                    "x": 57,
                    "y": 175,
                    "h": 57,
                    "w": 325
                },
                "ocr_type": 1, "regex": "[0-9]{11}"
            },
            "2": {
                "name": "name",
                "type": 0,
                "points": {
                    "x": 335,
                    "y": 349,
                    "h": 56,
                    "w": 420
                },
                "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
            },
            "3": {
                "name": "surname",
                "type": 0,
                "points": {
                    "x": 346,
                    "y": 272,
                    "h": 58,
                    "w": 333
                },
                "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
            },
            "4": {
                "name": "birth_date",
                "type": 0,
                "points": {
                    "x": 334,
                    "y": 420,
                    "h": 55,
                    "w": 232
                },
                "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
            },
            "5": {
                "name": "serial_number",
                "type": 0,
                "points": {
                    "x": 346,
                    "y": 494,
                    "h": 52,
                    "w": 221
                },
                "ocr_type": 1, "regex": "[A-Z0-9]{9}"
            },
            "6": {
                "name": "expiry_date",
                "type": 0,
                "points": {
                    "x": 347,
                    "y": 559,
                    "h": 58,
                    "w": 215
                },
                "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
            },
            "7": {
                  "name": "gender",
                  "type": 0,
                  "points": {
                        "x": 626,
                        "y": 419,
                        "h": 59,
                        "w": 122
                  },
                  "ocr_type": 1, "regex": "[EK]\\s/\\s[MF]"
            }
        }
    },
    "792_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 857,
                  "w": 1398
            },
            "ref": {
                  "x": 10,
                  "y": 265,
                  "h": 35,
                  "w": 180
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "mother_name",
                        "type": 0,
                        "points": {
                              "x": 110,
                              "y": 210,
                              "h": 40,
                              "w": 180
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "1": {
                        "name": "father_name",
                        "type": 0,
                        "points": {
                              "x": 110,
                              "y": 175,
                              "h": 40,
                              "w": 180
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "2": {
                        "name": "mrz",
                        "mrz_type": "td1",
                        "type": 2,
                        "points": {
                              "x": 10,
                              "y": 10,
                              "h": 110,
                              "w": 460
                        },
                        "check_mrz": True
                  }
            }
      },
    "792_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 768,
                  "w": 1024
            },
            "ref": {
                  "x": 285,
                  "y": 255,
                  "h": 50,
                  "w": 60
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 5,
                              "y": 90,
                              "h": 170,
                              "w": 240
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 180,
                              "h": 20,
                              "w": 80
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 145,
                              "y": 245,
                              "h": 20,
                              "w": 80
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 145,
                              "y": 260,
                              "h": 20,
                              "w": 80
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 145,
                              "y": 140,
                              "h": 20,
                              "w": 100
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 350,
                              "y": 280,
                              "h": 20,
                              "w": 80
                        },
                        "ocr_type": 1, "regex": "([0-9A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 145,
                              "y": 90,
                              "h": 20,
                              "w": 100
                        },
                        "ocr_type": 1, "regex": "([0-9]+\\s{1,2}[A-Z]{3})\\/([A-Z]{3})\\s[0-9]{4}"
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 350,
                              "y": 210,
                              "h": 20,
                              "w": 80
                        },
                        "ocr_type": 1, "regex": "[EK]\\/[MF]"
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 270,
                              "y": 80,
                              "h": 60,
                              "w": 120
                        }
                  },
                  "9": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 10,
                              "y": 15,
                              "h": 60,
                              "w": 465
                        },
                        "check_mrz": True
                  }
            }
      },
    "792_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1134,
                  "w": 2016
            },
            "ref": {
                  "x": 260,
                  "y": 240,
                  "h": 60,
                  "w": 250
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 10,
                              "y": 55,
                              "h": 190,
                              "w": 150
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 350,
                              "y": 120,
                              "h": 30,
                              "w": 120
                        },
                        "ocr_type": 1, "regex": "[0-9]{11}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 185,
                              "y": 190,
                              "h": 30,
                              "w": 150
                        },
                        "ocr_type": 0, "regex": "([A-Za-zĞÇŞÜÖİğçşüöı]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 185,
                              "y": 220,
                              "h": 30,
                              "w": 150
                        },
                        "ocr_type": 0, "regex": "([A-ZĞÇŞÜÖİ]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 185,
                              "y": 170,
                              "h": 30,
                              "w": 110
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 190,
                              "y": 120,
                              "h": 30,
                              "w": 110
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "licence_number",
                        "type": 0,
                        "points": {
                              "x": 190,
                              "y": 95,
                              "h": 30,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": "([0-9]){1,}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 190,
                              "y": 50,
                              "h": 50,
                              "w": 150
                        }
                  },
                  "8": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 35,
                              "y": 30,
                              "h": 30,
                              "w": 90
                        }
                  }
            }
      },
    "792_driving_licence_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 813,
                  "w": 1280
            },
            "ref": {
                  "x": 100,
                  "y": 25,
                  "h": 300,
                  "w": 110
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "blood_type",
                        "type": 3,
                        "points": {
                              "x": 35,
                              "y": 275,
                              "h": 20,
                              "w": 70
                        }
                  },
                  "1": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 100,
                              "y": 25,
                              "h": 300,
                              "w": 325
                        }
                  }
            }
      },
    "31_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1085,
                  "w": 1675
            },
            "ref": {
                  "x": 330,
                  "y": 49,
                  "h": 59,
                  "w": 281
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 77,
                              "y": 155,
                              "h": 621,
                              "w": 509
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 1080,
                              "y": 725,
                              "h": 102,
                              "w": 269
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 589,
                              "y": 352,
                              "h": 79,
                              "w": 681
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 599,
                              "y": 215,
                              "h": 91,
                              "w": 697
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 1195,
                              "y": 600,
                              "h": 90,
                              "w": 353
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 725,
                              "h": 97,
                              "w": 377
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 599,
                              "y": 853,
                              "h": 115,
                              "w": 323
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 601,
                              "y": 595,
                              "h": 90,
                              "w": 147
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 1077,
                              "y": 861,
                              "h": 160,
                              "w": 519
                        }
                  }
            }
      },
    "31_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 732,
                  "w": 1040
            },
            "ref": {
                  "x": 208,
                  "y": 64,
                  "h": 51,
                  "w": 95
            },
            "threshold": 0.76,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 50,
                              "y": 115,
                              "h": 317,
                              "w": 250
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 500,
                              "y": 342,
                              "h": 40,
                              "w": 200
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 245,
                              "h": 40,
                              "w": 238
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 305,
                              "y": 132,
                              "h": 70,
                              "w": 249
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 311,
                              "y": 340,
                              "h": 40,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 660,
                              "y": 85,
                              "h": 35,
                              "w": 202
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 435,
                              "h": 42,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 733,
                              "y": 342,
                              "h": 34,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 737,
                              "y": 443,
                              "h": 100,
                              "w": 249
                        }
                  },
                  "9": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 40,
                              "y": 574,
                              "h": 118,
                              "w": 960
                        },
                        "check_mrz": True
                  }
            }
      },
    "250_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 652,
                  "w": 1024
            },
            "ref": {
                  "x": 62,
                  "y": 33,
                  "h": 113,
                  "w": 184
            },
            "threshold": 0.83,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 67,
                              "y": 143,
                              "h": 452,
                              "w": 325
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 400,
                              "y": 234,
                              "h": 37,
                              "w": 374
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "alternative_name",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 418,
                              "h": 41,
                              "w": 346
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 317,
                              "h": 31,
                              "w": 166
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 476,
                              "h": 42,
                              "w": 283
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 470,
                              "h": 27,
                              "w": 182
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 317,
                              "h": 38,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 446,
                              "y": 516,
                              "h": 81,
                              "w": 256
                        }
                  }
            }
      },
    "276_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 525,
                  "w": 834
            },
            "ref": {
                  "x": 31,
                  "y": 15,
                  "h": 79,
                  "w": 221
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 33,
                              "y": 105,
                              "h": 402,
                              "w": 314
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 364,
                              "y": 219,
                              "h": 35,
                              "w": 248
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 361,
                              "y": 136,
                              "h": 62,
                              "w": 319
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 293,
                              "h": 30,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 577,
                              "y": 20,
                              "h": 48,
                              "w": 228
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 409,
                              "h": 35,
                              "w": 168
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "nationality",
                        "type": 0,
                        "points": {
                              "x": 546,
                              "y": 289,
                              "h": 38,
                              "w": 226
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 354,
                              "y": 436,
                              "h": 78,
                              "w": 253
                        }
                  }
            }
      },
    "276_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 678,
                  "w": 958
            },
            "ref": {
                  "x": 341,
                  "y": 14,
                  "h": 30,
                  "w": 189
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 40,
                              "y": 111,
                              "h": 337,
                              "w": 261
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 332,
                              "y": 122,
                              "h": 34,
                              "w": 140
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 311,
                              "y": 148,
                              "h": 33,
                              "w": 155
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 323,
                              "y": 267,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 605,
                              "y": 72,
                              "h": 34,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 519,
                              "y": 273,
                              "h": 32,
                              "w": 58
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 524,
                              "y": 377,
                              "h": 38,
                              "w": 147
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 688,
                              "y": 392,
                              "h": 90,
                              "w": 255
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 14,
                              "y": 517,
                              "h": 121,
                              "w": 926
                        },
                        "ocr_type": 2,
                        "check_mrz": True
                  }
            }
      },
    "40_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 387,
                  "w": 619
            },
            "ref": {
                  "x": 368,
                  "y": 9,
                  "h": 57,
                  "w": 180
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 28,
                              "y": 93,
                              "h": 262,
                              "w": 193
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 114,
                              "h": 24,
                              "w": 204
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 242,
                              "y": 92,
                              "h": 24,
                              "w": 213
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 284,
                              "h": 28,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 241,
                              "y": 202,
                              "h": 23,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 247,
                              "h": 24,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 238,
                              "y": 322,
                              "h": 30,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 479,
                              "y": 275,
                              "h": 38,
                              "w": 132
                        }
                  }
            }
      },
    "56_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 466,
                  "w": 737
            },
            "ref": {
                  "x": 504,
                  "y": 5,
                  "h": 61,
                  "w": 136
            },
            "threshold": 0.81,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 25,
                              "y": 160,
                              "h": 286,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 18,
                              "y": 86,
                              "h": 25,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 20,
                              "y": 123,
                              "h": 26,
                              "w": 252
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 564,
                              "y": 191,
                              "h": 25,
                              "w": 122
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 289,
                              "h": 27,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 338,
                              "h": 29,
                              "w": 121
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 268,
                              "y": 190,
                              "h": 29,
                              "w": 54
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 330,
                              "y": 371,
                              "h": 81,
                              "w": 227
                        }
                  }
            }
      },
    "100_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 378,
                  "w": 598
            },
            "ref": {
                  "x": 366,
                  "y": 33,
                  "h": 38,
                  "w": 210
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 33,
                              "y": 94,
                              "h": 198,
                              "w": 151
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 318,
                              "y": 206,
                              "h": 24,
                              "w": 107
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 279,
                              "y": 147,
                              "h": 21,
                              "w": 167
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 277,
                              "y": 105,
                              "h": 22,
                              "w": 186
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 250,
                              "h": 20,
                              "w": 90
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 446,
                              "y": 287,
                              "h": 28,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 368,
                              "y": 270,
                              "h": 18,
                              "w": 92
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 499,
                              "y": 207,
                              "h": 25,
                              "w": 39
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 437,
                              "y": 319,
                              "h": 49,
                              "w": 139
                        }
                  }
            }
      },
    "191_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 379,
                  "w": 600
            },
            "ref": {
                  "x": 153,
                  "y": 31,
                  "h": 45,
                  "w": 175
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 23,
                              "y": 111,
                              "h": 252,
                              "w": 188
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 228,
                              "y": 258,
                              "h": 25,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 229,
                              "y": 147,
                              "h": 20,
                              "w": 171
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 229,
                              "y": 96,
                              "h": 28,
                              "w": 222
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 444,
                              "y": 205,
                              "h": 27,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 444,
                              "y": 255,
                              "h": 24,
                              "w": 132
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 228,
                              "y": 204,
                              "h": 28,
                              "w": 51
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 242,
                              "y": 306,
                              "h": 62,
                              "w": 165
                        }
                  }
            }
      },
    "233_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 603,
                  "w": 954
            },
            "ref": {
                  "x": 64,
                  "y": 56,
                  "h": 37,
                  "w": 237
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 65,
                              "y": 100,
                              "h": 391,
                              "w": 333
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 716,
                              "y": 351,
                              "h": 55,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 166,
                              "h": 41,
                              "w": 223
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 118,
                              "h": 43,
                              "w": 269
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 713,
                              "y": 296,
                              "h": 43,
                              "w": 178
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 394,
                              "y": 401,
                              "h": 45,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 394,
                              "y": 350,
                              "h": 39,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 613,
                              "y": 246,
                              "h": 34,
                              "w": 60
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 442,
                              "y": 510,
                              "h": 66,
                              "w": 182
                        }
                  }
            }
      },
    "348_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 648,
                  "w": 1022
            },
            "ref": {
                  "x": 902,
                  "y": 37,
                  "h": 165,
                  "w": 94
            },
            "threshold": 0.81,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 42,
                              "y": 143,
                              "h": 451,
                              "w": 329
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 426,
                              "y": 169,
                              "h": 45,
                              "w": 226
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 654,
                              "y": 171,
                              "h": 40,
                              "w": 213
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 780,
                              "y": 310,
                              "h": 36,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 806,
                              "y": 380,
                              "h": 47,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 777,
                              "y": 342,
                              "h": 40,
                              "w": 231
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 521,
                              "y": 274,
                              "h": 41,
                              "w": 64
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 446,
                              "y": 532,
                              "h": 69,
                              "w": 296
                        }
                  }
            }
      },
    "368_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 751,
                  "w": 1105
            },
            "ref": {
                  "x": 18,
                  "y": 33,
                  "h": 42,
                  "w": 305
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 13,
                              "y": 158,
                              "h": 376,
                              "w": 291
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 314,
                              "y": 196,
                              "h": 41,
                              "w": 481
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 310,
                              "y": 249,
                              "h": 32,
                              "w": 261
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 561,
                              "y": 315,
                              "h": 36,
                              "w": 182
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 841,
                              "y": 135,
                              "h": 32,
                              "w": 218
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 303,
                              "y": 468,
                              "h": 37,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 307,
                              "y": 303,
                              "h": 52,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 10,
                              "y": 622,
                              "h": 103,
                              "w": 1073
                        },
                        "check_mrz": True
                  }
            }
      },
    "438_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 642,
                  "w": 1024
            },
            "ref": {
                  "x": 308,
                  "y": 105,
                  "h": 48,
                  "w": 319
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 80,
                              "y": 215,
                              "h": 342,
                              "w": 266
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 42,
                              "h": 44,
                              "w": 247
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 389,
                              "y": 420,
                              "h": 43,
                              "w": 326
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 390,
                              "y": 310,
                              "h": 41,
                              "w": 398
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 533,
                              "h": 48,
                              "w": 189
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 663,
                              "y": 496,
                              "h": 106,
                              "w": 332
                        }
                  }
            }
      },
    "616_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 646,
                  "w": 1024
            },
            "ref": {
                  "x": 172,
                  "y": 22,
                  "h": 45,
                  "w": 374
            },
            "threshold": 0.55,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 50,
                              "y": 182,
                              "h": 417,
                              "w": 289
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 232,
                              "h": 43,
                              "w": 302
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 153,
                              "h": 47,
                              "w": 338
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 307,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 395,
                              "h": 39,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 460,
                              "h": 35,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 690,
                              "y": 392,
                              "h": 34,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 373,
                              "y": 528,
                              "h": 83,
                              "w": 391
                        }
                  }
            }
      },
    "620_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 645,
                  "w": 946
            },
            "ref": {
                  "x": 572,
                  "y": 45,
                  "h": 84,
                  "w": 353
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 701,
                              "y": 294,
                              "h": 296,
                              "w": 207
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 284,
                              "y": 432,
                              "h": 43,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 264,
                              "y": 248,
                              "h": 44,
                              "w": 327
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 268,
                              "y": 157,
                              "h": 44,
                              "w": 411
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 345,
                              "h": 41,
                              "w": 139
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 455,
                              "y": 422,
                              "h": 51,
                              "w": 76
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 435,
                              "h": 37,
                              "w": 138
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 260,
                              "y": 515,
                              "h": 74,
                              "w": 415
                        }
                  },
                  "8": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 262,
                              "y": 342,
                              "h": 40,
                              "w": 46
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "642_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 633,
                  "w": 1021
            },
            "ref": {
                  "x": 160,
                  "y": 33,
                  "h": 96,
                  "w": 305
            },
            "threshold": 0.82,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 32,
                              "y": 133,
                              "h": 476,
                              "w": 348
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 407,
                              "y": 362,
                              "h": 38,
                              "w": 270
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 401,
                              "y": 201,
                              "h": 71,
                              "w": 302
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 403,
                              "y": 136,
                              "h": 42,
                              "w": 334
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 775,
                              "y": 299,
                              "h": 35,
                              "w": 220
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 405,
                              "y": 431,
                              "h": 33,
                              "w": 194
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 777,
                              "y": 429,
                              "h": 40,
                              "w": 211
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 402,
                              "y": 295,
                              "h": 40,
                              "w": 52
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 470,
                              "y": 511,
                              "h": 97,
                              "w": 355
                        }
                  }
            }
      },
    "642_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 874,
                  "w": 1333
            },
            "ref": {
                  "x": 1051,
                  "y": 56,
                  "h": 83,
                  "w": 217
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 84,
                              "y": 256,
                              "h": 310,
                              "w": 264
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 730,
                              "y": 344,
                              "h": 63,
                              "w": 244
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 177,
                              "h": 51,
                              "w": 338
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 117,
                              "h": 63,
                              "w": 355
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 225,
                              "h": 69,
                              "w": 411
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 389,
                              "h": 64,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 471,
                              "y": 337,
                              "h": 54,
                              "w": 188
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 119,
                              "y": 674,
                              "h": 76,
                              "w": 537
                        }
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 571,
                              "y": 466,
                              "h": 139,
                              "w": 279
                        }
                  }
            }
      },
    "703_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 500,
                  "w": 765
            },
            "ref": {
                  "x": 99,
                  "y": 36,
                  "h": 40,
                  "w": 319
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 38,
                              "y": 110,
                              "h": 284,
                              "w": 209
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 234,
                              "h": 35,
                              "w": 181
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 261,
                              "y": 146,
                              "h": 31,
                              "w": 253
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 264,
                              "y": 103,
                              "h": 29,
                              "w": 286
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 192,
                              "h": 29,
                              "w": 153
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 262,
                              "y": 295,
                              "h": 38,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 533,
                              "y": 322,
                              "h": 31,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 263,
                              "y": 235,
                              "h": 29,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 441,
                              "y": 393,
                              "h": 81,
                              "w": 286
                        }
                  }
            }
      },
    "724_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 865,
                  "w": 1536
            },
            "ref": {
                  "x": 261,
                  "y": 53,
                  "h": 109,
                  "w": 475
            },
            "threshold": 0.84,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 45,
                              "y": 229,
                              "h": 587,
                              "w": 537
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 153,
                              "h": 85,
                              "w": 573
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 597,
                              "y": 371,
                              "h": 53,
                              "w": 441
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 601,
                              "y": 253,
                              "h": 93,
                              "w": 479
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 1203,
                              "y": 447,
                              "h": 51,
                              "w": 289
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 603,
                              "y": 603,
                              "h": 55,
                              "w": 333
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 897,
                              "y": 525,
                              "h": 57,
                              "w": 289
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 591,
                              "y": 449,
                              "h": 51,
                              "w": 81
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 647,
                              "y": 651,
                              "h": 127,
                              "w": 527
                        }
                  }
            }
      },
    "578_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 578,
                  "w": 906
            },
            "ref": {
                  "x": 24,
                  "y": 20,
                  "h": 61,
                  "w": 199
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 41,
                              "y": 106,
                              "h": 433,
                              "w": 327
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 376,
                              "y": 136,
                              "h": 36,
                              "w": 380
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 90,
                              "h": 35,
                              "w": 325
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 377,
                              "y": 255,
                              "h": 39,
                              "w": 239
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 377,
                              "y": 325,
                              "h": 36,
                              "w": 230
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 378,
                              "y": 397,
                              "h": 32,
                              "w": 240
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 184,
                              "h": 35,
                              "w": 31
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 382,
                              "y": 455,
                              "h": 80,
                              "w": 256
                        }
                  }
            }
      },
    "470_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 715,
                  "w": 1169
            },
            "ref": {
                  "x": 252,
                  "y": 67,
                  "h": 64,
                  "w": 373
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 61,
                              "y": 231,
                              "h": 386,
                              "w": 285
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 906,
                              "y": 196,
                              "h": 50,
                              "w": 197
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 266,
                              "h": 52,
                              "w": 317
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 231,
                              "h": 43,
                              "w": 347
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 794,
                              "y": 407,
                              "h": 39,
                              "w": 240
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 800,
                              "y": 455,
                              "h": 45,
                              "w": 203
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 528,
                              "h": 43,
                              "w": 239
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 370,
                              "y": 408,
                              "h": 40,
                              "w": 62
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 377,
                              "y": 590,
                              "h": 89,
                              "w": 381
                        }
                  }
            }
      },
    "380_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 386,
                  "w": 600
            },
            "ref": {
                  "x": 117,
                  "y": 22,
                  "h": 47,
                  "w": 288
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 29,
                              "y": 125,
                              "h": 205,
                              "w": 164
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 201,
                              "y": 163,
                              "h": 15,
                              "w": 179
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 202,
                              "y": 132,
                              "h": 17,
                              "w": 171
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 479,
                              "y": 192,
                              "h": 25,
                              "w": 73
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 443,
                              "y": 20,
                              "h": 38,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 396,
                              "y": 265,
                              "h": 19,
                              "w": 74
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 201,
                              "y": 234,
                              "h": 20,
                              "w": 23
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 227,
                              "y": 309,
                              "h": 36,
                              "w": 101
                        }
                  }
            }
      },
    "246_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 646,
                  "w": 1024
            },
            "ref": {
                  "x": 38,
                  "y": 23,
                  "h": 77,
                  "w": 459
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 55,
                              "y": 142,
                              "h": 346,
                              "w": 268
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 255,
                              "h": 44,
                              "w": 246
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 162,
                              "h": 38,
                              "w": 307
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 415,
                              "h": 43,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 730,
                              "y": 417,
                              "h": 38,
                              "w": 187
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 726,
                              "y": 478,
                              "h": 39,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 492,
                              "y": 356,
                              "h": 39,
                              "w": 38
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 37,
                              "y": 526,
                              "h": 70,
                              "w": 424
                        }
                  }
            }
      },
    "203_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 336,
                  "w": 532
            },
            "ref": {
                  "x": 22,
                  "y": 12,
                  "h": 63,
                  "w": 96
            },
            "threshold": 0.83,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 126,
                              "h": 181,
                              "w": 126
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 121,
                              "y": 71,
                              "h": 14,
                              "w": 173
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 130,
                              "y": 90,
                              "h": 15,
                              "w": 175
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 184,
                              "y": 119,
                              "h": 25,
                              "w": 166
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 372,
                              "y": 42,
                              "h": 23,
                              "w": 140
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 180,
                              "y": 287,
                              "h": 30,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 123,
                              "h": 48,
                              "w": 72
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 331,
                              "y": 245,
                              "h": 56,
                              "w": 164
                        }
                  }
            }
      },
    "440_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 645,
                  "w": 1024
            },
            "ref": {
                  "x": 25,
                  "y": 23,
                  "h": 108,
                  "w": 307
            },
            "threshold": 0.84,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 34,
                              "y": 175,
                              "h": 436,
                              "w": 317
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 540,
                              "y": 417,
                              "h": 37,
                              "w": 185
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 373,
                              "y": 260,
                              "h": 40,
                              "w": 328
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 375,
                              "y": 166,
                              "h": 38,
                              "w": 384
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 788,
                              "y": 415,
                              "h": 38,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 539,
                              "y": 480,
                              "h": 37,
                              "w": 156
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 788,
                              "y": 480,
                              "h": 45,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 374,
                              "y": 350,
                              "h": 32,
                              "w": 102
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 378,
                              "y": 538,
                              "h": 81,
                              "w": 336
                        }
                  }
            }
      },
    "428_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 338,
                  "w": 544
            },
            "ref": {
                  "x": 11,
                  "y": 9,
                  "h": 21,
                  "w": 172
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 18,
                              "y": 57,
                              "h": 242,
                              "w": 183
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 320,
                              "y": 171,
                              "h": 30,
                              "w": 151
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 107,
                              "h": 19,
                              "w": 150
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 56,
                              "h": 23,
                              "w": 165
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 215,
                              "h": 22,
                              "w": 99
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 420,
                              "y": 5,
                              "h": 23,
                              "w": 104
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 200,
                              "y": 255,
                              "h": 20,
                              "w": 105
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 205,
                              "y": 290,
                              "h": 41,
                              "w": 127
                        }
                  }
            }
      },
    "804_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 571,
                  "w": 911
            },
            "ref": {
                  "x": 474,
                  "y": 20,
                  "h": 102,
                  "w": 383
            },
            "threshold": 0.73,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 136,
                              "h": 400,
                              "w": 312
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 626,
                              "y": 401,
                              "h": 42,
                              "w": 238
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 378,
                              "y": 205,
                              "h": 67,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 121,
                              "h": 67,
                              "w": 312
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 383,
                              "y": 402,
                              "h": 40,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 620,
                              "y": 457,
                              "h": 42,
                              "w": 171
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 385,
                              "y": 460,
                              "h": 40,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 346,
                              "h": 39,
                              "w": 78
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 471,
                              "y": 497,
                              "h": 61,
                              "w": 234
                        }
                  }
            }
      },
    "826_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 600,
                  "w": 1200
            },
            "ref": {
                  "x": 884,
                  "y": 147,
                  "h": 201,
                  "w": 286
            },
            "threshold": 0.59,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 37,
                              "y": 216,
                              "h": 351,
                              "w": 391
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 196,
                              "y": 160,
                              "h": 49,
                              "w": 424
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 195,
                              "y": 116,
                              "h": 47,
                              "w": 425
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 429,
                              "y": 374,
                              "h": 52,
                              "w": 285
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 433,
                              "y": 508,
                              "h": 52,
                              "w": 228
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 430,
                              "y": 313,
                              "h": 46,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 828,
                              "y": 477,
                              "h": 83,
                              "w": 325
                        }
                  }
            }
      },
    "826_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 590,
                  "w": 845
            },
            "ref": {
                  "x": 101,
                  "y": 6,
                  "h": 39,
                  "w": 185
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 62,
                              "y": 114,
                              "h": 268,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 530,
                              "y": 75,
                              "h": 36,
                              "w": 149
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 292,
                              "y": 157,
                              "h": 33,
                              "w": 333
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 116,
                              "h": 35,
                              "w": 333
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 237,
                              "h": 33,
                              "w": 238
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 287,
                              "y": 356,
                              "h": 34,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 430,
                              "y": 313,
                              "h": 46,
                              "w": 68
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 529,
                              "y": 368,
                              "h": 63,
                              "w": 223
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 27,
                              "y": 439,
                              "h": 115,
                              "w": 773
                        },
                        "ocr_type": 1, "regex": "",
                        "check_mrz": True
                  }
            }
      },
    "784_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 585,
                  "w": 909
            },
            "ref": {
                  "x": 9,
                  "y": 18,
                  "h": 43,
                  "w": 367
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 45,
                              "y": 127,
                              "h": 269,
                              "w": 219
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 308,
                              "y": 172,
                              "h": 58,
                              "w": 279
                        },
                        "ocr_type": 1, "regex": "[0-9]{3}\\-[0-9]{4}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 351,
                              "y": 249,
                              "h": 56,
                              "w": 348
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 483,
                              "y": 286,
                              "h": 66,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 336,
                              "y": 500,
                              "h": 63,
                              "w": 178
                        },
                        "ocr_type": 1,
                        "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 809,
                              "y": 485,
                              "h": 66,
                              "w": 74
                        },
                        "ocr_type": 1,
                        "regex": "[MF]{1}"
                  },
                  "6": {
                        "name": "nationality",
                        "type": 0,
                        "points": {
                              "x": 394,
                              "y": 378,
                              "h": 50,
                              "w": 238
                        },
                        "regex": "([A-Za-z]+\\s?){1,}",
                        "ocr_type": 1
                  }
            }
      },
    "756_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 163,
                  "y": 81,
                  "h": 132,
                  "w": 350
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 177,
                              "y": 251,
                              "h": 336,
                              "w": 267
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 810,
                              "y": 244,
                              "h": 54,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 463,
                              "y": 435,
                              "h": 38,
                              "w": 277
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 340,
                              "h": 66,
                              "w": 387
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 466,
                              "y": 559,
                              "h": 49,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 752,
                              "y": 487,
                              "h": 71,
                              "w": 246
                        }
                  }
            }
      },
    "710_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 161,
                  "y": 99,
                  "h": 82,
                  "w": 406
            },
            "threshold": 0.77,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 736,
                              "y": 179,
                              "h": 326,
                              "w": 275
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 432,
                              "h": 31,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 276,
                              "h": 30,
                              "w": 276
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 355,
                              "y": 223,
                              "h": 32,
                              "w": 347
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 485,
                              "h": 32,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 326,
                              "h": 35,
                              "w": 44
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 798,
                              "y": 548,
                              "h": 61,
                              "w": 242
                        }
                  }
            }
      },
    "705_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 351,
                  "y": 103,
                  "h": 106,
                  "w": 302
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 148,
                              "y": 246,
                              "h": 343,
                              "w": 294
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 770,
                              "y": 165,
                              "h": 50,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 416,
                              "h": 44,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 336,
                              "h": 61,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 493,
                              "h": 39,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 562,
                              "h": 42,
                              "w": 175
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 468,
                              "y": 494,
                              "h": 40,
                              "w": 34
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 725,
                              "y": 510,
                              "h": 79,
                              "w": 280
                        }
                  }
            }
      },
    "528_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 665,
                  "w": 1142
            },
            "ref": {
                  "x": 108,
                  "y": 53,
                  "h": 69,
                  "w": 303
            },
            "threshold": 0.62,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 124,
                              "y": 133,
                              "h": 343,
                              "w": 235
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 420,
                              "y": 259,
                              "h": 37,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 418,
                              "y": 210,
                              "h": 35,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 419,
                              "y": 364,
                              "h": 36,
                              "w": 305
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 782,
                              "y": 158,
                              "h": 36,
                              "w": 194
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 415,
                              "y": 462,
                              "h": 40,
                              "w": 272
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 415,
                              "y": 310,
                              "h": 37,
                              "w": 69
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 117,
                              "y": 498,
                              "h": 73,
                              "w": 263
                        }
                  }
            }
      },
    "442_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 911,
                  "y": 419,
                  "h": 186,
                  "w": 104
            },
            "threshold": 0.9,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 169,
                              "y": 201,
                              "h": 324,
                              "w": 258
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 328,
                              "h": 40,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 469,
                              "y": 236,
                              "h": 38,
                              "w": 277
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 473,
                              "y": 449,
                              "h": 37,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 465,
                              "y": 508,
                              "h": 42,
                              "w": 221
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 472,
                              "y": 572,
                              "h": 50,
                              "w": 164
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 464,
                              "y": 388,
                              "h": 44,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 167,
                              "y": 530,
                              "h": 54,
                              "w": 272
                        }
                  }
            }
      },
    "417_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 142,
                  "y": 72,
                  "h": 102,
                  "w": 358
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 175,
                              "y": 216,
                              "h": 346,
                              "w": 244
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 751,
                              "y": 509,
                              "h": 38,
                              "w": 183
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 469,
                              "y": 274,
                              "h": 59,
                              "w": 317
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 470,
                              "y": 201,
                              "h": 62,
                              "w": 360
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 472,
                              "y": 495,
                              "h": 37,
                              "w": 159
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 753,
                              "y": 576,
                              "h": 36,
                              "w": 154
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 473,
                              "y": 393,
                              "h": 42,
                              "w": 90
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 472,
                              "y": 551,
                              "h": 65,
                              "w": 246
                        }
                  }
            }
      },
    "268_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 132,
                  "y": 94,
                  "h": 86,
                  "w": 310
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 165,
                              "y": 209,
                              "h": 358,
                              "w": 262
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 715,
                              "y": 445,
                              "h": 40,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 447,
                              "y": 287,
                              "h": 38,
                              "w": 262
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 454,
                              "y": 352,
                              "h": 34,
                              "w": 247
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 451,
                              "y": 525,
                              "h": 40,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 202,
                              "y": 585,
                              "h": 44,
                              "w": 212
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 665,
                              "y": 520,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 600,
                              "y": 451,
                              "h": 35,
                              "w": 103
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 706,
                              "y": 573,
                              "h": 76,
                              "w": 254
                        }
                  }
            }
      },
    "8_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 653,
                  "w": 1040
            },
            "ref": {
                  "x": 330,
                  "y": 17,
                  "h": 33,
                  "w": 361
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 82,
                              "y": 111,
                              "h": 305,
                              "w": 223
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 685,
                              "y": 459,
                              "h": 47,
                              "w": 232
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 327,
                              "y": 171,
                              "h": 41,
                              "w": 282
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 326,
                              "y": 113,
                              "h": 43,
                              "w": 303
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 328,
                              "y": 345,
                              "h": 39,
                              "w": 195
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 688,
                              "y": 229,
                              "h": 47,
                              "w": 204
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 684,
                              "y": 402,
                              "h": 41,
                              "w": 258
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 684,
                              "y": 345,
                              "h": 39,
                              "w": 56
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 59,
                              "y": 460,
                              "h": 73,
                              "w": 251
                        }
                  }
            }
      },
    "752_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 622,
                  "w": 1024
            },
            "ref": {
                  "x": 66,
                  "y": 18,
                  "h": 94,
                  "w": 309
            },
            "threshold": 0.67,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 55,
                              "y": 152,
                              "h": 406,
                              "w": 295
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 390,
                              "y": 284,
                              "h": 34,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 171,
                              "h": 37,
                              "w": 306
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 392,
                              "y": 113,
                              "h": 35,
                              "w": 443
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 740,
                              "y": 227,
                              "h": 37,
                              "w": 243
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 486,
                              "y": 337,
                              "h": 35,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 484,
                              "y": 411,
                              "h": 39,
                              "w": 233
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 389,
                              "y": 227,
                              "h": 37,
                              "w": 59
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 682,
                              "y": 513,
                              "h": 96,
                              "w": 334
                        }
                  }
            }
      },
    "840_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1010,
                  "w": 1521
            },
            "ref": {
                  "x": 506,
                  "y": 12,
                  "h": 89,
                  "w": 542
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 1069,
                              "y": 141,
                              "h": 61,
                              "w": 301
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "1": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 535,
                              "y": 200,
                              "h": 55,
                              "w": 445
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 535,
                              "y": 271,
                              "h": 59,
                              "w": 383
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 530,
                              "y": 412,
                              "h": 62,
                              "w": 227
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 526,
                              "y": 635,
                              "h": 65,
                              "w": 219
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 1208,
                              "y": 486,
                              "h": 65,
                              "w": 69
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 24,
                              "y": 823,
                              "h": 160,
                              "w": 1478
                        },
                        "check_mrz": True
                  },
                  "7": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 104,
                              "y": 206,
                              "h": 550,
                              "w": 380
                        }
                  }
            }
      },
    "586_nic_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 651,
                  "w": 1031
            },
            "ref": {
                  "x": 243,
                  "y": 33,
                  "h": 88,
                  "w": 265
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 726,
                              "y": 145,
                              "h": 325,
                              "w": 238
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 283,
                              "y": 472,
                              "h": 58,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 270,
                              "y": 130,
                              "h": 70,
                              "w": 431
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 281,
                              "y": 259,
                              "h": 70,
                              "w": 402
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 280,
                              "y": 391,
                              "h": 59,
                              "w": 100
                        },
                        "ocr_type": 1, "regex": "([FM]){1}"
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 520,
                              "y": 460,
                              "h": 60,
                              "w": 180
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 520,
                              "y": 535,
                              "h": 65,
                              "w": 180
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 740,
                              "y": 464,
                              "h": 108,
                              "w": 223
                        }
                  }
            }
      },
    "586_nic_id_front_test": {
        "initial": {
            "x": 0,
            "y": 0,
            "h": 733,
            "w": 1191
        },
        "ref": {
            "x": 79,
            "y": 14,
            "h": 195,
            "w": 186
        },
        "threshold": 0.7,
        "fields": {
            "0": {
                "name": "photo",
                "type": 1,
                "points": {
                    "x": 851,
                    "y": 219,
                    "h": 327,
                    "w": 268
                }
            },
            "1": {
                "name": "identity_number",
                "type": 0,
                "points": {
                    "x": 312,
                    "y": 561,
                    "h": 61,
                    "w": 302
                },
                "ocr_type": 1, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
            },
            "2": {
                "name": "name",
                "type": 0,
                "points": {
                    "x": 321,
                    "y": 169,
                    "h": 62,
                    "w": 590
                },
                "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
            },
            "3": {
                "name": "surname",
                "type": 0,
                "points": {
                    "x": 321,
                    "y": 318,
                    "h": 58,
                    "w": 529
                },
                "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
            },
            "4": {
                "name": "gender",
                "type": 0,
                "points": {
                    "x": 314,
                    "y": 466,
                    "h": 64,
                    "w": 119
                },
                "ocr_type": 1, "regex": "([FM]){1}"
            },
            "5": {
                "name": "birth_date",
                "type": 0,
                "points": {
                    "x": 622,
                    "y": 568,
                    "h": 48,
                    "w": 204
                },
                "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
            },
            "6": {
                "name": "expiry_date",
                "type": 0,
                "points": {
                    "x": 616,
                    "y": 649,
                    "h": 59,
                    "w": 188
                },
                "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
            },
            "7": {
                "name": "signature",
                "type": 3,
                "points": {
                    "x": 854,
                    "y": 544,
                    "h": 131,
                    "w": 260
                }
            }
        }
    },

    "586_nic_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 752,
                  "w": 1148
            },
            "ref": {
                  "x": 178,
                  "y": 41,
                  "h": 53,
                  "w": 313
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 40,
                              "y": 57,
                              "h": 130,
                              "w": 125
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 815,
                              "y": 40,
                              "h": 65,
                              "w": 270
                        },
                        "ocr_type": 0, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "present_address",
                        "type": 1,
                        "points": {
                              "x": 179,
                              "y": 81,
                              "h": 100,
                              "w": 664
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "3": {
                        "name": "permanent_address",
                        "type": 1,
                        "points": {
                              "x": 184,
                              "y": 238,
                              "h": 100,
                              "w": 635
                        },
                        "ocr_type": 0, "regex": "(.+\\s?){1,}"
                  },
                  "4": {
                        "name": "mrz",
                        "mrz_type": "",
                        "type": 2,
                        "points": {
                              "x": 25,
                              "y": 490,
                              "h": 220,
                              "w": 1050
                        },
                        "check_mrz": True
                  }
            }
      },
    "586_nicop_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 421,
                  "w": 669
            },
            "ref": {
                  "x": 161,
                  "y": 24,
                  "h": 46,
                  "w": 194
            },
            "threshold": 0.55,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 25,
                              "y": 68,
                              "h": 205,
                              "w": 168
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 255,
                              "y": 124,
                              "h": 40,
                              "w": 232
                        },
                        "ocr_type": 1, "regex": "[0-9]{6}\\-[0-9]{6}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 278,
                              "y": 163,
                              "h": 32,
                              "w": 221
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 338,
                              "y": 194,
                              "h": 29,
                              "w": 249
                        },
                        "ocr_type": 0, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 340,
                              "y": 223,
                              "h": 29,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": "([A-Za-z]+\\s?){1,}"
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 254,
                              "h": 25,
                              "w": 123
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 452,
                              "y": 306,
                              "h": 58,
                              "w": 204
                        }
                  }
            }
      },
    "586_nicop_id_back": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 638,
                  "w": 1024
            },
            "ref": {
                  "x": 225,
                  "y": 109,
                  "h": 54,
                  "w": 268
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 77,
                              "y": 191,
                              "h": 151,
                              "w": 130
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 956,
                              "y": 158,
                              "h": 267,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": "[0-9]{5}\\-[0-9]{7}\\-[0-9]{1}"
                  },
                  "2": {
                        "name": "present_address",
                        "type": 1,
                        "points": {
                              "x": 214,
                              "y": 142,
                              "h": 87,
                              "w": 589
                        },
                        "ocr_type": 0, "regex": "([-,/0-9A-Za-z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "permanent_address",
                        "type": 1,
                        "points": {
                              "x": 215,
                              "y": 258,
                              "h": 93,
                              "w": 583
                        },
                        "ocr_type": 0, "regex": "([-,/0-9A-Za-z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 876,
                              "y": 227,
                              "h": 199,
                              "w": 55
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\.[0-9]{1,2}\\.[0-9]{4}"
                  },
                  "5": {
                        "name": "mrz",
                        "mrz_type": "td1",
                        "type": 2,
                        "points": {
                              "x": 66,
                              "y": 441,
                              "h": 181,
                              "w": 923
                        },
                        "check_mrz": True
                  }
            }
      },
    "414_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 544,
                  "w": 1024
            },
            "ref": {
                  "x": 272,
                  "y": 101,
                  "h": 42,
                  "w": 523
            },
            "threshold": 0.45,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 143,
                              "y": 133,
                              "h": 249,
                              "w": 184
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 551,
                              "y": 142,
                              "h": 48,
                              "w": 246
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 305,
                              "h": 51,
                              "w": 462
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 363,
                              "y": 404,
                              "h": 44,
                              "w": 86
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 642,
                              "y": 469,
                              "h": 49,
                              "w": 143
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 311,
                              "y": 465,
                              "h": 45,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "196_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 460,
                  "w": 730
            },
            "ref": {
                  "x": 35,
                  "y": 12,
                  "h": 56,
                  "w": 352
            },
            "threshold": 0.64,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 39,
                              "y": 190,
                              "h": 241,
                              "w": 190
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 541,
                              "y": 32,
                              "h": 40,
                              "w": 176
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 28,
                              "y": 150,
                              "h": 39,
                              "w": 196
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 28,
                              "y": 91,
                              "h": 44,
                              "w": 226
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 435,
                              "y": 206,
                              "h": 39,
                              "w": 79
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 206,
                              "h": 42,
                              "w": 161
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 248,
                              "y": 341,
                              "h": 41,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 246,
                              "y": 397,
                              "h": 46,
                              "w": 162
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 501,
                              "y": 383,
                              "h": 64,
                              "w": 209
                        }
                  }
            }
      },
    "498_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 500,
                  "w": 780
            },
            "ref": {
                  "x": 140,
                  "y": 32,
                  "h": 39,
                  "w": 406
            },
            "threshold": 0.58,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 64,
                              "y": 131,
                              "h": 271,
                              "w": 209
                        }
                  },
                  "1": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 582,
                              "y": 48,
                              "h": 41,
                              "w": 160
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 291,
                              "y": 189,
                              "h": 32,
                              "w": 215
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 286,
                              "y": 142,
                              "h": 30,
                              "w": 253
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 538,
                              "y": 241,
                              "h": 30,
                              "w": 47
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 291,
                              "y": 286,
                              "h": 32,
                              "w": 146
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 289,
                              "y": 380,
                              "h": 33,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 163,
                              "y": 406,
                              "h": 69,
                              "w": 191
                        }
                  }
            }
      },
    "458_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 154,
                  "y": 68,
                  "h": 101,
                  "w": 496
            },
            "threshold": 0.48,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 727,
                              "y": 212,
                              "h": 349,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 124,
                              "y": 172,
                              "h": 56,
                              "w": 330
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 136,
                              "y": 427,
                              "h": 52,
                              "w": 400
                        },
                        "ocr_type": 0, "regex": ""
                  }
            }
      },
    "458_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 788,
                  "w": 1108
            },
            "ref": {
                  "x": 77,
                  "y": 54,
                  "h": 70,
                  "w": 241
            },
            "threshold": 0.48,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 74,
                              "y": 159,
                              "h": 343,
                              "w": 262
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 352,
                              "y": 186,
                              "h": 37,
                              "w": 210
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 703,
                              "y": 244,
                              "h": 40,
                              "w": 189
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "3": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 842,
                              "y": 113,
                              "h": 32,
                              "w": 153
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 354,
                              "y": 306,
                              "h": 37,
                              "w": 172
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 705,
                              "y": 427,
                              "h": 33,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 349,
                              "y": 365,
                              "h": 35,
                              "w": 77
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "524_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 634,
                  "w": 1024
            },
            "ref": {
                  "x": 51,
                  "y": 30,
                  "h": 86,
                  "w": 97
            },
            "threshold": 0.85,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 719,
                              "y": 141,
                              "h": 308,
                              "w": 228
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 62,
                              "y": 388,
                              "h": 54,
                              "w": 204
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 264,
                              "h": 68,
                              "w": 283
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 146,
                              "h": 80,
                              "w": 300
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 205,
                              "y": 143,
                              "h": 42,
                              "w": 61
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 481,
                              "y": 388,
                              "h": 45,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 689,
                              "y": 513,
                              "h": 91,
                              "w": 286
                        }
                  }
            }
      },
    "70_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 803,
                  "w": 1280
            },
            "ref": {
                  "x": 67,
                  "y": 21,
                  "h": 120,
                  "w": 376
            },
            "threshold": 0.75,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 72,
                              "y": 178,
                              "h": 496,
                              "w": 381
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 417,
                              "h": 80,
                              "w": 295
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 490,
                              "y": 221,
                              "h": 77,
                              "w": 424
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 121,
                              "y": 700,
                              "h": 49,
                              "w": 291
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 493,
                              "y": 541,
                              "h": 48,
                              "w": 108
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 496,
                              "y": 633,
                              "h": 44,
                              "w": 178
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 491,
                              "y": 715,
                              "h": 45,
                              "w": 183
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 804,
                              "y": 651,
                              "h": 88,
                              "w": 369
                        }
                  }
            }
      },
    "674_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 389,
                  "w": 614
            },
            "ref": {
                  "x": 212,
                  "y": 8,
                  "h": 63,
                  "w": 383
            },
            "threshold": 0.51,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 26,
                              "y": 154,
                              "h": 205,
                              "w": 172
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 208,
                              "y": 204,
                              "h": 48,
                              "w": 270
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 210,
                              "y": 138,
                              "h": 41,
                              "w": 267
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 204,
                              "y": 87,
                              "h": 31,
                              "w": 125
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 207,
                              "y": 272,
                              "h": 23,
                              "w": 202
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "608_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 684,
                  "w": 1072
            },
            "ref": {
                  "x": 88,
                  "y": 13,
                  "h": 155,
                  "w": 142
            },
            "threshold": 0.87,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 57,
                              "y": 271,
                              "h": 257,
                              "w": 232
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 20,
                              "y": 192,
                              "h": 67,
                              "w": 373
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 491,
                              "y": 332,
                              "h": 79,
                              "w": 486
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 485,
                              "y": 255,
                              "h": 46,
                              "w": 508
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 489,
                              "y": 512,
                              "h": 58,
                              "w": 331
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "608_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 651,
                  "w": 963
            },
            "ref": {
                  "x": 127,
                  "y": 52,
                  "h": 35,
                  "w": 329
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 42,
                              "y": 148,
                              "h": 345,
                              "w": 291
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 613,
                              "y": 93,
                              "h": 68,
                              "w": 253
                        },
                        "ocr_type": 1, "regex": "[0-9A-Z]{9}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 212,
                              "h": 44,
                              "w": 255
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 154,
                              "h": 49,
                              "w": 290
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 308,
                              "h": 48,
                              "w": 267
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 300,
                              "y": 456,
                              "h": 63,
                              "w": 236
                        },
                        "ocr_type": 1, "regex": "[0-9]+\\s{1,2}[A-Z]{3}\\s[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 314,
                              "y": 366,
                              "h": 44,
                              "w": 73
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 48,
                              "y": 515,
                              "h": 124,
                              "w": 891
                        }
                  },
            }
      },
    "702_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 400,
                  "w": 614
            },
            "ref": {
                  "x": 426,
                  "y": 5,
                  "h": 119,
                  "w": 139
            },
            "threshold": 0.85,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 36,
                              "y": 96,
                              "h": 202,
                              "w": 152
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 308,
                              "y": 147,
                              "h": 34,
                              "w": 179
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 210,
                              "y": 144,
                              "h": 36,
                              "w": 93
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 212,
                              "y": 305,
                              "h": 27,
                              "w": 124
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 226,
                              "y": 48,
                              "h": 38,
                              "w": 201
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 348,
                              "y": 307,
                              "h": 26,
                              "w": 32
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "688_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 452,
                  "w": 720
            },
            "ref": {
                  "x": 241,
                  "y": 17,
                  "h": 39,
                  "w": 249
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 38,
                              "y": 115,
                              "h": 238,
                              "w": 197
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 164,
                              "h": 30,
                              "w": 227
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 238,
                              "y": 116,
                              "h": 34,
                              "w": 258
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 210,
                              "h": 33,
                              "w": 262
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 243,
                              "y": 350,
                              "h": 37,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 370,
                              "y": 257,
                              "h": 35,
                              "w": 181
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 239,
                              "y": 258,
                              "h": 33,
                              "w": 64
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 521,
                              "y": 376,
                              "h": 56,
                              "w": 167
                        }
                  }
            }
      },
    "356_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 534,
                  "w": 900
            },
            "ref": {
                  "x": 15,
                  "y": 338,
                  "h": 136,
                  "w": 221
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 17,
                              "y": 119,
                              "h": 224,
                              "w": 199
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 287,
                              "y": 135,
                              "h": 36,
                              "w": 307
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 285,
                              "y": 165,
                              "h": 34,
                              "w": 145
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "3": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 267,
                              "y": 193,
                              "h": 33,
                              "w": 54
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "372_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 571,
                  "w": 850
            },
            "ref": {
                  "x": 116,
                  "y": 15,
                  "h": 55,
                  "w": 148
            },
            "threshold": 0.77,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 14,
                              "y": 105,
                              "h": 343,
                              "w": 251
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 569,
                              "y": 131,
                              "h": 41,
                              "w": 253
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 281,
                              "y": 231,
                              "h": 38,
                              "w": 238
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 282,
                              "y": 182,
                              "h": 38,
                              "w": 272
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 566,
                              "y": 282,
                              "h": 40,
                              "w": 285
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 570,
                              "y": 381,
                              "h": 37,
                              "w": 279
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 277,
                              "y": 334,
                              "h": 33,
                              "w": 50
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 322,
                              "y": 455,
                              "h": 75,
                              "w": 490
                        }
                  }
            }
      },
    "32_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 637,
                  "w": 1024
            },
            "ref": {
                  "x": 59,
                  "y": 33,
                  "h": 100,
                  "w": 284
            },
            "threshold": 0.7,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 84,
                              "y": 151,
                              "h": 349,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 385,
                              "y": 540,
                              "h": 60,
                              "w": 184
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 384,
                              "y": 218,
                              "h": 39,
                              "w": 285
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 386,
                              "y": 131,
                              "h": 41,
                              "w": 329
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 388,
                              "y": 365,
                              "h": 34,
                              "w": 199
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 383,
                              "y": 479,
                              "h": 39,
                              "w": 219
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 80,
                              "y": 547,
                              "h": 54,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 381,
                              "y": 304,
                              "h": 36,
                              "w": 74
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 754,
                              "y": 343,
                              "h": 95,
                              "w": 216
                        }
                  }
            }
      },
    "344_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 601,
                  "w": 955
            },
            "ref": {
                  "x": 127,
                  "y": 71,
                  "h": 47,
                  "w": 210
            },
            "threshold": 0.43,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 53,
                              "y": 220,
                              "h": 340,
                              "w": 280
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 220,
                              "h": 49,
                              "w": 310
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 155,
                              "y": 175,
                              "h": 49,
                              "w": 265
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 27,
                              "y": 177,
                              "h": 44,
                              "w": 110
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 345,
                              "h": 46,
                              "w": 221
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 365,
                              "y": 517,
                              "h": 56,
                              "w": 223
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 645,
                              "y": 519,
                              "h": 58,
                              "w": 276
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 610,
                              "y": 341,
                              "h": 51,
                              "w": 72
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "51_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 592,
                  "w": 928
            },
            "ref": {
                  "x": 595,
                  "y": 40,
                  "h": 81,
                  "w": 265
            },
            "threshold": 0.8,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 49,
                              "y": 225,
                              "h": 314,
                              "w": 233
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 604,
                              "y": 432,
                              "h": 39,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 299,
                              "y": 266,
                              "h": 44,
                              "w": 304
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 298,
                              "y": 181,
                              "h": 35,
                              "w": 343
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 301,
                              "y": 432,
                              "h": 34,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 304,
                              "y": 486,
                              "h": 41,
                              "w": 150
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 302,
                              "y": 381,
                              "h": 35,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": ""
                  }
            }
      },
    "364_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 1117,
                  "w": 1599
            },
            "ref": {
                  "x": 898,
                  "y": 86,
                  "h": 42,
                  "w": 165
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 85,
                              "y": 175,
                              "h": 579,
                              "w": 399
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 1309,
                              "y": 175,
                              "h": 70,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "([0-9A-Z]){1,}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 629,
                              "y": 347,
                              "h": 80,
                              "w": 371
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 659,
                              "y": 255,
                              "h": 85,
                              "w": 369
                        },
                        "ocr_type": 0, "regex": "([A-Z]+\\s?){1,}"
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 887,
                              "y": 549,
                              "h": 75,
                              "w": 245
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "5": {
                        "name": "expired_date",
                        "type": 0,
                        "points": {
                              "x": 787,
                              "y": 841,
                              "h": 85,
                              "w": 235
                        },
                        "ocr_type": 1, "regex": "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 597,
                              "y": 689,
                              "h": 85,
                              "w": 75
                        },
                        "ocr_type": 1, "regex": "[MF]{1}"
                  },
                  "7": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 93,
                              "y": 915,
                              "h": 175,
                              "w": 1400
                        },
                        "check_mrz": True
                  }
            }
      },
    "214_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 120,
                  "y": 71,
                  "h": 100,
                  "w": 433
            },
            "threshold": 0.5,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 132,
                              "y": 200,
                              "h": 336,
                              "w": 245
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 477,
                              "y": 167,
                              "h": 64,
                              "w": 412
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 153,
                              "y": 540,
                              "h": 35,
                              "w": 268
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 154,
                              "y": 580,
                              "h": 38,
                              "w": 299
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 409,
                              "y": 319,
                              "h": 33,
                              "w": 252
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 406,
                              "y": 486,
                              "h": 50,
                              "w": 264
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 481,
                              "y": 388,
                              "h": 44,
                              "w": 34
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 134,
                              "y": 466,
                              "h": 65,
                              "w": 242
                        }
                  }
            }
      },
    "124_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 139,
                  "y": 75,
                  "h": 58,
                  "w": 233
            },
            "threshold": 0.74,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 136,
                              "y": 198,
                              "h": 350,
                              "w": 307
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 275,
                              "h": 36,
                              "w": 212
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 461,
                              "y": 197,
                              "h": 39,
                              "w": 340
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 161,
                              "h": 37,
                              "w": 237
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 457,
                              "y": 512,
                              "h": 41,
                              "w": 264
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 462,
                              "y": 569,
                              "h": 40,
                              "w": 246
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 453,
                              "y": 354,
                              "h": 43,
                              "w": 40
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 193,
                              "y": 554,
                              "h": 70,
                              "w": 220
                        }
                  }
            }
      },
    "124_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 562,
                  "w": 816
            },
            "ref": {
                  "x": 354,
                  "y": 5,
                  "h": 49,
                  "w": 185
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 31,
                              "y": 97,
                              "h": 364,
                              "w": 294
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 883,
                              "y": 394,
                              "h": 63,
                              "w": 344
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 383,
                              "y": 262,
                              "h": 45,
                              "w": 616
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 387,
                              "y": 197,
                              "h": 46,
                              "w": 474
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 391,
                              "y": 390,
                              "h": 51,
                              "w": 258
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 399,
                              "y": 572,
                              "h": 45,
                              "w": 265
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 391,
                              "y": 453,
                              "h": 39,
                              "w": 50
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 878,
                              "y": 133,
                              "h": 42,
                              "w": 176
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "9": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 69,
                              "y": 625,
                              "h": 153,
                              "w": 1162
                        },
                        "check_mrz": True
                  }
            }
      },
    "76_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 385,
                  "y": 77,
                  "h": 70,
                  "w": 380
            },
            "threshold": 0.72,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 743,
                              "y": 214,
                              "h": 316,
                              "w": 267
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 151,
                              "y": 413,
                              "h": 55,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 227,
                              "h": 29,
                              "w": 332
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 196,
                              "h": 33,
                              "w": 396
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 359,
                              "y": 373,
                              "h": 35,
                              "w": 138
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 425,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 274,
                              "h": 36,
                              "w": 43
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "signature",
                        "type": 0,
                        "points": {
                              "x": 452,
                              "y": 526,
                              "h": 90,
                              "w": 263
                        }
                  }
            }
      },
    "76_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 780,
                  "w": 1287
            },
            "ref": {
                  "x": 134,
                  "y": 80,
                  "h": 74,
                  "w": 188
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 30,
                              "y": 98,
                              "h": 296,
                              "w": 221
                        }
                  },
                  "1": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 250,
                              "y": 151,
                              "h": 33,
                              "w": 282
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 250,
                              "y": 113,
                              "h": 32,
                              "w": 215
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 249,
                              "y": 231,
                              "h": 31,
                              "w": 296
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 252,
                              "y": 350,
                              "h": 29,
                              "w": 225
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 252,
                              "y": 270,
                              "h": 30,
                              "w": 38
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 587,
                              "y": 74,
                              "h": 35,
                              "w": 174
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 28,
                              "y": 427,
                              "h": 111,
                              "w": 760
                        },
                        "check_mrz": True
                  }
            }
      },
    "112_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 704,
                  "w": 1171
            },
            "ref": {
                  "x": 131,
                  "y": 80,
                  "h": 82,
                  "w": 314
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 136,
                              "y": 168,
                              "h": 318,
                              "w": 285
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 615,
                              "y": 167,
                              "h": 35,
                              "w": 276
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 500,
                              "y": 302,
                              "h": 92,
                              "w": 393
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 505,
                              "y": 207,
                              "h": 94,
                              "w": 364
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 560,
                              "y": 467,
                              "h": 41,
                              "w": 164
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 847,
                              "y": 567,
                              "h": 46,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 563,
                              "y": 563,
                              "h": 53,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 855,
                              "y": 461,
                              "h": 56,
                              "w": 112
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 125,
                              "y": 555,
                              "h": 69,
                              "w": 234
                        }
                  }
            }
      },
    "152_id_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 680,
                  "w": 1074
            },
            "ref": {
                  "x": 254,
                  "y": 19,
                  "h": 70,
                  "w": 547
            },
            "threshold": 0.63,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 58,
                              "y": 164,
                              "h": 379,
                              "w": 275
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 118,
                              "y": 578,
                              "h": 57,
                              "w": 222
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 368,
                              "y": 219,
                              "h": 45,
                              "w": 477
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 363,
                              "y": 117,
                              "h": 77,
                              "w": 427
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 367,
                              "y": 352,
                              "h": 51,
                              "w": 193
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 616,
                              "y": 355,
                              "h": 45,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 615,
                              "y": 424,
                              "h": 44,
                              "w": 196
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 610,
                              "y": 286,
                              "h": 46,
                              "w": 49
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 356,
                              "y": 490,
                              "h": 129,
                              "w": 452
                        }
                  }
            }
      },
    "496_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 832,
                  "w": 1108
            },
            "ref": {
                  "x": 792,
                  "y": 66,
                  "h": 63,
                  "w": 236
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 41,
                              "y": 179,
                              "h": 423,
                              "w": 295
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 797,
                              "y": 145,
                              "h": 59,
                              "w": 165
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 792,
                              "y": 220,
                              "h": 65,
                              "w": 210
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 357,
                              "y": 301,
                              "h": 56,
                              "w": 184
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 362,
                              "y": 210,
                              "h": 61,
                              "w": 245
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 358,
                              "y": 478,
                              "h": 55,
                              "w": 169
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 782,
                              "y": 574,
                              "h": 52,
                              "w": 159
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 779,
                              "y": 484,
                              "h": 57,
                              "w": 61
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 3,
                        "points": {
                              "x": 13,
                              "y": 646,
                              "h": 157,
                              "w": 1076
                        },
                        "check_mrz": True
                  }
            }
      },
    "275_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 521,
                  "w": 792
            },
            "ref": {
                  "x": 29,
                  "y": 23,
                  "h": 36,
                  "w": 219
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 517,
                              "y": 127,
                              "h": 322,
                              "w": 220
                        }
                  },
                  "1": {
                        "name": "identity_number",
                        "type": 0,
                        "points": {
                              "x": 541,
                              "y": 453,
                              "h": 38,
                              "w": 167
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "serial_number",
                        "type": 0,
                        "points": {
                              "x": 88,
                              "y": 312,
                              "h": 38,
                              "w": 129
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 407,
                              "y": 215,
                              "h": 35,
                              "w": 97
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 404,
                              "y": 156,
                              "h": 32,
                              "w": 91
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 338,
                              "y": 248,
                              "h": 39,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 342,
                              "y": 278,
                              "h": 34,
                              "w": 119
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "7": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 401,
                              "y": 369,
                              "h": 40,
                              "w": 74
                        }
                  }
            }
      },
    "598_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 714,
                  "w": 1105
            },
            "ref": {
                  "x": 495,
                  "y": 48,
                  "h": 64,
                  "w": 148
            },
            "threshold": 0.6,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 75,
                              "y": 92,
                              "h": 342,
                              "w": 271
                        }
                  },
                  "1": {
                        "name": "licence_number",
                        "type": 0,
                        "points": {
                              "x": 162,
                              "y": 549,
                              "h": 87,
                              "w": 186
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 477,
                              "y": 186,
                              "h": 40,
                              "w": 387
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 682,
                              "y": 477,
                              "h": 50,
                              "w": 365
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 387,
                              "y": 566,
                              "h": 71,
                              "w": 297
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 670,
                              "y": 357,
                              "h": 79,
                              "w": 274
                        }
                  }
            }
      },
    "704_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 573,
                  "w": 810
            },
            "ref": {
                  "x": 70,
                  "y": 70,
                  "h": 35,
                  "w": 208
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 78,
                              "y": 111,
                              "h": 269,
                              "w": 196
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 576,
                              "y": 95,
                              "h": 41,
                              "w": 122
                        },
                        "ocr_type": 1, "regex": "[A-Z]{1}[0-9]{7}"
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 297,
                              "y": 143,
                              "h": 39,
                              "w": 197
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 295,
                              "y": 217,
                              "h": 35,
                              "w": 148
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "4": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 521,
                              "y": 314,
                              "h": 38,
                              "w": 142
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "gender",
                        "type": 0,
                        "points": {
                              "x": 285,
                              "y": 265,
                              "h": 37,
                              "w": 135
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 49,
                              "y": 409,
                              "h": 123,
                              "w": 729
                        },
                        "check_mrz": True
                  }
            }
      },
    "36_driving_licence_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 591,
                  "w": 898
            },
            "ref": {
                  "x": 218,
                  "y": 38,
                  "h": 47,
                  "w": 235
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 633,
                              "y": 243,
                              "h": 237,
                              "w": 195
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 714,
                              "y": 181,
                              "h": 51,
                              "w": 136
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 15,
                              "y": 268,
                              "h": 33,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 17,
                              "y": 235,
                              "h": 33,
                              "w": 297
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 304,
                              "y": 389,
                              "h": 43,
                              "w": 224
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 17,
                              "y": 383,
                              "h": 48,
                              "w": 205
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "car_type",
                        "type": 1,
                        "points": {
                              "x": 12,
                              "y": 450,
                              "h": 38,
                              "w": 253
                        }
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 12,
                              "y": 484,
                              "h": 87,
                              "w": 321
                        }
                  }
            }
      },
    "504_passport_front": {
            "initial": {
                  "x": 0,
                  "y": 0,
                  "h": 757,
                  "w": 1106
            },
            "ref": {
                  "x": 9,
                  "y": 4,
                  "h": 45,
                  "w": 308
            },
            "threshold": 0.65,
            "fields": {
                  "0": {
                        "name": "photo",
                        "type": 1,
                        "points": {
                              "x": 633,
                              "y": 243,
                              "h": 237,
                              "w": 195
                        }
                  },
                  "1": {
                        "name": "passport_number",
                        "type": 0,
                        "points": {
                              "x": 717,
                              "y": 90,
                              "h": 42,
                              "w": 155
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "2": {
                        "name": "surname",
                        "type": 0,
                        "points": {
                              "x": 348,
                              "y": 179,
                              "h": 45,
                              "w": 328
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "3": {
                        "name": "name",
                        "type": 0,
                        "points": {
                              "x": 342,
                              "y": 272,
                              "h": 46,
                              "w": 358
                        },
                        "ocr_type": 0, "regex": ""
                  },
                  "4": {
                        "name": "birth_date",
                        "type": 0,
                        "points": {
                              "x": 704,
                              "y": 333,
                              "h": 44,
                              "w": 158
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "5": {
                        "name": "expiry_date",
                        "type": 0,
                        "points": {
                              "x": 360,
                              "y": 499,
                              "h": 52,
                              "w": 152
                        },
                        "ocr_type": 1, "regex": ""
                  },
                  "6": {
                        "name": "car_type",
                        "type": 3,
                        "points": {
                              "x": 110,
                              "y": 501,
                              "h": 51,
                              "w": 151
                        }
                  },
                  "7": {
                        "name": "signature",
                        "type": 3,
                        "points": {
                              "x": 771,
                              "y": 494,
                              "h": 86,
                              "w": 279
                        }
                  },
                  "8": {
                        "name": "mrz",
                        "mrz_type": "td3",
                        "type": 2,
                        "points": {
                              "x": 42,
                              "y": 564,
                              "h": 144,
                              "w": 1033
                        }
                  }
            }
      }
}
