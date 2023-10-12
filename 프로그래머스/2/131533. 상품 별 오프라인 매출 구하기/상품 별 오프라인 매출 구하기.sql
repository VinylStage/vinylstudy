select PRODUCT_CODE, sum(price*sales_amount) SALES from product a
inner join offline_sale b
using (product_id)
group by product_code
order by sales desc, product_code