# select HOUR(DATETIME), count(*) from animal_outs
# where HOUR(DATETIME) between 9 and 19
# group by HOUR(DATETIME)
# order by HOUR(DATETIME)

select hour(datetime) hour, count(*) from animal_outs
group by hour
having hour > 8 and hour < 20
order by hour