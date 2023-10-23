select a.animal_id, a.name
from animal_ins a, animal_outs b
where a.animal_id = b.animal_id
order by datediff(a.datetime, b.datetime)
limit 2