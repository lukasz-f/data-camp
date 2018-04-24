from sqlalchemy import create_engine 
from sqlalchemy import Table 
from sqlalchemy import MetaData 
from sqlalchemy import select 
from sqlalchemy import and_

debug = True 
new_income_ids = ['02', '03', '04', '05', '06', '12', '14', '15', '16', '17', '19', '20', '21', '23']
output_file_name = '0101-fed-INCOMESELD.sql'

script_header = """declare
  record_dict_def fed_utils_dict.T_TYPE_DICT_DEF;
  record_dict fed_utiis_dict.t_type_dict;
  record_dict_val fed_utils_dict.t_type_dict_val; 
  tab_dict_val fed_utils_dict.t_table_dict_val:=fed_utils_dict.t_table_dict_val();
begin
"""

script_footer = """
end:
/
commit;
exit 0;
"""

script_dict_def = """
  -- jakiś tam skrypt sql
"""

script_dict = """
  --DICT--
  record_dict.tt_dict_def:=record_dict_def;
  record_dict.t_sKey:='{0}';
  record_dict.t_nUniqueKey:='{0}{1}B';
  record_dict.t_sAttrName:='B';
"""

script_dict_val = """
  --1--
  record_dict_val.tt_dict:=record_dict;
  record_dict_val.t_sKey:='defaultValue';
  record_dict_val.t_sValue:='{defaultValue}';

  --2--
  record_dict_val.tt_dict:=record_dict;
  record_dict_val.t_sKey:='indicatorEditabled';
  record_dict_val.t_sValue:='{indicatorEditabled}';

  --3--
  record_dict_val.tt_dict:=record_dict;
  record_dict_val.t_sKey:='indicatorRequirment';
  record_dict_val.t_sValue:='{indicatorRequirment}';

  --4--
  record_dict_val.tt_dict:=record_dict;
  record_dict_val.t_sKey:='indicatorVisibility';
  record_dict_val.t_sValue:='{indicatorVisibility}';

  --5--
  record_dict_val.tt_dict:=record_dict;
  record_dict_val.t_sKey:='sourceFortune';
  record_dict_val.t_sValue:='{sourceFortune}';
"""


engine = create_engine('oracle+cx_oracle://user:pass@db-host:port/db-name', implicit_returning=False)
if debug: print('DB tables:', engine.table_names())

conn = engine.connect() 
metadata = MetaData()

dict_def = Table('dict_def', metadata, autoload=True, autoload_with=engine) 
if debug: print('TABLE dict_def columns:', dict_def.columns.keys())

dict = Table('dict', metadata, autoload=True, autoload_with=engine) 
if debug: print('TABLE dict columns:', dict.columns.keys())

dict_val = Table('dict_val', metadata, autoload=True, autoload_with=engine) 
if debug: print('TABLE dict_val columns:', dict_val.columns.keys())


dict_def_stmt = (select([dict_def.columns.id])
                 .where(
                        and_(dict_def.columns.name == 'INCOMESFLD',
                             dict_def.columns.dict_group == 'MOK')
                 ))
if debug: print('dict_def select', dict_def_stmt)

dict_def_results = conn.execute(dict_def_stmt).first() 
if debug: print('select result:', dict_def_results)

dict_def_id, = dict_def_results 
if debug: print('INCOMESFLD id:', dict_def_id)


with open(output_file_name, 'w', encoding="utf-8") as output_file:
    output_file.write(script_header)
    output_file.write(script_dict_def)

    for income_id in new_income_ids:
        dict_stmt = (select([dict])
                     .where(
                            and_(dict.columns.dict_def_id == dict_def_id,
                                 dict.columns.unique_key.like('%{}C'.format(income_id)))
                     )
                     .order_by(dict.columns.unique_key))
        if debug: print('dict select:', dict_stmt)

        dict_results = conn.execute(dict_stmt).fetchall()
        for dict_row in dict_results:
            if debug: print(dict_row.key, dict_row.unique_key, dict_row.attr_name)
            output_file.write(script_dict.format(dict_row.key, income_id))

            dict_id = dict_row.id 
            dict_val_stmt = (select([dict_val])
                             .where(dict_val.columns.dict_id == dict_id)
                             .order_by(dict_val.columns.key))
            if debug: print('dict_val select:', dict_val_stmt)

            dict_val_results = conn.execute(dict_val_stmt).fetchall() 
            data = {} 
            for dict_val_row in dict_val_results:
                if debug: print(dict_val_row.key, dict_val_row.value) 
                data[dict_val_row.key] = dict_val_row.value if dict_val_row.value is not None else ''

            if debug: print('dict_val data:', data) 
            output_file.write(script_dict_val.format (**data))

        output_file.write(script_footer)

conn.close()
engine.dispose()
