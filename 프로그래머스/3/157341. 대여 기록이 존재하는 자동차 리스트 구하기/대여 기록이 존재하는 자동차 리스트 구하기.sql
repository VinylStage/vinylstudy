select distinct(car_id)
from CAR_RENTAL_COMPANY_CAR a join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
using (car_id)
where car_type like '세단'
and month(start_date) like 10
order by car_id desc