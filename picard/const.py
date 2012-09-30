# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2007 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

# Install gettext "noop" function in case const.py gets imported directly.
import __builtin__
__builtin__.__dict__['N_'] = lambda a: a

# AcoustID client API key
ACOUSTID_KEY = '0zClDiGo'

# Various Artists MBID
VARIOUS_ARTISTS_ID = '89ad4ac3-39f7-470e-963a-56509c546377'

# Release formats
RELEASE_FORMATS = {
    u'CD': N_('CD'),
    u'CD-R': N_('CD-R'),
    u'HDCD': N_('HDCD'),
    u'8cm CD': N_('8cm CD'),
    u'Vinyl': N_('Vinyl'),
    u'7" Vinyl': N_('7" Vinyl'),
    u'10" Vinyl': N_('10" Vinyl'),
    u'12" Vinyl': N_('12" Vinyl'),
    u'Digital Media': N_('Digital Media'),
    u'USB Flash Drive': N_('USB Flash Drive'),
    u'slotMusic': N_('slotMusic'),
    u'Cassette': N_('Cassette'),
    u'DVD': N_('DVD'),
    u'DVD-Audio': N_('DVD-Audio'),
    u'DVD-Video': N_('DVD-Video'),
    u'SACD': N_('SACD'),
    u'DualDisc': N_('DualDisc'),
    u'MiniDisc': N_('MiniDisc'),
    u'Blu-ray': N_('Blu-ray'),
    u'HD-DVD': N_('HD-DVD'),
    u'Videotape': N_('Videotape'),
    u'VHS': N_('VHS'),
    u'Betamax': N_('Betamax'),
    u'VCD': N_('VCD'),
    u'SVCD': N_('SVCD'),
    u'UMD': N_('UMD'),
    u'Other': N_('Other'),
    u'LaserDisc': N_('LaserDisc'),
    u'Cartridge': N_('Cartridge'),
    u'Reel-to-reel': N_('Reel-to-reel'),
    u'DAT': N_('DAT'),
    u'Wax Cylinder': N_('Wax Cylinder'),
    u'Piano Roll': N_('Piano Roll'),
    u'DCC': N_('DCC')
}

# Release countries
RELEASE_COUNTRIES = {
    u'BD': N_('Bangladesh'),
    u'BE': N_('Belgium'),
    u'BF': N_('Burkina Faso'),
    u'BG': N_('Bulgaria'),
    u'BB': N_('Barbados'),
    u'WF': N_('Wallis and Futuna Islands'),
    u'BM': N_('Bermuda'),
    u'BN': N_('Brunei Darussalam'),
    u'BO': N_('Bolivia'),
    u'BH': N_('Bahrain'),
    u'BI': N_('Burundi'),
    u'BJ': N_('Benin'),
    u'BT': N_('Bhutan'),
    u'JM': N_('Jamaica'),
    u'BV': N_('Bouvet Island'),
    u'BW': N_('Botswana'),
    u'WS': N_('Samoa'),
    u'BR': N_('Brazil'),
    u'BS': N_('Bahamas'),
    u'BY': N_('Belarus'),
    u'BZ': N_('Belize'),
    u'RU': N_('Russian Federation'),
    u'RW': N_('Rwanda'),
    u'RE': N_('Reunion'),
    u'TM': N_('Turkmenistan'),
    u'TJ': N_('Tajikistan'),
    u'RO': N_('Romania'),
    u'TK': N_('Tokelau'),
    u'GW': N_('Guinea-Bissa'),
    u'GU': N_('Guam'),
    u'GT': N_('Guatemala'),
    u'GR': N_('Greece'),
    u'GQ': N_('Equatorial Guinea'),
    u'GP': N_('Guadeloupe'),
    u'JP': N_('Japan'),
    u'GY': N_('Guyana'),
    u'GF': N_('French Guiana'),
    u'GE': N_('Georgia'),
    u'GD': N_('Grenada'),
    u'GB': N_('United Kingdom'),
    u'GA': N_('Gabon'),
    u'SV': N_('El Salvador'),
    u'GN': N_('Guinea'),
    u'GM': N_('Gambia'),
    u'GL': N_('Greenland'),
    u'GI': N_('Gibraltar'),
    u'GH': N_('Ghana'),
    u'OM': N_('Oman'),
    u'TN': N_('Tunisia'),
    u'JO': N_('Jordan'),
    u'HT': N_('Haiti'),
    u'HU': N_('Hungary'),
    u'HK': N_('Hong Kong'),
    u'HN': N_('Honduras'),
    u'HM': N_('Heard and Mc Donald Islands'),
    u'VE': N_('Venezuela'),
    u'PR': N_('Puerto Rico'),
    u'PW': N_('Palau'),
    u'PT': N_('Portugal'),
    u'SJ': N_('Svalbard and Jan Mayen Islands'),
    u'PY': N_('Paraguay'),
    u'IQ': N_('Iraq'),
    u'PA': N_('Panama'),
    u'PF': N_('French Polynesia'),
    u'PG': N_('Papua New Guinea'),
    u'PE': N_('Peru'),
    u'PK': N_('Pakistan'),
    u'PH': N_('Philippines'),
    u'PN': N_('Pitcairn'),
    u'PL': N_('Poland'),
    u'PM': N_('St. Pierre and Miquelon'),
    u'ZM': N_('Zambia'),
    u'EH': N_('Western Sahara'),
    u'EE': N_('Estonia'),
    u'EG': N_('Egypt'),
    u'ZA': N_('South Africa'),
    u'EC': N_('Ecuador'),
    u'IT': N_('Italy'),
    u'VN': N_('Viet Nam'),
    u'SB': N_('Solomon Islands'),
    u'ET': N_('Ethiopia'),
    u'SO': N_('Somalia'),
    u'ZW': N_('Zimbabwe'),
    u'SA': N_('Saudi Arabia'),
    u'ES': N_('Spain'),
    u'ER': N_('Eritrea'),
    u'MD': N_('Moldova, Republic of'),
    u'MG': N_('Madagascar'),
    u'MA': N_('Morocco'),
    u'MC': N_('Monaco'),
    u'UZ': N_('Uzbekistan'),
    u'MM': N_('Myanmar'),
    u'ML': N_('Mali'),
    u'MO': N_('Macau'),
    u'MN': N_('Mongolia'),
    u'MH': N_('Marshall Islands'),
    u'MK': N_('Macedonia, The Former Yugoslav Republic of'),
    u'MU': N_('Mauritius'),
    u'MT': N_('Malta'),
    u'MW': N_('Malawi'),
    u'MV': N_('Maldives'),
    u'MQ': N_('Martinique'),
    u'MP': N_('Northern Mariana Islands'),
    u'MS': N_('Montserrat'),
    u'MR': N_('Mauritania'),
    u'UG': N_('Uganda'),
    u'MY': N_('Malaysia'),
    u'MX': N_('Mexico'),
    u'IL': N_('Israel'),
    u'FR': N_('France'),
    u'IO': N_('British Indian Ocean Territory'),
    u'SH': N_('St. Helena'),
    u'FI': N_('Finland'),
    u'FJ': N_('Fiji'),
    u'FK': N_('Falkland Islands (Malvinas)'),
    u'FM': N_('Micronesia, Federated States of'),
    u'FO': N_('Faroe Islands'),
    u'NI': N_('Nicaragua'),
    u'NL': N_('Netherlands'),
    u'NO': N_('Norway'),
    u'NA': N_('Namibia'),
    u'VU': N_('Vanuatu'),
    u'NC': N_('New Caledonia'),
    u'NE': N_('Niger'),
    u'NF': N_('Norfolk Island'),
    u'NG': N_('Nigeria'),
    u'NZ': N_('New Zealand'),
    u'ZR': N_('Zaire'),
    u'NP': N_('Nepal'),
    u'NR': N_('Nauru'),
    u'NU': N_('Niue'),
    u'CK': N_('Cook Islands'),
    u'CI': N_('Cote d\'Ivoire'),
    u'CH': N_('Switzerland'),
    u'CO': N_('Colombia'),
    u'CN': N_('China'),
    u'CM': N_('Cameroon'),
    u'CL': N_('Chile'),
    u'CC': N_('Cocos (Keeling) Islands'),
    u'CA': N_('Canada'),
    u'CG': N_('Congo'),
    u'CF': N_('Central African Republic'),
    u'CZ': N_('Czech Republic'),
    u'CY': N_('Cyprus'),
    u'CX': N_('Christmas Island'),
    u'CR': N_('Costa Rica'),
    u'CV': N_('Cape Verde'),
    u'CU': N_('Cuba'),
    u'SZ': N_('Swaziland'),
    u'SY': N_('Syrian Arab Republic'),
    u'KG': N_('Kyrgyzstan'),
    u'KE': N_('Kenya'),
    u'SR': N_('Suriname'),
    u'KI': N_('Kiribati'),
    u'KH': N_('Cambodia'),
    u'KN': N_('Saint Kitts and Nevis'),
    u'KM': N_('Comoros'),
    u'ST': N_('Sao Tome and Principe'),
    u'SI': N_('Slovenia'),
    u'KW': N_('Kuwait'),
    u'SN': N_('Senegal'),
    u'SM': N_('San Marino'),
    u'SL': N_('Sierra Leone'),
    u'SC': N_('Seychelles'),
    u'KZ': N_('Kazakhstan'),
    u'KY': N_('Cayman Islands'),
    u'SG': N_('Singapore'),
    u'SE': N_('Sweden'),
    u'SD': N_('Sudan'),
    u'DO': N_('Dominican Republic'),
    u'DM': N_('Dominica'),
    u'DJ': N_('Djibouti'),
    u'DK': N_('Denmark'),
    u'VG': N_('Virgin Islands (British)'),
    u'DE': N_('Germany'),
    u'YE': N_('Yemen'),
    u'DZ': N_('Algeria'),
    u'US': N_('United States'),
    u'UY': N_('Uruguay'),
    u'YT': N_('Mayotte'),
    u'UM': N_('United States Minor Outlying Islands'),
    u'LB': N_('Lebanon'),
    u'LC': N_('Saint Lucia'),
    u'LA': N_('Lao People\'s Democratic Republic'),
    u'TV': N_('Tuvalu'),
    u'TW': N_('Taiwan'),
    u'TT': N_('Trinidad and Tobago'),
    u'TR': N_('Turkey'),
    u'LK': N_('Sri Lanka'),
    u'LI': N_('Liechtenstein'),
    u'LV': N_('Latvia'),
    u'TO': N_('Tonga'),
    u'LT': N_('Lithuania'),
    u'LU': N_('Luxembourg'),
    u'LR': N_('Liberia'),
    u'LS': N_('Lesotho'),
    u'TH': N_('Thailand'),
    u'TF': N_('French Southern Territories'),
    u'TG': N_('Togo'),
    u'TD': N_('Chad'),
    u'TC': N_('Turks and Caicos Islands'),
    u'LY': N_('Libyan Arab Jamahiriya'),
    u'VA': N_('Vatican City State (Holy See)'),
    u'VC': N_('Saint Vincent and The Grenadines'),
    u'AE': N_('United Arab Emirates'),
    u'AD': N_('Andorra'),
    u'AG': N_('Antigua and Barbuda'),
    u'AF': N_('Afghanistan'),
    u'AI': N_('Anguilla'),
    u'VI': N_('Virgin Islands (U.S.)'),
    u'IS': N_('Iceland'),
    u'IR': N_('Iran (Islamic Republic of)'),
    u'AM': N_('Armenia'),
    u'AL': N_('Albania'),
    u'AO': N_('Angola'),
    u'AN': N_('Netherlands Antilles'),
    u'AQ': N_('Antarctica'),
    u'AS': N_('American Samoa'),
    u'AR': N_('Argentina'),
    u'AU': N_('Australia'),
    u'AT': N_('Austria'),
    u'AW': N_('Aruba'),
    u'IN': N_('India'),
    u'TZ': N_('Tanzania, United Republic of'),
    u'AZ': N_('Azerbaijan'),
    u'IE': N_('Ireland'),
    u'ID': N_('Indonesia'),
    u'UA': N_('Ukraine'),
    u'QA': N_('Qatar'),
    u'MZ': N_('Mozambique'),
    u'BA': N_('Bosnia and Herzegovina'),
    u'CD': N_('Congo, The Democratic Republic of the'),
    u'CS': N_('Serbia and Montenegro (historical, 2003-2006)'),
    u'RS': N_('Serbia'),
    u'ME': N_('Montenegro'),
    u'HR': N_('Croatia'),
    u'KP': N_('Korea (North), Democratic People\'s Republic of'),
    u'KR': N_('Korea (South), Republic of'),
    u'SK': N_('Slovakia'),
    u'SU': N_('Soviet Union (historical, 1922-1991)'),
    u'TL': N_('East Timor'),
    u'XC': N_('Czechoslovakia (historical, 1918-1992)'),
    u'XE': N_('Europe'),
    u'XG': N_('East Germany (historical, 1949-1990)'),
    u'XU': N_('[Unknown Country]'),
    u'XW': N_('[Worldwide]'),
    u'YU': N_('Yugoslavia (historical, 1918-1992)'),
}

# List of available user interface languages
UI_LANGUAGES = [
    #(u'af', u'Afrikaans', N_(u'Afrikaans')),
    #(u'ar', u'العربية', N_(u'Arabic')),
    #(u'ast', u'Asturianu', N_(u'Asturian')),
    #(u'bg', u'Български', N_(u'Bulgarian')),
    #(u'ca', u'Català', N_(u'Catalan')),
    #(u'cs', u'Čeština', N_(u'Czech')),
    #(u'cy', u'Cymraeg', N_(u'Welsh')),
    (u'da', u'Dansk', N_(u'Danish')),
    (u'de', u'Deutsch', N_(u'German')),
    #(u'el', u'ελληνικά', N_(u'Greek')),
    (u'en', u'English', N_(u'English')),
    (u'en_CA', u'English (Canada)', N_(u'English (Canada)')),
    (u'en_GB', u'English (UK)', N_(u'English (UK)')),
    #(u'eo', u'Esperanto', N_(u'Esperanto')),
    (u'es', u'Español', N_(u'Spanish')),
    (u'et', u'Eesti keel', N_(u'Estonian')),
    #(u'fa', u'فارسی', N_(u'Persian')),
    (u'fi', u'Suomi', N_(u'Finnish')),
    #(u'fo', u'Føroyskt', N_(u'Faroese')),
    (u'fr', u'Français', N_(u'French')),
    #(u'fr_CA', u'Français canadien', N_(u'French (Canada)')),
    #(u'fy', u'Frysk', N_(u'Frisian')),
    #(u'gl', u'Galego', N_(u'Galician')),
    #(u'he', u'עברית', N_(u'Hebrew')),
    #(u'hi', u'हिन्दी', N_(u'Hindi')),
    #(u'hu', u'Magyar', N_(u'Hungarian')),
    #(u'id', u'Bahasa Indonesia', N_(u'Indonesian')),
    #(u'is', u'Íslenska', N_(u'Islandic')),
    (u'it', u'Italiano', N_(u'Italian')),
    #(u'ja', u'日本語', N_(u'Japanese')),
    #(u'kn', u'ಕನ್ನಡ', N_(u'Kannada')),
    #(u'ko', u'한국어', N_(u'Korean')),
    #(u'lt', u'Lietuvių', N_(u'Lithuanian')),
    #(u'nb', u'Norsk bokmål', N_(u'Norwegian Bokmal')),
    #(u'nds', u'Plattdüütsch', N_(u'Low German')),
    (u'nl', u'Nederlands', N_(u'Dutch')),
    #(u'oc', u'Occitan', N_(u'Occitan')),
    (u'pl', u'Polski', N_(u'Polish')),
    #(u'pt', u'Português', N_(u'Portuguese')),
    (u'pt_BR', u'Português do Brasil', N_(u'Brazilian Portuguese')),
    #(u'ro', u'Română', N_(u'Romanian')),
    #(u'ru', u'Pyccĸий', N_(u'Russian')),
    #(u'sco', u'Scots leid', N_(u'Scots')),
    #(u'sk', u'Slovenčina', N_(u'Slovak')),
    #(u'sl', u'Slovenščina', N_(u'Slovenian')),
    #(u'sr', u'Србин', N_(u'Serbian')),
    (u'sv', u'Svenska', N_(u'Swedish')),
    #(u'ta', u'தமிழ்', N_(u'Tamil')),
    #(u'tr', u'Türkçe', N_(u'Turkish')),
    #(u'uk', u'Украї́нська мо́ва', N_(u'Ukrainian')),
    #(u'zh_CN', u'中文', N_(u'Chinese')),
]

ALIAS_LOCALES = {
    u'aa': 'Afar',
    u'aa_DJ': 'Afar (Djibouti)',
    u'aa_ER': 'Afar (Eritrea)',
    u'aa_ER_SAAHO': 'Afar (Eritrea) (Saho)',
    u'aa_ET': 'Afar (Ethiopia)',
    u'af': 'Afrikaans',
    u'af_NA': 'Afrikaans (Namibia)',
    u'af_ZA': 'Afrikaans (South Africa)',
    u'ak': 'Akan',
    u'ak_GH': 'Akan (Ghana)',
    u'sq': 'Albanian',
    u'sq_AL': 'Albanian (Albania)',
    u'am': 'Amharic',
    u'am_ET': 'Amharic (Ethiopia)',
    u'ar': 'Arabic',
    u'ar_DZ': 'Arabic (Algeria)',
    u'ar_BH': 'Arabic (Bahrain)',
    u'ar_EG': 'Arabic (Egypt)',
    u'ar_IQ': 'Arabic (Iraq)',
    u'ar_JO': 'Arabic (Jordan)',
    u'ar_KW': 'Arabic (Kuwait)',
    u'ar_LB': 'Arabic (Lebanon)',
    u'ar_LY': 'Arabic (Libya)',
    u'ar_MA': 'Arabic (Morocco)',
    u'ar_OM': 'Arabic (Oman)',
    u'ar_QA': 'Arabic (Qatar)',
    u'ar_SA': 'Arabic (Saudi Arabia)',
    u'ar_SD': 'Arabic (Sudan)',
    u'ar_SY': 'Arabic (Syria)',
    u'ar_TN': 'Arabic (Tunisia)',
    u'ar_AE': 'Arabic (United Arab Emirates)',
    u'ar_YE': 'Arabic (Yemen)',
    u'hy': 'Armenian',
    u'hy_AM': 'Armenian (Armenia)',
    u'hy_AM_REVISED': 'Armenian (Armenia) (Revised Orthography)',
    u'as': 'Assamese',
    u'as_IN': 'Assamese (India)',
    u'cch': 'Atsam',
    u'cch_NG': 'Atsam (Nigeria)',
    u'az': 'Azerbaijani',
    u'az_AZ': 'Azerbaijani (Azerbaijan)',
    u'az_Cyrl': 'Azerbaijani (Cyrillic)',
    u'az_Cyrl_AZ': 'Azerbaijani (Cyrillic) (Azerbaijan)',
    u'az_Latn': 'Azerbaijani (Latin)',
    u'az_Latn_AZ': 'Azerbaijani (Latin) (Azerbaijan)',
    u'eu': 'Basque',
    u'eu_ES': 'Basque (Spain)',
    u'be': 'Belarusian',
    u'be_BY': 'Belarusian (Belarus)',
    u'bn': 'Bengali',
    u'bn_BD': 'Bengali (Bangladesh)',
    u'bn_IN': 'Bengali (India)',
    u'byn': 'Blin',
    u'byn_ER': 'Blin (Eritrea)',
    u'bs': 'Bosnian',
    u'bs_BA': 'Bosnian (Bosnia and Herzegovina)',
    u'bg': 'Bulgarian',
    u'bg_BG': 'Bulgarian (Bulgaria)',
    u'my': 'Burmese',
    u'my_MM': 'Burmese (Myanmar [Burma])',
    u'ca': 'Catalan',
    u'ca_ES': 'Catalan (Spain)',
    u'zh': 'Chinese',
    u'zh_CN': 'Chinese (China)',
    u'zh_HK': 'Chinese (Hong Kong SAR China)',
    u'zh_MO': 'Chinese (Macau SAR China)',
    u'zh_Hans': 'Chinese (Simplified Han)',
    u'zh_Hans_CN': 'Chinese (Simplified Han) (China)',
    u'zh_Hans_HK': 'Chinese (Simplified Han) (Hong Kong SAR China)',
    u'zh_Hans_MO': 'Chinese (Simplified Han) (Macau SAR China)',
    u'zh_Hans_SG': 'Chinese (Simplified Han) (Singapore)',
    u'zh_SG': 'Chinese (Singapore)',
    u'zh_TW': 'Chinese (Taiwan)',
    u'zh_Hant': 'Chinese (Traditional Han)',
    u'zh_Hant_HK': 'Chinese (Traditional Han) (Hong Kong SAR China)',
    u'zh_Hant_MO': 'Chinese (Traditional Han) (Macau SAR China)',
    u'zh_Hant_TW': 'Chinese (Traditional Han) (Taiwan)',
    u'cop': 'Coptic',
    u'kw': 'Cornish',
    u'kw_GB': 'Cornish (United Kingdom)',
    u'hr': 'Croatian',
    u'hr_HR': 'Croatian (Croatia)',
    u'cs': 'Czech',
    u'cs_CZ': 'Czech (Czech Republic)',
    u'da': 'Danish',
    u'da_DK': 'Danish (Denmark)',
    u'dv': 'Divehi',
    u'dv_MV': 'Divehi (Maldives)',
    u'nl': 'Dutch',
    u'nl_BE': 'Dutch (Belgium)',
    u'nl_NL': 'Dutch (Netherlands)',
    u'dz': 'Dzongkha',
    u'dz_BT': 'Dzongkha (Bhutan)',
    u'en': 'English',
    u'en_AS': 'English (American Samoa)',
    u'en_AU': 'English (Australia)',
    u'en_BE': 'English (Belgium)',
    u'en_BZ': 'English (Belize)',
    u'en_BW': 'English (Botswana)',
    u'en_CA': 'English (Canada)',
    u'en_Dsrt': 'English (Deseret)',
    u'en_Dsrt_US': 'English (Deseret) (United States)',
    u'en_GU': 'English (Guam)',
    u'en_HK': 'English (Hong Kong SAR China)',
    u'en_IN': 'English (India)',
    u'en_IE': 'English (Ireland)',
    u'en_JM': 'English (Jamaica)',
    u'en_MT': 'English (Malta)',
    u'en_MH': 'English (Marshall Islands)',
    u'en_NA': 'English (Namibia)',
    u'en_NZ': 'English (New Zealand)',
    u'en_MP': 'English (Northern Mariana Islands)',
    u'en_PK': 'English (Pakistan)',
    u'en_PH': 'English (Philippines)',
    u'en_Shaw': 'English (Shavian)',
    u'en_SG': 'English (Singapore)',
    u'en_ZA': 'English (South Africa)',
    u'en_TT': 'English (Trinidad and Tobago)',
    u'en_UM': 'English (U.S. Minor Outlying Islands)',
    u'en_VI': 'English (U.S. Virgin Islands)',
    u'en_GB': 'English (United Kingdom)',
    u'en_US': 'English (United States)',
    u'en_US_POSIX': 'English (United States) (Computer)',
    u'en_ZW': 'English (Zimbabwe)',
    u'eo': 'Esperanto',
    u'et': 'Estonian',
    u'et_EE': 'Estonian (Estonia)',
    u'ee': 'Ewe',
    u'ee_GH': 'Ewe (Ghana)',
    u'ee_TG': 'Ewe (Togo)',
    u'fo': 'Faroese',
    u'fo_FO': 'Faroese (Faroe Islands)',
    u'fil': 'Filipino',
    u'fil_PH': 'Filipino (Philippines)',
    u'fi': 'Finnish',
    u'fi_FI': 'Finnish (Finland)',
    u'fr': 'French',
    u'fr_BE': 'French (Belgium)',
    u'fr_CA': 'French (Canada)',
    u'fr_FR': 'French (France)',
    u'fr_LU': 'French (Luxembourg)',
    u'fr_MC': 'French (Monaco)',
    u'fr_SN': 'French (Senegal)',
    u'fr_CH': 'French (Switzerland)',
    u'fur': 'Friulian',
    u'fur_IT': 'Friulian (Italy)',
    u'gaa': 'Ga',
    u'gaa_GH': 'Ga (Ghana)',
    u'gl': 'Galician',
    u'gl_ES': 'Galician (Spain)',
    u'gez': 'Geez',
    u'gez_ER': 'Geez (Eritrea)',
    u'gez_ET': 'Geez (Ethiopia)',
    u'ka': 'Georgian',
    u'ka_GE': 'Georgian (Georgia)',
    u'de': 'German',
    u'de_AT': 'German (Austria)',
    u'de_BE': 'German (Belgium)',
    u'de_DE': 'German (Germany)',
    u'de_LI': 'German (Liechtenstein)',
    u'de_LU': 'German (Luxembourg)',
    u'de_CH': 'German (Switzerland)',
    u'el_POLYTON': 'Greek',
    u'el': 'Greek',
    u'el_CY': 'Greek (Cyprus)',
    u'el_GR': 'Greek (Greece)',
    u'gu': 'Gujarati',
    u'gu_IN': 'Gujarati (India)',
    u'ha': 'Hausa',
    u'ha_Arab': 'Hausa (Arabic)',
    u'ha_Arab_NG': 'Hausa (Arabic) (Nigeria)',
    u'ha_Arab_SD': 'Hausa (Arabic) (Sudan)',
    u'ha_GH': 'Hausa (Ghana)',
    u'ha_Latn': 'Hausa (Latin)',
    u'ha_Latn_GH': 'Hausa (Latin) (Ghana)',
    u'ha_Latn_NE': 'Hausa (Latin) (Niger)',
    u'ha_Latn_NG': 'Hausa (Latin) (Nigeria)',
    u'ha_NE': 'Hausa (Niger)',
    u'ha_NG': 'Hausa (Nigeria)',
    u'ha_SD': 'Hausa (Sudan)',
    u'haw': 'Hawaiian',
    u'haw_US': 'Hawaiian (United States)',
    u'he': 'Hebrew',
    u'he_IL': 'Hebrew (Israel)',
    u'hi': 'Hindi',
    u'hi_IN': 'Hindi (India)',
    u'hu': 'Hungarian',
    u'hu_HU': 'Hungarian (Hungary)',
    u'is': 'Icelandic',
    u'is_IS': 'Icelandic (Iceland)',
    u'ig': 'Igbo',
    u'ig_NG': 'Igbo (Nigeria)',
    u'id': 'Indonesian',
    u'id_ID': 'Indonesian (Indonesia)',
    u'ia': 'Interlingua',
    u'iu': 'Inuktitut',
    u'ga': 'Irish',
    u'ga_IE': 'Irish (Ireland)',
    u'it': 'Italian',
    u'it_IT': 'Italian (Italy)',
    u'it_CH': 'Italian (Switzerland)',
    u'ja': 'Japanese',
    u'ja_JP': 'Japanese (Japan)',
    u'kaj': 'Jju',
    u'kaj_NG': 'Jju Nigeria',
    u'kl': 'Kalaallisut',
    u'kl_GL': 'Kalaallisut (Greenland)',
    u'kam': 'Kamba',
    u'kam_KE': 'Kamba (Kenya)',
    u'kn': 'Kannada',
    u'kn_IN': 'Kannada (India)',
    u'kk': 'Kazakh',
    u'kk_Cyrl': 'Kazakh (Cyrillic)',
    u'kk_Cyrl_KZ': 'Kazakh (Cyrillic) (Kazakhstan)',
    u'kk_KZ': 'Kazakh (Kazakhstan)',
    u'km': 'Khmer',
    u'km_KH': 'Khmer (Cambodia)',
    u'rw': 'Kinyarwanda',
    u'rw_RW': 'Kinyarwanda (Rwanda)',
    u'ky': 'Kirghiz',
    u'ky_KG': 'Kirghiz (Kyrgyzstan)',
    u'kok': 'Konkani',
    u'kok_IN': 'Konkani (India)',
    u'ko': 'Korean',
    u'ko_KR': 'Korean (South Korea)',
    u'kfo': 'Koro',
    u'kfo_CI': u'Koro (Côte d’Ivoire)',
    u'kpe': 'Kpelle',
    u'kpe_GN': 'Kpelle (Guinea)',
    u'kpe_LR': 'Kpelle (Liberia)',
    u'ku': 'Kurdish',
    u'ku_Arab': 'Kurdish (Arabic)',
    u'ku_Arab_IR': 'Kurdish (Arabic) (Iran)',
    u'ku_Arab_IQ': 'Kurdish (Arabic) (Iraq)',
    u'ku_Arab_SY': 'Kurdish (Arabic) (Syria)',
    u'ku_IR': 'Kurdish (Iran)',
    u'ku_IQ': 'Kurdish (Iraq)',
    u'ku_Latn': 'Kurdish (Latin)',
    u'ku_Latn_TR': 'Kurdish (Latin) (Turkey)',
    u'ku_SY': 'Kurdish (Syria)',
    u'ku_TR': 'Kurdish (Turkey)',
    u'lo': 'Lao',
    u'lo_LA': 'Lao (Laos)',
    u'lv': 'Latvian',
    u'lv_LV': 'Latvian (Latvia)',
    u'ln': 'Lingala',
    u'ln_CG': 'Lingala (Congo - Brazzaville)',
    u'ln_CD': 'Lingala (Congo - Kinshasa)',
    u'lt': 'Lithuanian',
    u'lt_LT': 'Lithuanian (Lithuania)',
    u'nds': 'Low German',
    u'nds_DE': 'Low German (Germany)',
    u'mk': 'Macedonian',
    u'mk_MK': 'Macedonian (Macedonia)',
    u'ms': 'Malay',
    u'ms_BN': 'Malay (Brunei)',
    u'ms_MY': 'Malay (Malaysia)',
    u'ml': 'Malayalam',
    u'ml_IN': 'Malayalam (India)',
    u'mt': 'Maltese',
    u'mt_MT': 'Maltese (Malta)',
    u'gv': 'Manx',
    u'gv_GB': 'Manx (United Kingdom)',
    u'mr': 'Marathi',
    u'mr_IN': 'Marathi (India)',
    u'mo': 'Moldavian',
    u'mn': 'Mongolian',
    u'mn_CN': 'Mongolian (China)',
    u'mn_Cyrl': 'Mongolian (Cyrillic)',
    u'mn_Cyrl_MN': 'Mongolian (Cyrillic) (Mongolia)',
    u'mn_MN': 'Mongolian (Mongolia)',
    u'mn_Mong': 'Mongolian (Mongolian)',
    u'mn_Mong_CN': 'Mongolian (Mongolian) (China)',
    u'ne': 'Nepali',
    u'ne_IN': 'Nepali (India)',
    u'ne_NP': 'Nepali (Nepal)',
    u'se': 'Northern Sami',
    u'se_FI': 'Northern (Sami Finland)',
    u'se_NO': 'Northern (Sami Norway)',
    u'nso': 'Northern Sotho',
    u'nso_ZA': 'Northern Sotho (South Africa)',
    u'no': 'Norwegian',
    u'nb': u'Norwegian Bokmål',
    u'nb_NO': u'Norwegian Bokmål (Norway)',
    u'nn': 'Norwegian Nynorsk',
    u'nn_NO': 'Norwegian Nynorsk (Norway)',
    u'ny': 'Nyanja',
    u'ny_MW': 'Nyanja (Malawi)',
    u'oc': 'Occitan',
    u'oc_FR': 'Occitan (France)',
    u'or': 'Oriya',
    u'or_IN': 'Oriya (India)',
    u'om': 'Oromo',
    u'om_ET': 'Oromo (Ethiopia)',
    u'om_KE': 'Oromo (Kenya)',
    u'ps': 'Pashto',
    u'ps_AF': 'Pashto (Afghanistan)',
    u'fa': 'Persian',
    u'fa_AF': 'Persian (Afghanistan)',
    u'fa_IR': 'Persian (Iran)',
    u'pl': 'Polish',
    u'pl_PL': 'Polish (Poland)',
    u'pt': 'Portuguese',
    u'pt_BR': 'Portuguese (Brazil)',
    u'pt_PT': 'Portuguese (Portugal)',
    u'pa': 'Punjabi',
    u'pa_Arab': 'Punjabi (Arabic)',
    u'pa_Arab_PK': 'Punjabi (Arabic) (Pakistan)',
    u'pa_Guru': 'Punjabi (Gurmukhi)',
    u'pa_Guru_IN': 'Punjabi (Gurmukhi) (India)',
    u'pa_IN': 'Punjabi (India)',
    u'pa_PK': 'Punjabi (Pakistan)',
    u'ro': 'Romanian',
    u'ro_MD': 'Romanian (Moldova)',
    u'ro_RO': 'Romanian (Romania)',
    u'ru': 'Russian',
    u'ru_RU': 'Russian (Russia)',
    u'ru_UA': 'Russian (Ukraine)',
    u'sa': 'Sanskrit',
    u'sa_IN': 'Sanskrit (India)',
    u'sr_YU': 'Serbian',
    u'sr': 'Serbian',
    u'sr_BA': 'Serbian (Bosnia and Herzegovina)',
    u'sr_Cyrl': 'Serbian (Cyrillic)',
    u'sr_Cyrl_YU': 'Serbian (Cyrillic)',
    u'sr_Cyrl_BA': 'Serbian (Cyrillic) (Bosnia and Herzegovina)',
    u'sr_Cyrl_ME': 'Serbian (Cyrillic) (Montenegro)',
    u'sr_Cyrl_RS': 'Serbian (Cyrillic) (Serbia)',
    u'sr_Cyrl_CS': 'Serbian (Cyrillic) (Serbia and Montenegro)',
    u'sr_Latn': 'Serbian (Latin)',
    u'sr_Latn_YU': 'Serbian (Latin)',
    u'sr_Latn_BA': 'Serbian (Latin) (Bosnia and Herzegovina)',
    u'sr_Latn_ME': 'Serbian (Latin) (Montenegro)',
    u'sr_Latn_RS': 'Serbian (Latin) (Serbia)',
    u'sr_Latn_CS': 'Serbian (Latin) (Serbia and Montenegro)',
    u'sr_ME': 'Serbian (Montenegro)',
    u'sr_RS': 'Serbian (Serbia)',
    u'sr_CS': 'Serbian (Serbia and Montenegro)',
    u'sh': 'Serbo-Croatian',
    u'sh_YU': 'Serbo-Croatian',
    u'sh_BA': 'Serbo-Croatian (Bosnia and Herzegovina)',
    u'sh_CS': 'Serbo-Croatian (Serbia and Montenegro)',
    u'ii': 'Sichuan Yi',
    u'ii_CN': 'Sichuan (Yi China)',
    u'sid': 'Sidamo',
    u'sid_ET': 'Sidamo (Ethiopia)',
    u'si': 'Sinhala',
    u'si_LK': 'Sinhala (Sri Lanka)',
    u'sk': 'Slovak',
    u'sk_SK': 'Slovak (Slovakia)',
    u'sl': 'Slovenian',
    u'sl_SI': 'Slovenian (Slovenia)',
    u'so': 'Somali',
    u'so_DJ': 'Somali (Djibouti)',
    u'so_ET': 'Somali (Ethiopia)',
    u'so_KE': 'Somali (Kenya)',
    u'so_SO': 'Somali (Somalia)',
    u'nr': 'South Ndebele',
    u'nr_ZA': 'South Ndebele (South Africa)',
    u'st': 'Southern Sotho',
    u'st_LS': 'Southern Sotho (Lesotho)',
    u'st_ZA': 'Southern Sotho (South Africa)',
    u'es': 'Spanish',
    u'es_AR': 'Spanish (Argentina)',
    u'es_BO': 'Spanish (Bolivia)',
    u'es_CL': 'Spanish (Chile)',
    u'es_CO': 'Spanish (Colombia)',
    u'es_CR': 'Spanish (Costa Rica)',
    u'es_DO': 'Spanish (Dominican Republic)',
    u'es_EC': 'Spanish (Ecuador)',
    u'es_SV': 'Spanish (El Salvador)',
    u'es_GT': 'Spanish (Guatemala)',
    u'es_HN': 'Spanish (Honduras)',
    u'es_MX': 'Spanish (Mexico)',
    u'es_NI': 'Spanish (Nicaragua)',
    u'es_PA': 'Spanish (Panama)',
    u'es_PY': 'Spanish (Paraguay)',
    u'es_PE': 'Spanish (Peru)',
    u'es_PR': 'Spanish (Puerto Rico)',
    u'es_ES': 'Spanish (Spain)',
    u'es_US': 'Spanish (United States)',
    u'es_UY': 'Spanish (Uruguay)',
    u'es_VE': 'Spanish (Venezuela)',
    u'sw': 'Swahili',
    u'sw_KE': 'Swahili (Kenya)',
    u'sw_TZ': 'Swahili (Tanzania)',
    u'ss': 'Swati',
    u'ss_ZA': 'Swati (South Africa)',
    u'ss_SZ': 'Swati (Swaziland)',
    u'sv': 'Swedish',
    u'sv_FI': 'Swedish (Finland)',
    u'sv_SE': 'Swedish (Sweden)',
    u'gsw': 'Swiss German',
    u'gsw_CH': 'Swiss German (Switzerland)',
    u'syr': 'Syriac',
    u'syr_SY': 'Syriac (Syria)',
    u'tl': 'Tagalog',
    u'tg': 'Tajik',
    u'tg_Cyrl': 'Tajik (Cyrillic)',
    u'tg_Cyrl_TJ': 'Tajik (Cyrillic) (Tajikistan)',
    u'tg_TJ': 'Tajik (Tajikistan)',
    u'ta': 'Tamil',
    u'ta_IN': 'Tamil (India)',
    u'trv': 'Taroko',
    u'trv_TW': 'Taroko (Taiwan)',
    u'tt': 'Tatar',
    u'tt_RU': 'Tatar (Russia)',
    u'te': 'Telugu',
    u'te_IN': 'Telugu (India)',
    u'th': 'Thai',
    u'th_TH': 'Thai (Thailand)',
    u'bo': 'Tibetan',
    u'bo_CN': 'Tibetan (China)',
    u'bo_IN': 'Tibetan (India)',
    u'tig': 'Tigre',
    u'tig_ER': 'Tigre (Eritrea)',
    u'ti': 'Tigrinya',
    u'ti_ER': 'Tigrinya (Eritrea)',
    u'ti_ET': 'Tigrinya (Ethiopia)',
    u'to': 'Tonga',
    u'to_TO': 'Tonga (Tonga)',
    u'ts': 'Tsonga',
    u'ts_ZA': 'Tsonga (South Africa)',
    u'tn': 'Tswana',
    u'tn_ZA': 'Tswana (South Africa)',
    u'tr': 'Turkish',
    u'tr_TR': 'Turkish (Turkey)',
    u'kcg': 'Tyap',
    u'kcg_NG': 'Tyap (Nigeria)',
    u'ug': 'Uighur',
    u'ug_Arab': 'Uighur (Arabic)',
    u'ug_Arab_CN': 'Uighur (Arabic) (China)',
    u'ug_CN': 'Uighur (China)',
    u'uk': 'Ukrainian',
    u'uk_UA': 'Ukrainian (Ukraine)',
    u'ur': 'Urdu',
    u'ur_IN': 'Urdu (India)',
    u'ur_PK': 'Urdu (Pakistan)',
    u'uz': 'Uzbek',
    u'uz_AF': 'Uzbek (Afghanistan)',
    u'uz_Arab': 'Uzbek (Arabic)',
    u'uz_Arab_AF': 'Uzbek (Arabic) (Afghanistan)',
    u'uz_Cyrl': 'Uzbek (Cyrillic)',
    u'uz_Cyrl_UZ': 'Uzbek (Cyrillic) (Uzbekistan)',
    u'uz_Latn': 'Uzbek (Latin)',
    u'uz_Latn_UZ': 'Uzbek (Latin) (Uzbekistan)',
    u'uz_UZ': 'Uzbek (Uzbekistan)',
    u've': 'Venda',
    u've_ZA': 'Venda (South Africa)',
    u'vi': 'Vietnamese',
    u'vi_VN': 'Vietnamese (Vietnam)',
    u'wal': 'Walamo',
    u'wal_ET': 'Walamo (Ethiopia)',
    u'cy': 'Welsh',
    u'cy_GB': 'Welsh (United Kingdom)',
    u'wo': 'Wolof',
    u'wo_Latn': 'Wolof (Latin)',
    u'wo_Latn_SN': 'Wolof (Latin) (Senegal)',
    u'wo_SN': 'Wolof (Senegal)',
    u'xh': 'Xhosa',
    u'xh_ZA': 'Xhosa (South Africa)',
    u'yo': 'Yoruba',
    u'yo_NG': 'Yoruba (Nigeria)',
    u'zu': 'Zulu',
    u'zu_ZA': 'Zulu (South Africa)',
}
