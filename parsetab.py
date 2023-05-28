
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABC ENTER PDER PIZQ\n    s : e1 ENTER\n    \n    e1 : PIZQ e2\n    \n    e2 : e1 PDER\n       | ABC\n    '
    
_lr_action_items = {'PIZQ':([0,3,],[3,3,]),'$end':([1,4,],[0,-1,]),'ENTER':([2,5,7,8,],[4,-2,-4,-3,]),'ABC':([3,],[7,]),'PDER':([5,6,7,8,],[-2,8,-4,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'s':([0,],[1,]),'e1':([0,3,],[2,6,]),'e2':([3,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> s","S'",1,None,None,None),
  ('s -> e1 ENTER','s',2,'p_s','parser.py',28),
  ('e1 -> PIZQ e2','e1',2,'p_e1','parser.py',34),
  ('e2 -> e1 PDER','e2',2,'p_e2','parser.py',40),
  ('e2 -> ABC','e2',1,'p_e2','parser.py',41),
]