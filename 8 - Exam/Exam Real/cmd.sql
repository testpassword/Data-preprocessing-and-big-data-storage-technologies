# Please count the amount of all observations when the stop time of the TROLLEY at the stop with the ID_STOP 15055 has not been fixed.
SELECT COUNT(*) FROM track
WHERE 
  id_vehicle IN (
    SELECT id_vehicle FROM vehicle
    WHERE vehicle_name_en LIKE 'TROLLEY'
  ) AND
  id_stop = 15055 AND
  stop_time_real IS NULL;

# What is the length of the BUS route number 30 in the RETURN direction?
SELECT SUM(distance_back) FROM route_by_stops
WHERE 
  route_number = 30 AND
  id_vehicle IN (
    SELECT id_vehicle FROM vehicle 
    WHERE vehicle_name_en LIKE 'BUS'
  ) AND
  id_direction IN (
    SELECT id_direction FROM direction 
    WHERE direction_type_en LIKE 'RETURN'
  );

# How many TROLLEYes (with different board numbers) have been in operation of city routes on September 10, 2019 during the period from [09:00:00 - 10:00:00)?
SELECT COUNT(*) FROM (
  SELECT DISTINCT carrier_board_num FROM track
  WHERE
    id_vehicle IN (
      SELECT id_vehicle FROM vehicle
      WHERE vehicle_name_en LIKE 'TROLLEY'
    ) AND
    stop_time_real >= to_date('10/09/2019 09:00', 'dd/mm/yyyy hh24:mi') AND
    stop_time_real < to_date('10/09/2019 10:00', 'dd/mm/yyyy hh24:mi')
);