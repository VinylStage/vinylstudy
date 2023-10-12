SELECT animal_id, a.animal_type, a.name FROM ANIMAL_INS a
join ANIMAL_OUTS b
using (animal_id)
WHERE SEX_UPON_INTAKE like 'Intact%'
and (SEX_UPON_OUTCOME  LIKE 'Spayed%'
OR SEX_UPON_OUTCOME  LIKE 'Neutered%')
order by animal_id