# 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
SELECT
b.TITLE,
b.BOARD_ID,
r.REPLY_ID,
r.WRITER_ID,
r.CONTENTS,
DATE_FORMAT(r.CREATED_DATE,'%Y-%m-%d')
from USED_GOODS_BOARD b
inner join USED_GOODS_REPLY r
on b.BOARD_ID = r.BOARD_ID
where b.CREATED_DATE LIKE '2022-10%'
order by r.CREATED_DATE ASC, b.TITLE ASC