-- In OpenEdu you should type answer without trailing zeros, for example: 6:40 is correct, 06:40 isn't correct
SELECT * FROM (
  SELECT to_char(stop_time_real, 'dd/mm/yyyy hh24:mi') FROM track
  WHERE 
    carrier_board_num = 194105 AND
    route_number = 10 AND
    stop_time_real > to_date('10/09/2019 00:00', 'dd/mm/yyyy hh24:mi') AND 
    id_vehicle IN (
      SELECT id_vehicle FROM vehicle 
      WHERE vehicle_name_en LIKE 'BUS'
    )
  ORDER BY stop_time_real ASC
)
WHERE ROWNUM <= 1;