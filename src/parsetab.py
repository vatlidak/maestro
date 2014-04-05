
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xca|\xc8\x1f\x8e\xf9\x18\xb5\xc1\x805\x87\xbf\xd5\x81R'
    
_lr_action_items = {'RP':([1,2,7,10,11,12,13,14,15,17,18,],[-3,-9,13,-5,17,-2,-8,-7,-6,-1,-4,]),'LP':([0,2,3,5,6,8,9,16,],[3,5,3,3,3,3,3,3,]),'DEP':([1,2,4,7,10,12,13,14,15,17,18,],[-3,-9,8,8,8,8,-8,-7,-6,-1,8,]),'ASSIGN':([2,],[6,]),'COMMA':([1,2,10,11,12,13,14,15,17,18,],[-3,-9,-5,16,-2,-8,-7,-6,-1,-4,]),'STR':([0,3,5,6,8,9,16,],[1,1,1,1,1,1,1,]),'NODEP':([1,2,4,7,10,12,13,14,15,17,18,],[-3,-9,9,9,9,9,-8,9,-6,-1,9,]),'ID':([0,3,5,6,8,9,16,],[2,2,2,2,2,2,2,]),'$end':([1,2,4,12,13,14,15,17,],[-3,-9,0,-2,-8,-7,-6,-1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'E':([0,3,5,6,8,9,16,],[4,7,10,12,14,15,18,]),'LII':([5,],[11,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> E","S'",1,None,None,None),
  ('E -> ID LP LII RP','E',4,'p_func_call','myacc.py',13),
  ('E -> ID ASSIGN E','E',3,'p_assign','myacc.py',20),
  ('E -> STR','E',1,'p_e_str','myacc.py',25),
  ('LII -> LII COMMA E','LII',3,'p_list_inside_grow','myacc.py',38),
  ('LII -> E','LII',1,'p_list_inside_orig','myacc.py',42),
  ('E -> E NODEP E','E',3,'p_e_nodep','myacc.py',46),
  ('E -> E DEP E','E',3,'p_e_dep','myacc.py',50),
  ('E -> LP E RP','E',3,'p_e_parenthesize','myacc.py',54),
  ('E -> ID','E',1,'p_e_id','myacc.py',59),
]