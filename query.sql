SELECT query, sum(click_count/log2(position+1))/sum(click_count/log2(sorted_position+1)) as ndcg
FROM (
	SELECT query as sorted_position_query, position as sorted_position, click_count as sorted_position_clicks, ROW_NUMBER() OVER(ORDER BY query, position) AS id
	from  dk_table
	ORDER by query, position) as t1
JOIN (
	SELECT *, ROW_NUMBER() OVER(ORDER BY query, click_count DESC) AS id
	from dk_table
	ORDER by query,  click_count DESC) as t2

	on t2.id = t1.id
	group by query
