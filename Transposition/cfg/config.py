import numpy as np
from tools.cipher import SingleTransposition, BlockTransposition, TableTransposition,\
    VerticalTransposition, DoubleTransposition, MagicSquare, RotaryTransposition

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

ciphers_config = (
  {
    'name': 'Простая\nодинарная',
    'tag': 'simple',
    'key': '3',
    'reg': True,
    'class': SingleTransposition,
    'alphabet': alphabet
   },

  {
    'name': 'Блочная\nперестановка',
    'tag': 'block',
    'key': '3',
    'reg': False,
    'class': BlockTransposition,
    'alphabet': alphabet
   },

  {
    'name': 'Табличная\nмаршрутная',
    'tag': 'table',
    'key': '4',
    'reg': False,
    'class': TableTransposition,
    'alphabet': alphabet
  },

  {
    'name': 'Вертикальная\nперестановка',
    'tag': 'vertical',
    'key': 'ДЯДИНА',
    'reg': False,
    'class': VerticalTransposition,
    'alphabet': alphabet
  },
#
  {
    'name': 'Поворотн\nрешетки',
    'tag': 'bars',
    'key': '5',
    'reg': False,
    'class': RotaryTransposition,
    'alphabet': alphabet
  },

  {
    'name': 'Магический\nквадрат',
    'tag': 'magic',
    'key': '',
    'reg': False,
    'class': MagicSquare,
    'alphabet': alphabet
  },

 {
    'name': 'Двойная\nперстановка',
    'tag': 'double',
    'key': '543210 543210',
    'reg': True,
    'class': DoubleTransposition,
    'alphabet': np.array([['А','Б','В','Г','Д','Е'],
                        ['Ё','Ж','З','И','Й','К'],
                        ['Л','М','Н','О','П','Р'],
                        ['С','Т','У','Ф','Х','Ц'],
                        ['Ч','Ш','Щ','Ъ','Ы','Ь'],
                        ['Э','Ю','Я','-','_',' ']])
  }
)

cipher_num = {c['tag']: i for i, c in enumerate(ciphers_config)}