import numpy as np
from tools.cipher import CaesarCipher, SloganCipher, PolybianChiper,\
    TrisemusCipher, HomophonicCipher, PlayfairCipher, VigilanteCipher

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

alphabet_codes = {
    'А': ['012', '659'],
    'Б': ['128', '556'],
    'В': ['325', '026'],
    'Г': ['210', '215'],
    'Д': ['435', '436'],
    'Е': ['037', '700'],
    'Ё': ['346', '007'],
    'Ж': ['991', '995'],
    'З': ['889', '885'],
    'И': ['088', '087'],
    'Й': ['888', '643'],
    'К': ['891', '890'],
    'Л': ['456', '458'],
    'М': ['112', '119'],
    'Н': ['230', '234'],
    'О': ['064', '149'],
    'П': ['058', '073'],
    'Р': ['265', '323'],
    'С': ['347', '349'],
    'Т': ['321', '322'],
    'У': ['121', '122'],
    'Ф': ['081', '082'],
    'Х': ['075', '076'],
    'Ц': ['071', '072'],
    'Ч': ['055', '056'],
    'Ш': ['043', '044'],
    'Щ': ['041', '042'],
    'Ъ': ['032', '033'],
    'Ы': ['504', '031'],
    'Ь': ['502', '503'],
    'Э': ['501', '248'],
    'Ю': ['065', '749'],
    'Я': ['106', '098']
    }

ciphers_config = (
  {
    'name': 'Шифр Цезаря',
    'tag': 'caesar',
    'key': '5',
    'reg': True,
    'class': CaesarCipher,
    'alphabet': alphabet
   },

  {
    'name': 'Лозунговый\nшифр',
    'tag': 'slogan',
    'key': 'КЛЮЧ',
    'reg': True,
    'class': SloganCipher,
    'alphabet': alphabet
   },

  {
    'name': 'Полибианский\nквадрат',
    'tag': 'polybian',
    'key': 'КЛЮЧ',
    'reg': False,
    'class': PolybianChiper,
    'alphabet': np.array([['А','Б','В','Г','Д','Е'],
                          ['Ё','Ж','З','И','Й','К'],
                          ['Л','М','Н','О','П','Р'],
                          ['С','Т','У','Ф','Х','Ц'],
                          ['Ч','Ш','Щ','Ъ','Ы','Ь'],
                          ['Э','Ю','Я','-','-','-']])
  },

  {
    'name': 'Шифрующая\nсистема\nТрисемуса',
    'tag': 'trissemus',
    'key': 'КЛЮЧ 5 7',
    'reg': True,
    'class': TrisemusCipher,
    'alphabet': u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ&*"
  },

  {
    'name': 'Системы\nомофонов',
    'tag': 'homophones',
    'key': 'КЛЮЧ',
    'reg': False,
    'class': HomophonicCipher,
    'alphabet': alphabet_codes
  },

  {
    'name': 'Шифр\nPlayfair',
    'tag': 'playfair',
    'key': 'КЛЮЧ',
    'reg': False,
    'class': PlayfairCipher,
    'alphabet': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'
  },

 {
    'name': 'Шифр\nВижинера',
    'tag': 'vigenere',
    'key': 'КЛЮЧ',
    'reg': True,
    'class': VigilanteCipher,
    'alphabet': alphabet
  }
)

cipher_num = {c['tag']: i for i, c in enumerate(ciphers_config)}