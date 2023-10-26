select board_id, writer_id, title, price,
case
when status like 'sale' then '판매중'
when status like 'reserved' then '예약중'
else '거래완료'
end status
from used_goods_board
where CREATED_DATE like '2022-10-05'
order by board_id desc